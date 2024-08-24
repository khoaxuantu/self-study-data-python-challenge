
print("Nhập biểu thức với các số có 1 chữ số")
print("Các phép tính: + - x / % ")
str_input = input("Nhập phép tính: ")

res = []
list1 = []

def calcu(a, b, c):
    if b=='+':
        return a+c
    elif b=='-':
        return a-c 
    elif b=='/':
        return a/c
    elif b=='%':
        return a%c
    else:
        return a*c

def is_num(a):
    return '0'<a and a<'9'

def xu_ly(res):
    list2 = []
    list3 = []
    check = 1
    #Duyệt dấu nhân / chia
    for index, ch in enumerate(res):  
        if ch=='/' or ch=='x' or ch=='%':
            list3[-1] = calcu(list3[-1], ch, res[index+1])
            check=0
        elif check==1:
            list3.append(ch)
        else:
            check=1

    #Duyệt dấu cộng, trừ
    check=1
    for index, ch in enumerate(list3):
        if ch=='+' or ch=='-':
            list2[-1] = calcu(list2[-1], ch, list3[index+1])
            check=0
        elif check==1:
            list2.append(ch)
        else:
            check=1
    return list2[0]




#Xử lý dấu cách, số nhiều chữ số
for index, ch in enumerate(str_input):

    #Xử lý kĩ tự cách
    if (ch==' '):
        continue

    #Xử lý kĩ tự số
    elif is_num(ch):
        ch = int(ch)
        if(len(res)!=0 and type(res[-1])==int):
            res[-1] = res[-1] * 10 + ch
        else:
            res.append(ch)
    
    else:
        res.append(ch)

print(xu_ly(res))
#Gud job on finishing this project! '
#However, just to let you know, Python is famous for many convinient built-in functions: e.g: eval() and also other ways to think out of the box to finish this project.
#I hope you can look through other projects to improve yours. Feel free to ask us!