from tkinter import *
def NomalClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)
def ClearClick():
    global operator
    operator = ''
    text_Input.set(operator)
def EqualClick():
    global flag
    global operator
    global result
    flag = 0
    result = str(eval(operator))
    operator = result
    flag = 1
    text_Input.set(result)
def AnsClick():
    global operator
    global result
    operator = operator + result
    text_Input.set(operator)
def DelClick():
    global operator
    global flag
    if flag == 1: 
        text_Input.set(operator)
        return
    operator = operator[0:-1]
    text_Input.set(operator)
cal = Tk()
cal.title('CALCULATOR')
operator = ''
result= ''
flag = 0
text_Input = StringVar()
txtDisplay = Entry(cal,width = 20,font = ('arial',20,'bold'),textvariable = text_Input,insertwidth = 4, bg='white',justify = 'right').grid(columnspan = 4)
btC = Button(cal,padx = 75, fg = 'white',font = ('arial',15,'bold'),text = 'AC',command = ClearClick, bg = 'black').grid(row = 1, column = 0, columnspan = 2)
btDel = Button(cal,padx = 68, fg = 'white',font = ('arial',15,'bold'),text = 'DEL',command = DelClick, bg = 'black').grid(row = 1, column = 2, columnspan = 2)

bt7 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '7',command = lambda:NomalClick(7), bg = 'silver').grid(row = 2, column = 0)
bt8 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '8',command = lambda:NomalClick(8), bg = 'silver').grid(row = 2, column = 1)
bt9 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '9',command = lambda:NomalClick(9), bg = 'silver').grid(row = 2, column = 2)
btDe = Button(cal,padx = 35, fg = 'black',font = ('arial',15,'bold'),text = '/',command = lambda:NomalClick('/'), bg = 'pink').grid(row = 2, column = 3)

bt4 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '4',command = lambda:NomalClick(4), bg = 'silver').grid(row = 3, column = 0)
bt5 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '5',command = lambda:NomalClick(5), bg = 'silver').grid(row = 3, column = 1)
bt6 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '6',command = lambda:NomalClick(6), bg = 'silver').grid(row = 3, column = 2)
btMu = Button(cal,padx = 35, fg = 'black',font = ('arial',15,'bold'),text = '*',command = lambda:NomalClick('*'), bg = 'pink').grid(row = 3, column = 3)

bt1 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '1',command = lambda:NomalClick(1), bg = 'silver').grid(row = 4, column = 0)
bt2 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '2',command = lambda:NomalClick(2), bg = 'silver').grid(row = 4, column = 1)
bt3 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '3',command = lambda:NomalClick(3), bg = 'silver').grid(row = 4, column = 2)
btSu = Button(cal,padx = 35, fg = 'black',font = ('arial',15,'bold'),text = '-',command = lambda:NomalClick('-'), bg = 'pink').grid(row = 4, column = 3)

bt0 = Button(cal,padx = 35, fg = 'white',font = ('arial',15,'bold'),text = '0',command = lambda:NomalClick(0), bg = 'silver').grid(row = 5, column = 0)
btdot = Button(cal,padx = 37, fg = 'black',font = ('arial',15,'bold'),text = '.',command = lambda:NomalClick('.'), bg = 'pink').grid(row = 5, column = 1)
btMod = Button(cal,padx = 32, fg = 'black',font = ('arial',15,'bold'),text = '%',command = lambda:NomalClick('%'), bg = 'pink').grid(row = 5, column = 2)
btAdd = Button(cal,padx = 33, fg = 'black',font = ('arial',15,'bold'),text = '+',command = lambda:NomalClick('+'), bg = 'pink').grid(row = 5, column = 3)

btop = Button(cal,padx = 37, fg = 'black',font = ('arial',15,'bold'),text = '(',command = lambda:NomalClick('('), bg = 'pink').grid(row = 6, column = 0)
btcl = Button(cal,padx = 37, fg = 'black',font = ('arial',15,'bold'),text = ')',command = lambda:NomalClick(')'), bg = 'pink').grid(row = 6, column = 1)
btAns = Button(cal,padx = 22, fg = 'black',font = ('arial',15,'bold'),text = 'Ans',command = AnsClick, bg = 'aqua').grid(row = 6, column = 2)
btEqual = Button(cal,padx = 33, fg = 'black',font = ('arial',15,'bold'),text = '=',command = EqualClick, bg = 'aqua').grid(row = 6, column = 3)
cal.mainloop()