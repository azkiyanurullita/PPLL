from sly import Lexer

class BasicLexer(Lexer):
    tokens = {NAME, NUMBER, STRING, IF, PRINT, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ}
    ignore = '\t'

    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}

    #pendefinisian token
    IF = r'SEANDAINYO'
    PRINT = r'CETAK'
    THEN = r'MANGKONYO'
    ELSE = r'LAINNYO'
    FOR = r'UNTUK'
    FUN = r'FUNGSI'
    TO = r'SAMPAI'
    ARROW = r'->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    EQEQ = r'=='

    #token bilangan
    @_(r'\d+')
    def NUMBER(self, t):

        #konvert ke integer
        t.value = int(t.value)
        return t
    
    #token komen
    @_(r'//.*')
    def COMMENT(self, t):
        pass 

    #token newline
    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')
    
   
if __name__ == '__main__':
    lexer = BasicLexer()
    env = {}
    while True:
        try:
            text = input('pm >')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for tokens in lex:
                print(tokens)
