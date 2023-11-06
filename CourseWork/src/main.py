from LexicalAnalizer import LexicalAnalyzer

lexer = LexicalAnalyzer("input.poullang")
lexer.analysis()
if lexer.current.state!=lexer.states.ERR:
    for i in lexer.lexeme_table:
        print(i)
