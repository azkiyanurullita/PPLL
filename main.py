import pm_lexer
import pm_parser
import pm_interpreter

from sys import *

#masukan langsung
if __name__ == '__main__':
    lexer = pm_lexer.BasicLexer()
    parser = pm_parser.BasicParser()
    env = {}

    while True:
        try:
            text = input('pm > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            pm_interpreter.BasicExecute(tree, env)
