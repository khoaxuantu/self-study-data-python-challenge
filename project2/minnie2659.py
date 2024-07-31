import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.current_result = 0

    def cal(self, expression):
        try:
            # Evaluate the expression safely
            result = eval(expression)
            return result
        except ZeroDivisionError:
            raise ValueError("Error: Division by zero.")
        except Exception as e:
            raise ValueError(f"Error: {e}")

class CalculatorApp:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        root.geometry("340x320")
        self.root.title("Calculator")
        self.root.config(bg='light blue')

        self.expression = ""
        self.input_text = tk.StringVar()

        self.input_frame = tk.Frame(self.root)
        self.input_frame.config(bg='light blue')
        self.input_frame.pack()

        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, width=22, justify='right', font=('arial', 18, 'bold'))
        self.input_field.grid(row=0, column=0, padx=10, pady=10)
        #self.input_field.pack(ipady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.config(bg='light blue')
        self.buttons_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('-', 1, 3), ('*', 2, 3), ('/', 3, 3), ('=', 4, 3),
            ('(', 4, 0), ('CE', 0, 0), ('C', 0, 1),
            (')', 4, 2), ('+', 0, 3), ('%', 0, 2)
        ]

        # Add padding between rows
        row_padding = {1: 5, 2: 5, 3: 5, 4: 10}  
        
        for (text, row, column) in buttons:
            if text == '=':
                button = tk.Button(self.buttons_frame, text=text, width=5, bg='red', fg = 'white', font=("arial", 14), command=self.calculate_result)
            else:
                button = tk.Button(self.buttons_frame, text=text, width=5, font=("arial", 14), command=lambda t=text: self.button_click(t))
            pady_value = row_padding.get(row, 5)  
            button.grid(row=row, column=column, padx=5, pady=pady_value)

    def button_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == 'CE':
            self.expression = self.expression[:-1]
        elif char == '=':
            self.calculate_result()
        else:
            self.expression += str(char)
        self.input_text.set(self.expression)

    def calculate_result(self):
        try:
            result = self.calc.cal(self.expression)
            self.expression = str(result)
        except ValueError as e:
            self.expression = ""
            messagebox.showerror("Error", str(e))
        self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    
    app = CalculatorApp(root)
    root.mainloop()
