from LexicalAnalizer import LexicalAnalyzer
from SyntacticalAnalyzer import SyntacticalAnalyzer

PRINT_LEXEMES = True
PATH_TO_PROGRAM = "first_program.poullang"

lexer = LexicalAnalyzer(PATH_TO_PROGRAM)
lexer.analysis()
if lexer.current.state != lexer.states.ERR:
    if PRINT_LEXEMES:
        for i in lexer.lexeme_table:
            print(f"{i.token_name} {i.token_value}")

    syntaxAnalyzer = SyntacticalAnalyzer(lexer.lexeme_table)
    syntaxAnalyzer.PROGRAMM()