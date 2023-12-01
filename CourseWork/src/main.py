from LexicalAnalizer import LexicalAnalyzer
from SyntacticalAnalyzer import SyntacticalAnalyzer
lexer = LexicalAnalyzer("second_program.poullang")
lexer.analysis()
if lexer.current.state != lexer.states.ERR:
    for i in lexer.lexeme_table:
        print(f"{i.token_name} {i.token_value}")

    syntaxAnalyzer = SyntacticalAnalyzer(lexer.lexeme_table)

    syntaxAnalyzer.PROGRAMM()