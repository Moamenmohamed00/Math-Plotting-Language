import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
def execute_plot_command(result, canvas_frame):
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
    fig = plt.figure(figsize=(5, 4), dpi=100)
    plt.plot(x, y)
    plt.title(f"Plot of: {expr_str}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

# while True:
#     text = input('calc>> ')
#     if text.lower() in ['exit', 'quit']:
#         break
#     lexer = Le(text)
#     token = lexer.generate_tokens()
#     parser = Parser(token)
#     result = parser.parse()
#     if result["command"] == "PLOT":
#         execute_plot_command(result)
# Remove previous canvas
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


# ------------------ GUI APPLICATION ------------------ #
ctk.set_appearance_mode("dark")  # light / dark / system
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Math Plotting Language GUI")
app.geometry("900x600")

# Input Frame
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=15, padx=15, fill="x")

label = ctk.CTkLabel(input_frame, text="Enter Plot Command:")
label.pack(anchor="w", padx=10, pady=5)

entry = ctk.CTkEntry(input_frame, height=40, font=("Arial", 18))
entry.pack(fill="x", padx=10)

error_label = ctk.CTkLabel(input_frame, text="", text_color="red")
error_label.pack(anchor="w", padx=10, pady=5)

# Canvas Frame
canvas_frame = ctk.CTkFrame(app)
canvas_frame.pack(pady=10, padx=10, fill="both", expand=True)


# BUTTON FUNCTION
def on_plot():
    command = entry.get().strip()

    if command.lower() in ["exit", "quit"]:
        app.destroy()
        return

    try:
        lexer = Le(command)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        result = parser.parse()

        error_label.configure(text="")  # clear errors
        execute_plot_command(result, canvas_frame)

    except Exception as e:
        error_label.configure(text=f"Syntax Error: {str(e)}\nExample: PLOT sin(x) FROM 0 TO 10")


# Plot Button
plot_button = ctk.CTkButton(app, text="Plot", command=on_plot, height=40, font=("Arial", 18))
plot_button.pack(pady=10)

# Quit Button
quit_button = ctk.CTkButton(app, text="Quit", command=app.destroy, height=40, fg_color="red")
quit_button.pack(pady=5)

app.mainloop()
# calc>>  PLOT sin(x) + x**2 FROM -5 TO 5
# calc>>  PLOT sin(x) + x**2 FROM -5 TO 200
# calc>>  PLOT 3*cos(x) - 2*x FROM 0 TO 10
# calc>> PLOT sqrt(x) FROM 0 TO 50
# calc>> PLOT ((x**2 + sin(x))*(log(x+10)+exp(-x)))/(1+cos(x))