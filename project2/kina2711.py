import tkinter as tk
from tkinter import font as tkfont
import winsound
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(False, False)
        
        self.expression = ""
        self.result_var = tk.StringVar()
        self.last_result = False
        self.error_state = False

        self.create_widgets()

    def create_widgets(self):
        large_font = tkfont.Font(family="Helvetica", size=30, weight="bold")
        self.display = tk.Entry(self, textvariable=self.result_var, font=large_font, bd=10, insertwidth=2, width=14,
                                borderwidth=4, relief="ridge", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=20)

        buttons = [
            ('(', 1, 0), (')', 1, 1), ('←', 1, 2), ('AC', 1, 3),
            ('X²', 2, 0), ('√', 2, 1), ('%', 2, 2), ('÷', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('x', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
            ('0', 6, 0), ('.', 6, 1), ('=', 6, 2, 2)
        ]

        for text, row, col, colspan in [(b[0], b[1], b[2], 1 if len(b) == 3 else b[3]) for b in buttons]:
            bg_color = self.get_button_color(text)
            button = tk.Button(self, text=text, bg=self.get_button_color(text), font=("Helvetica", 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=5, pady=5)

        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
            if i < 4:
                self.grid_columnconfigure(i, weight=1)

    def get_button_color(self, text):
        color_map = {
            '=': "purple",
            '÷': "orange", 'x': "orange", '-': "orange", '+': "orange", '%': "orange",
            'X²': "pink", '√': "pink", '(': "pink", ')': "pink",
            'AC': "lightgreen", '←': "lightgreen"
        }
        return color_map.get(text, "lightgray")

    def on_button_click(self, char):
        winsound.Beep(600, 100)        
        if self.error_state:
            self.expression = ""
            self.error_state = False

        if char == 'AC':
            self.expression = ""
            self.last_result = False
        elif char == '=':
            self.calculate_result()
        elif char in '÷x+-%':
            if self.last_result or (self.expression == "" and char in '+-'):
                self.expression += char
                self.last_result = False
            elif self.expression and self.expression[-1] not in '÷x+-%':
                self.expression += char
        elif char == '.':
            if not self.expression or '.' not in self.expression.split()[-1]:
                self.expression += char if self.expression else '0.'
        elif char == 'X²':
            if self.expression and self.expression[-1] not in '÷x+-%':
                self.expression += '**2'
        elif char == '√':
            if self.expression and self.expression[-1] not in '÷x+-%':
                self.expression = 'math.sqrt(' + self.expression + ')'
        elif char == '←':
            self.expression = self.expression[:-1]
        else:
            if self.last_result:
                self.expression = char
                self.last_result = False
            else:
                self.expression += char

        self.result_var.set(self.expression)

    def calculate_result(self):
        try:
            self.expression = self.expression.replace("*.","*0.").replace("/.","/0.").replace("+.","+0.").replace("-.","-0.")
            if '%' in self.expression:
                self.expression = self.expression.replace('%', '%')
            self.expression = self.expression.replace('÷', '/')
            self.expression = self.expression.replace('x', '*')
            result = eval(self.expression)
            self.expression = self.format_result(result)
            self.last_result = True
        except Exception:
            self.expression = "Error"
            self.error_state = True

    def format_result(self, result):
        if isinstance(result, float):
            result = round(result, 10)
            if result.is_integer():
                result = int(result)
        return str(result)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

#Noice! You overkill this small project! Keep it up!