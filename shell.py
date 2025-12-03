from Lexer import Le
from Parser import Parser
import matplotlib.pyplot as plt
import numpy as np
import math

MATH_FUNCS = {
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "sqrt": math.sqrt,
    "log": math.log,
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e
}
def execute_plot_command(result):
    expr_tokens = result["expression"]
    start = float(result["from"])
    end = float(result["to"])

    # نحول التوكنات إلى نص معادلة (مثلاً "10*x+5")
    expr_str = ""
    for token in expr_tokens:
        if token.type in ("INT", "FLOAT"):
            expr_str += str(token.value)
        elif token.type == "IDENT":
            expr_str += token.value
        elif token.type == "PLUS":
            expr_str += "+"
        elif token.type == "MINUS":
            expr_str += "-"
        elif token.type == "MUL":
            expr_str += "*"
        elif token.type == "POW":
            expr_str += "**"
        elif token.type == "DIV":
            expr_str += "/"
        elif token.type == "LPAREN":
            expr_str += "("
        elif token.type == "RPAREN":
            expr_str += ")"

    # نجهز بيانات الرسم
    x = np.linspace(start, end, 300)
    y = []

    # نحسب y لكل قيمة من x
    for val in x:
        try:
            # نستخدم eval لتقييم المعادلة، مع السماح فقط لـ x
            y_val = eval(
                expr_str,
                  {"__builtins__": None},
                  {"x":val,**MATH_FUNCS}
                  )
            y.append(y_val)
        except Exception:
            y.append(None)

    # نرسم باستخدام matplotlib
    plt.plot(x, y)
    plt.title(f"Plot of: {expr_str}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

while True:
    text = input('calc>> ')
    if text.lower() in ['exit', 'quit']:
        break
    lexer = Le(text)
    token = lexer.generate_tokens()
    parser = Parser(token)
    result = parser.parse()
    if result["command"] == "PLOT":
        execute_plot_command(result)
# calc>>  PLOT sin(x) + x**2 FROM -5 TO 5
# calc>>  PLOT sin(x) + x**2 FROM -5 TO 200
# calc>>  PLOT 3*cos(x) - 2*x FROM 0 TO 10
# calc>> PLOT sqrt(x) FROM 0 TO 50