from sly import Lexer

class BasicLexer(Lexer):
tokens = { NAME, Number, STRING, IF, PRINT, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
ignore = '\t '

literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';'}

#Pendefinisian token
IF = r'SEANDAINYO'
PRINT = r'CETAK'
THEN = r'MANGKONYO'
ELSE = r'LAINNYO'
FOR = r'UNTUK'
FUN = r'FUNGSI'
TO = r'SAMPAI'
ARROW = r'->'
NAME = r'[a-zA-Z_] [a-Za-Z0-9_]*'
STRING = r'\".*?\"'

EQEQ = r'=='

@_(r'\d+')
def NUMBER (self, t):
t.value = int(t.value)
return tokens

@_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')
