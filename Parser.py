from Lexer import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]

    def parse(self):
        if self.current_token.type == TT_PLOT:
            return self.parse_plot_command()
        else:
            raise Exception("Expected 'PLOT' command at start")

    def parse_plot_command(self):
        self.advance()  # skip PLOT

        expr_tokens = []
        while self.current_token.type not in (TT_FROM, TT_EOF):
            expr_tokens.append(self.current_token)
            self.advance()

        if self.current_token.type != TT_FROM:
            raise Exception("Expected 'FROM' keyword")

        self.advance()  # skip FROM
        # دعم الرقم السالب
        sign = 1
        if self.current_token.type == TT_MINUS:
            sign = -1
            self.advance()

        if self.current_token.type not in (TT_INT, TT_FLOAT):
            raise Exception("Expected a number after FROM")

        start = sign * self.current_token.value
        self.advance()

        if self.current_token.type != TT_TO:
            raise Exception("Expected 'TO' keyword")

        self.advance()  # skip TO
        sign = 1
        if self.current_token.type == TT_MINUS:
            sign = -1
            self.advance()

        if self.current_token.type not in (TT_INT, TT_FLOAT):
            raise Exception("Expected a number after TO")

        end = sign * self.current_token.value
        self.advance()

        return {
            "command": "PLOT",
            "expression": expr_tokens,
            "from": start,
            "to": end
        }
