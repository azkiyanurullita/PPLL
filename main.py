#MASIH ERROR

import pm_lexer
import pm_parser
import pm_interpreter

from sys import *

#DENGAN MASUKAN .pm
lexer = pm_lexer.BasicLexer()
parser = pm_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    pm_interpreter.BasicExecute(tree, env)
