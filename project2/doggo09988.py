# pip install tkinter
import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window = tk.Tk()
window.title('Calculator')
frame = tk.Frame(master=window, bg="white")
frame.pack()
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=80)
entry.grid(row=0, column=0, columnspan=3)


def myclick(number): entry.insert(tk.END, number)


def equal():
	try:
		y = str(eval(entry.get()))
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Syntax Error")


def clear(): entry.delete(0, tk.END)

button_1 = tk.Button(master=frame, text='(', padx=25, pady=5, width=20, command=lambda: myclick('('))
button_1.grid(row=1, column=0)
button_2 = tk.Button(master=frame, text=')', padx=25, pady=5, width=20, command=lambda: myclick(')'))
button_2.grid(row=1, column=1)
button_3 = tk.Button(master=frame, text='%', padx=25, pady=5, width=20, command=lambda: myclick('%'))
button_3.grid(row=1, column=2)
button_4 = tk.Button(master=frame, text='/', padx=25, pady=5, width=20, command=lambda: myclick('/'))
button_4.grid(row=2, column=3)
button_5 = tk.Button(master=frame, text='7', padx=25, pady=5, width=20, command=lambda: myclick(7))
button_5.grid(row=2, column=0)
button_6 = tk.Button(master=frame, text='8', padx=25, pady=5, width=20, command=lambda: myclick(8))
button_6.grid(row=2, column=1)
button_7 = tk.Button(master=frame, text='9', padx=25, pady=5, width=20, command=lambda: myclick(9))
button_7.grid(row=2, column=2)
button_8 = tk.Button(master=frame, text='*', padx=25, pady=5, width=20, command=lambda: myclick('*'))
button_8.grid(row=2, column=3)
button_9 = tk.Button(master=frame, text='4', padx=25, pady=5, width=20, command=lambda: myclick(4))
button_9.grid(row=3, column=0)
button_10 = tk.Button(master=frame, text='5', padx=25, pady=5, width=20, command=lambda: myclick(5))
button_10.grid(row=3, column=1)
button_11 = tk.Button(master=frame, text='6', padx=25, pady=5, width=20, command=lambda: myclick(6))
button_11.grid(row=3, column=2)
button_12 = tk.Button(master=frame, text='-', padx=25, pady=5, width=20, command=lambda: myclick('-'))
button_12.grid(row=3, column=3)
button_13 = tk.Button(master=frame, text='1', padx=25, pady=5, width=20, command=lambda: myclick(1))
button_13.grid(row=4, column=0)
button_14 = tk.Button(master=frame, text='2', padx=25, pady=5, width=20, command=lambda: myclick(2))
button_14.grid(row=4, column=1)
button_15 = tk.Button(master=frame, text='3', padx=25, pady=5, width=20, command=lambda: myclick(3))
button_15.grid(row=4, column=2)
button_16 = tk.Button(master=frame, text='+', padx=25, pady=5, width=20, command=lambda: myclick('+'))
button_16.grid(row=4, column=3)
button_17 = tk.Button(master=frame, text='clear', padx=25, pady=5, width=20, command=clear)
button_17.grid(row=5, column=0)
button_18 = tk.Button(master=frame, text='0', padx=25, pady=5, width=20, command=lambda: myclick(0))
button_18.grid(row=5, column=1)
button_19 = tk.Button(master=frame, text='.', padx=25, pady=5, width=20, command=lambda: myclick('.'))
button_19.grid(row=5, column=2)
button_20 = tk.Button(master=frame, text='=', padx=25, pady=5, width=20, command=equal)
button_20.grid(row=5, column=3)
window.mainloop()


#You nailed it!
#Nice UI