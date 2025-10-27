from Lexer import Le
from Parser import Parser

while True:
    text = input('calc>> ')
    lexer = Le(text)
    token = lexer.generate_tokens()
    parser = Parser(token)
    result = parser.parse()
    print(result)
