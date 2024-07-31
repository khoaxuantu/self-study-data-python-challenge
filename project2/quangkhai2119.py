def A(*a):
    return sum(a)
def S(*a):
    c=0
    d=[]
    for i in a:
       d.append(i)
    c=c+d[0]
    for i in range(1,len(d)):
        c=c-d[i]
    return c
def M(*a):
    c=1
    d=[]
    for i in a:
       d.append(i)
    for i in range(0,len(d)):
        c*=d[i]
    return c
def D(*a):
    c=0
    d=[]
    for i in a:
       d.append(i)
    c=c+d[0]
    for i in range(1,len(d)):
        c=c/d[i]
    return c
def Mo(*a):
    c=0
    d=[]
    for i in a:
       d.append(i)
    c=c+d[0]
    for i in range(1,len(d)):
        c=c%d[i]
    return c
a1=input('Nhấn 1 để thực hiện tính toán 1 biểu thức; Nhấn 2 để tính từng giá trị: ')
if a1=='1':
    b1=input('Nhập biểu thức của bạn tại đây: ')
    print(f'Kết quả của biểu thức {b1}=',eval(b1))
elif a1=='2':
    print("Enter 'A' for Addition","Enter 'S' for Substraction","Enter 'M' for Multiplication","Enter 'D' for Division","Enter 'Mo' for Mode",sep='\n')
    c=0
    while True:
        while True:
            x=input('Enter Choice (A,S,M,D,Mo): ').capitalize()
            if x in ('A','S','M','D','Mo'):
                break
            else:
                print('Bạn đã nhập sai, xin hãy nhập lại: ')
        if c==0:
            m=int(input('Enter First Number: '))
        else:
            m=d
            print('First Number from Result:',m)
        n=int(input('Enter Second Number: '))
        lst=[]
        while True:
            p=input('Do you want more numbers Y/N: ').upper()
            if p=='Y':
                n1=int(input('Enter Next Number: '))
                lst.append(n1)
            elif p=='N':
                break
        dic={'A':A,'S':S,'M':M,'D':D,'Mo':Mo}
        cal={'A':'+','S':'-','M':'*','D':'/','Mo':'%'}
        for i,j in dic.items():
            if i==x:
                d=j(m,n,*lst)
                print(f'Result {m}{cal[x]}{n}{cal[x]}{lst}=',d)
                c+=1
                c1=input('Bạn có muốn tiếp tục phép toán không? Ấn Q để ngừng/ Ấn C để tiếp tục: ').upper()
                if c1=='Q':
                    break
                elif c1=='C':
                    continue
