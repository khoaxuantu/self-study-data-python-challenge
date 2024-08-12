import tkinter as tk
from math import sqrt, pi, pow

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.memory = 0
        self.expression = ""
        self.result_var = tk.StringVar()

        self.result_calculated = False  # New attribute to track if result was calculated

        self.create_widgets()

    def create_widgets(self):
        display_frame = tk.Frame(self.root)
        display_frame.pack()

        result_entry = tk.Entry(display_frame, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        result_entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('CE', 5, 0), ('AC', 5, 1), ('+/-', 5, 2), ('%', 5, 3),
            ('mc', 6, 0), ('mr', 6, 1), ('m-', 6, 2), ('m+', 6, 3),
            ('√x', 7, 0), ('π', 7, 1), ('xy', 7, 2), ('R2', 7, 3),
            ('R0', 8, 0)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(display_frame, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)

    def on_button_click(self, char):
        if char in '0123456789.':
            if self.result_calculated:
                self.expression = ''
                self.result_calculated = False
            self.expression += char
            self.result_var.set(self.expression)
        elif char in '+-×÷%xy':
            self.result_calculated = False
            if self.expression and self.expression[-1] not in '+-×÷%xy':
                self.expression += char
                self.result_var.set(self.expression)
        elif char == '+/-':
            if self.expression:
                if self.expression[0] == '-':
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
                self.result_var.set(self.expression)
        elif char == 'CE':
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression)
        elif char == 'AC':
            self.expression = ''
            self.result_var.set(self.expression)
        elif char == '=':
            self.evaluate_expression()
        elif char == 'mc':
            self.memory = 0
        elif char == 'mr':
            self.result_var.set(f"{self.memory:.2f}")
        elif char == 'm-':
            self.memory -= float(self.result_var.get())
        elif char == 'm+':
            self.memory += float(self.result_var.get())
        elif char == '√x':
            self.result_var.set(f"{sqrt(float(self.result_var.get())):.2f}")
        elif char == 'π':
            self.result_var.set(f"{pi:.2f}")
        elif char == 'R2':
            self.result_var.set(f"{round(float(self.result_var.get()), 2):.2f}")
        elif char == 'R0':
            self.result_var.set(f"{round(float(self.result_var.get()), 0):.2f}")

    def evaluate_expression(self):
        try:
            expression = self.expression.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            self.result_var.set(f"{result:.2f}")
            self.expression = f"{result:.2f}"
            self.result_calculated = True  # Set flag to indicate result was calculated
        except:
            self.result_var.set("Error")
            self.expression = ""
            self.result_calculated = False

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
#Good jobb!
#Nice clean code!