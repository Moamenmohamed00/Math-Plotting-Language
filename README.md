📄 نموذج README لـ Math-Plotting-Language
# Math-Plotting-Language

**A simple mini-language and interpreter for plotting mathematical expressions.**

## ✨ What is this

This project implements a small domain-specific language (DSL) that lets you write commands like:



PLOT sin(x) + x**2 FROM -5 TO 5


Then the interpreter:
1. Lexes (tokenizes) the input  
2. Parses the expression and plot command  
3. Evaluates and plots the mathematical function using Python and matplotlib  

In short: you get a lightweight tool to draw mathematical functions from textual commands.

## ✅ Features

- Support for integers and floats  
- Arithmetic operations: `+`, `-`, `*`, `/`, power `**`  
- Parentheses for grouping and nested expressions  
- Mathematical functions and constants: `sin`, `cos`, `tan`, `exp`, `log`, `sqrt`, `pi`, `e`, etc.  
- Plot commands with ranges: `FROM <start> TO <end>` (supports negative bounds)  
- CLI interface — type commands interactively  

## 💻 Requirements

- Python 3.x  
- `matplotlib`  
- `numpy`  
- (optional) any other math library if you extend the language  

You can install dependencies with:

```bash
pip install matplotlib numpy

🚀 How to use

Clone the repository

git clone https://github.com/Moamenmohamed00/Math-Plotting-Language.git
cd Math-Plotting-Language


Make sure you have dependencies installed

Run the shell:

python shell.py


Enter a plot command, e.g.:

PLOT sin(x) + x**2 FROM -5 TO 5


A matplotlib window will pop up showing the graph.

🧪 Example commands
PLOT sin(x) FROM 0 TO 2*pi
PLOT exp(-x**2) FROM -3 TO 3
PLOT (x**2 + 1)/(sin(x) + 2) FROM -10 TO 10
PLOT (sin(x) + x**2 + log(x+10))**2 FROM -5 TO 10


Feel free to experiment with your own expressions!

📂 Project Structure
/Math-Plotting-Language
 ├── Lexer.py      # lexical analyzer
 ├── Parser.py     # parser / syntax analyzer
 ├── shell.py      # interactive shell + plot executor
 └── README.md     # ← this file

🔧 How to contribute / Extend

If you want to extend the language (e.g. add more math functions, support more syntax, improve parser, export plots to files, …) — feel free!
Just fork the repo, create a feature branch, commit your changes and make a pull request.

⚠️ Known limitations / Future work

The parser currently only supports one variable x.

No error recovery: syntax errors or invalid math operations may crash or throw exceptions.

No support yet for saving plots (only interactive display).

No support for more complex syntax like conditionals, loops, user-defined functions.

📜 License

You can indicate here the license under which you release your project (e.g. MIT, Apache, …).
If you don’t choose a license, default GitHub behavior applies (i.e. “All rights reserved”).
