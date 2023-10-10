import re


class Token:
    def __init__(self, token_name, token_value):
        self.token_name = token_name
        self.token_value = token_value

    def toString(self):
        return f"{self.token_name}, {self.token_value}"


class LexicalAnalyser:
    def __init__(self, filename: str, states: dict, token_names: dict):
        self.states = states
        self.token_names = token_names
        self.keywords = {"for", "do"}
        self.fgetc = self.fgetc_generator(filename)
        self.symbol = ""
        self.eof_state = False
        self.error_symbol = ""
        self.current_state = self.states["H"]
        self.lexeme_table = []

    def analysis(self):
        self.current_state = self.states["H"]
        self.symbol, self.eof_state = next(self.fgetc)
        while not self.eof_state:
            if self.current_state == self.states["H"]:
                self.h_state_processing()
            elif self.current_state == self.states["ASGN"]:
                self.asgn_state_processing()
            elif self.current_state == self.states["ID"]:
                self.id_state_processing()
            elif self.current_state == self.states["ERR"]:
                self.err_state_processing()
            elif self.current_state == self.states["NM"]:
                self.nm_state_processing()
            elif self.current_state == self.states["DLM"]:
                self.dlm_state_processing()

    def h_state_processing(self):
        while not self.eof_state and self.symbol in {" ", "\n", "\t"}:
            self.symbol, self.eof_state = next(self.fgetc)
        if self.symbol.isalpha() or self.symbol == '_':
            self.current_state = self.states["ID"]
        elif self.symbol in set(list("0123456789.+-")):
            self.current_state = self.states["NM"]
        elif self.symbol == ":":
            self.current_state = self.states["ASGN"]
        else:
            self.current_state = self.states["DLM"]

    def asgn_state_processing(self):
        self.symbol, self.eof_state = next(self.fgetc)
        if self.symbol == "=":
            self.current_state = self.states["H"]
            self.add_token(self.token_names["OPER"], ":=")
            if not self.eof_state:
                self.symbol, self.eof_state = next(self.fgetc)
        else:
            self.error_symbol = ":"
            self.current_state = self.states["ERR"]

    def dlm_state_processing(self):
        if self.symbol in set(list("();")):
            self.add_token(self.token_names["DELIM"], self.symbol)
            if not self.eof_state:
                self.symbol, self.eof_state = next(self.fgetc)
            self.current_state = self.states["H"]
        elif self.symbol in set(list("<>=")):
            self.add_token(self.token_names["OPER"], self.symbol)
            if not self.eof_state:
                self.symbol, self.eof_state = next(self.fgetc)
            self.current_state = self.states["H"]
        else:
            self.error_symbol = self.symbol
            if not self.eof_state:
                self.symbol, self.eof_state = next(self.fgetc)
            self.current_state = self.states["ERR"]

    def err_state_processing(self):
        print(f"\nUnknown character: {self.error_symbol}")
        self.current_state = self.states["H"]

    def id_state_processing(self):
        buf = [self.symbol]
        if not self.eof_state:
            self.symbol, self.eof_state = next(self.fgetc)
        while not self.eof_state and (self.symbol.isalpha() or self.symbol in set(list("0123456789_"))):
            buf.append(self.symbol)
            self.symbol, self.eof_state = next(self.fgetc)
        buf = ''.join(buf)
        if self.is_keyword(buf):
            self.add_token(self.token_names["KWORD"], buf)
        else:
            self.add_token(self.token_names["IDENT"], buf)
        self.current_state = self.states["H"]

    def nm_state_processing(self):
        buf = []
        buf.append(self.symbol)
        if not self.eof_state:
            self.symbol, self.eof_state = next(self.fgetc)
        while not self.eof_state and (self.symbol in set(list("0123456789.eE+-"))):
            buf.append(self.symbol)
            self.symbol, self.eof_state = next(self.fgetc)

        buf = ''.join(buf)
        if self.is_num(buf):
            self.add_token(self.token_names["NUM"], buf)
            self.current_state = self.states["H"]
        else:
            self.error_symbol = buf
            self.current_state = self.states["ERR"]

    def is_num(self, digit):
        return re.match(r"^[\+\-]?\d*\.?\d+([eE][\+\-]?\d+)?$", digit)

    def is_keyword(self, word):
        if word in self.keywords:
            return True
        return False

    def add_token(self, token_name, token_value):
        self.lexeme_table.append(Token(token_name, token_value))

    def fgetc_generator(self, filename: str):
        with open(filename) as fin:
            s = list(fin.read())
            s.append('\n')
            for i in range(len(s)):
                yield s[i], i == (len(s) - 1)


if __name__ == "__main__":
    states = {"H": "H",
              "ASGN": "ASGN",
              "ID": "ID",
              "ERR": "ERR",
              "NM": "NM",
              "DLM": "DLM"}
    token_names = {
        "KWORD": "KWORD",
        "IDENT": "IDENT",
        "NUM": "NUM",
        "OPER": "OPER",
        "DELIM": "DELIM"
    }

    lexer = LexicalAnalyser("input.txt", states, token_names)
    lexer.analysis()
    result = {i: [] for i in token_names.keys()}
    for i in lexer.lexeme_table:
        result[i.token_name].append(i.token_value)

    for i in result:
        print(i, ":", result[i])
