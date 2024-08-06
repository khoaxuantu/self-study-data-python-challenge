#!/usr/bin/env python
# coding: utf-8

# Day 1: Introduction to Python

# In[4]:


print('Hello world!')


# In[5]:


print('anh Rùa và Chính đẹp zoai')


# Day 2: Python Variables
# 

# In[7]:


x = 5


# In[8]:


print(x)


# In[9]:


x


# In[10]:


type(x)


# In[11]:


y = 'I love Python!'


# In[12]:


print(y)


# In[13]:


type(y)


# In[14]:


y = 'I love Python!'
Y = 'I hate Python!'
print(Y)


# In[15]:


x = 5
y = x
x = 10
print(y)


# In[16]:


count = 5


# In[18]:


count = count + 5
print(count)


# In[19]:


print(c)


# In[20]:


c = 'Hello'
print (c)


# In[24]:


c[::-1]


# In[23]:


a = "Python is"
b = 'Awesome!'
print( a + b)


# Day 3: Data Types Part 1
# 

# In[1]:


num = 5
print(type(num))


# In[5]:


num1 = 7
num2 = 3.5
print(type(num1+num2))


# In[6]:


x = float(10)
print(x)


# In[7]:


num = 0b1010
print(num)


# In[9]:


num = 3.14159
is_pi = isinstance(num,float)
print(is_pi)


# In[10]:


x = 5
y = True
print(x+y)


# In[11]:


7//2


# In[16]:


x = 3.5
y = int(x)
z = float(y)
print(z)


# In[13]:





# Day 4: Data Types - Parts 2
# 

# In[1]:


s = "Python"
print(s[-3:])


# In[2]:


l1 = [1,2,3,4,5]
l1[1:4] = [10,20,30]
print(l1)


# In[4]:


s = "Python Programming"
print(s.find("Pro"))


# In[6]:


s = "Python Programming"
print(s[7:18])


# Day 5: Data Types - Parts 3
# 

# Day 6: Data Types - Parts 4
# 
# Dictionaries:
# 
# A dictionary in python is an unordered collection of items. Each item stored in a dictionary has a key and a value. You can use the key to access(truy cap) the corresponding(tuong ung) value. Dictionaies are defined(duoc xac dinh) by enclosing a comma-separated sequence of key-value pairs in curly braces{}. The key and value are separated by colon:.
# 
# 
# person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# 
# In this dictionary, 'name', 'age', and 'city' are keys, and 'Alice', 25, and 'New york' are the corresponding values.
# 
# Dictionary are mutable, which means 
# you can add, remove, or change items after the dictionary is created.
# 
# Python provides(cung cap) a variety(da dang) of methods to manipulate(van dung) dictionaries, such as getting value of a key(get), getting all keys(keys), getting all values(values), and getting all key-value pairs(items)
# 
# Converting Data Types
# 
# You'll often need to convert data from type to another. This is known as type conversion or type casting. Python provides several built-in functions(ham) that can perform these conversions(chuyen doi)
# 

# In[1]:


dict = {'name':'Alice'}
print(dict['name'])


# In[2]:


dict['city'] = 'New York'


# In[3]:


dict


# In[6]:


dict.pop('city')


# In[7]:


dict


# In[12]:


dict = {'name': 'Alice', 'age': 25}
dict['age'] = 26
print(dict)


# In[14]:


dict.keys()


# In[15]:


dict = {'name': 'Alice', 'age': 25}
print(dict.get('city', 'not found'))


# In[16]:


dict = {'name': 'Alice', 'age': 25}
for key, value in dict.items():
    print(key, value)


# In[17]:


dict = {'name': 'Alice', 'age': 25}
dict.update({'city':'newyork', 'age':26})
print(dict)


# In[19]:


dict1 = {'name': 'Alice', 'age': 25}
dict2 = {'city':'newyork', 'age':26}
dict3 = {**dict1, **dict2}


# In[20]:


dict3


# In[13]:


dict1 = {'name': 'Alice', 'age': 25}
del dict1['age']
print(dict1)


# Day 7: Operators(toan tu) - Part 1
# 
# Operators are special symbols(ky tu) that carry out arithmetic(so hoc) or logical computation. They manipulate(van dung) data values, known as operands(toan hang), to produce a result. Python supports a wide range of operators, which can be classified(phan loai) into several types: 
# 
# Comparison(so sanh) operators are used to compare values. They return either True or False according(tuy theo) to the condition(dieu kien).
# == (Equal): If the values of two operands are equal, then the condition becomes true.
# 
# != (Not Equal): If values of two operands are not equal, then the condition becomes true.
# 
# > (Greater Than): If the value of the left operand is greater than the value of the right operand, then the condition becomes true.
# 
# < (Less Than): If the value of the left operand is less than the value of the right operand, then the condition becomes true.
# 
# >= (Greater Than or Equal to): If the value of the left operand is greater than or equal to the value of the right operand, then the condition becomes true.
# 
# <= (Less Than or Equal to): If the value of the left operand is less than or equal to the value of the right operand, then the condition becomes true.
# 
# 
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
# + (Addition): Adds values on either side of the operator.
# 
# (Subtraction): Subtracts the right-hand operand from the left-hand operand.
# 
# (Multiplication): Multiplies values on either side of the operator.
# 
# / (Division): Divides the left-hand operand by the right-hand operand.
# 
# % (Modulus): Returns the remainder of the division of the left-hand operand by the right-hand operand.
# 
# ** (Exponent): Performs exponential (power) calculation on operators.
# 
# // (Floor Division): The division of operands where the result is the quotient, and the digits after the decimal point are removed.
# 
# 
# 
# Logical operators are used to combine conditional(co dieu kien) statements(cau lenh).
# and: If both the operands are true, then the condition becomes true.
# 
# or: If any of the two operands are true, then the condition becomes true.
# 
# not: Reverses the logical state of the operand.

# In[1]:


a = 10
b = 20
print(a==b)


# In[2]:


a = 5
b = 3
c = 5
print(a!=c)


# In[3]:


x = 10
y = 3
print(x%y)


# In[4]:


x = -7

y = 3
print(x%y)


# In[5]:


a = True
b = False
print(a and b)


# In[6]:


a = 10
b = 20
print(a<b and a>5)


# In[7]:


x = 5
y = 2
print(x**y)


# In[8]:


a = 4
b = 2
print(a//b)


# In[9]:


5 == 5


# In[10]:


5!=5


# In[11]:


5<2


# In[12]:


a, b = '12'
b,c ='34'
print(a+b+c)


# Day 8 Operators Part 2
# 
# 
# Membership operators test whether a value is a member of a sequence, such as a string, list, or tuple.
# 
# in: Evaluates(danh gia) to true if it finds a variable in the specified sequence and false otherwise.
# 
# not in: Evaluates to true if it does not find a variable in the specified sequence and false otherwise.
# 
# 
# Assignment(gán) operators are used to assign values to variables.
# 
# =: Assigns values from the right side operands to the left side operand.
# 
# +=, -=, =, /=, %=, *=, //=: These are compound assignment operators that perform an operation and then assign the result to the left operand. For example, x += 3 is equivalent to x = x + 3.
# 
# 
# Identity(danh tính) operators compare the memory locations of two objects(đối tượng).
# is: Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
# 
# is not: Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
# 
# 
# 
# Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.
# & (Bitwise AND): Takes two numbers as operands and does AND on every bit of two numbers. The result of AND is 1 only if both bits are 1.
# 
# | (Bitwise OR): Takes two numbers as operands and does OR on every bit of two numbers. The result of OR is 1 if any of the two bits is 1.
# 
# ^ (Bitwise XOR): Takes two numbers as operands and does XOR on every bit of two numbers. The result of XOR is 1 if the two bits are different.
# 
# ~ (Bitwise NOT): Takes one number and inverts all bits of it.
# 
# << (Bitwise Left Shift): The left operands value is moved left by the number of bits specified by the right operand.
# 
# >> (Bitwise Right Shift): The left operands value is moved right by the number of bits specified by the right operand.

# In[2]:


x = 5
y = 3
x+=y
print(x)


# In[3]:


10|4


# In[4]:


a = 10
b = 4
c = a | b
print(c)


# In[5]:


lst = [1,2,3,4,5]
print(3 in lst)


# In[6]:


a = 5
b = 2
a*=b+3
print(a)


# In[7]:


a = 6
b = 2
a%=b
print(a)


# In[9]:


x = 10
y = 4
z = x & y
print(z)


# In[10]:


a = 7
b = 3
a//=b
print(a)


# In[11]:


a = 8
b = 2
a**=b
print(a)


# Day 10 Statements - Part 2
# 
# The for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range) or other iterable objects. Iterating over a sequence is called traversal. Here's the basic syntax:
# for item in sequence:
#     # code to execute for each item
# 
# enumerate(liet ke)

# In[2]:


for i in range(1,5,2):
    print(i)


# In[3]:


for i in range(2):
    for j in range(2):
        print(i,j)


# In[12]:


for i in range(5):
    if i ==3:
        break
    print(i)
    


# In[11]:


for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(i,j)


# Day 11 Statements - Part 3
# 
# A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement.
# 
# The code within the loop, often referred to as the body of the loop, is executed repeatedly until the condition evaluates to False.
# 
# Here's the basic syntax of a while loop:
# while condition:
#     # code to execute while the condition is True
# 
# The condition is checked before each execution of the loop body. If the condition is True, the loop body is executed. If the condition is False, the loop body is skipped and the program continues with the next statement after the while loop.
# 
# he break statement is used to exit the loop prematurely when a certain condition is met. When the break statement is executed, Python terminates the loop, even if the while condition is true.
# x = 0
# while x < 10:
#     if x == 5:
#         break
#     print(x)
#     x += 1
# 
# In this example, the loop will terminate when x is equal to 5, and thus only the numbers 0 through 4 will be printed.
# 
# 
# 
# The continue statement is used to skip the rest of the code inside the current loop iteration and move on to the next iteration.
# x = 0
# while x < 10:
#     x += 1
#     if x == 5:
#         continue
#     print(x)
# 
# In this example, the number 5 will not be printed because when x is equal to 5, the continue statement is executed, and the print statement is skipped for this iteration.
# 
# The continue statement is used to skip the rest of the code inside the current loop iteration and move on to the next iteration.
# x = 0
# while x < 10:
#     x += 1
#     if x == 5:
#         continue
#     print(x)
# 
# In this example, the number 5 will not be printed because when x is equal to 5, the continue statement is executed, and the print statement is skipped for this iteration.
# 
# 
# 
# The else statement can be used with a while loop and it is executed when the condition becomes false.
# x = 0
# while x < 5:
#     print(x)
#     x += 1
# else:
#     print("x is no longer less than 5")
# 
# In this example, after the while loop has finished executing, the else statement is executed, and "x is no longer less than 5" is printed.
# 
# 
# The pass statement is a placeholder and is used when a statement is required syntactically, but you do not want any command or code to execute.
# x = 0
# while x < 5:
#     if x == 3:
#         pass
#     print(x)
#     x += 1
# 
# In this example, the pass statement does nothing when x is equal to 3. It is simply a placeholder to ensure that the code runs without any syntax errors.
# 

# In[4]:


i = 0
while i<3:
    if i ==2:
        break
    print(i, end=" ")
    i+=1


# In[5]:


i = 0
while i<3:
    print(i, end=" ")
    i+=1
else: 
    print("done")


# In[6]:


i = 0
while i<5:
    if i ==3:
        i+=1
        continue
    print(i, end=" ")
    i+=1


# In[7]:


i = 1
while i<4:
    if i ==2:
        break
    print(i, end =" ")
    i +=1
else:
        print("Loop ended normally")


# In[9]:


i = 0
while i<3:
    print(i, end=" ")
    i+=1
print(i)


# In[11]:


i = 0
s = ""
while i < 5:
    if i % 2==0:
        s+= f"{i} even"
    i+=1
print(s)


# In[13]:


i = 10
while i>0:
    print(i, end="")
    i-=3


# In[16]:


i = 0
while i<5:
    print(i,end="")
    i+=1
    if i ==3:
        break
else: 
    print("Loop completed")


# In[20]:


scores = [85,90,78,92,88,75,98,60,82,95]
for i in scores:
    if i <75:
        print( i, "Bad Grade")
    elif i >=75:
        print(i, "Good Grade")


# In[21]:


temp_per_day = [70,72,71,76,75,83,85,82,88,79,89,91,87,85,87,80]
for i in temp_per_day:
    if i >=90:
        print(i)


# In[25]:


temp_per_day = [70, 72, 71, 76, 75, 83, 85, 82, 88, 79, 89, 91, 87, 85, 87, 80]
i = 0

while i < len(temp_per_day):
    if temp_per_day[i] >= 90:
        print(temp_per_day[i])
    i += 1



# In[26]:


temp_per_day = [70, 72, 71, 76, 75, 83, 85, 82, 88, 79, 89, 91, 87, 85, 87, 80]
i = 0
while i < len(temp_per_day):
    if temp_per_day[i] >= 90:
        print(temp_per_day[i])
    i+=1


# Day 12 Statements - Part 4
# List comprehension is a concise way to create lists in Python. It's a syntactic construct that enables lists to be created from other lists (or any iterable), transforming and filtering elements in the process. This can make your code more readable and efficient.

# In[2]:


flavors = ['vanilla', 'chocolate', 'chocolate fudge', 'strawberry', 'choco swirl']
choco_flavors = []
for flavor in flavors:
    if 'choco' in flavor:
        choco_flavors.append(flavor)
print(choco_flavors)


# In[3]:


choco_flavors2 = [flavor for flavor in flavors if 'choco' in flavor]
print(choco_flavors2)


# In[4]:


new_list = [x for x in range(10) if x % 2 == 0]
print(new_list)


# Project 1: Unit of Measurement Converter Project
# 
# our task in this project is to write Python code to convert between different units. The minimum number of units you need to convert is 3, and the maximum is 6. For each additional unit beyond 3, you will earn 1 bonus point. 
# 
# For example, converting between 4 units will earn you 2 bonus point, 5 units will earn you 3 bonus points, and 6 units will earn you 4 bonus points.
# 
# Website to check: https://www.unitconverters.net/
# 
# Link: https://forms.gle/4KBCvjHmmRnWRD8JA
# 

# the correct output should look like the photo
# I've reviewed the submissions, and it seems many of you misunderstood the project. Please redo it. @Python Challenger 
# 
# You can use any measurement unit you prefer, as long as you use a minimum of 3 and a maximum of 6 units.
# 
# 
# make sure it's the same units like Length, Temperature or Area... Check the website above
#  
# Hình ảnh

# In[5]:


i = 0
while i < 3:
    j = 0
    while j < 2:
        print(i,j)
        j+=1
    i+=1


# In[6]:


new = [x**2 for x in range(1,11)]
print(new)


# In[7]:


i = 0
while i<4:
    j=0
    while j<3:
        if i==j:
            break
        print(i,j)
        j+=1
    i+=1


# In[10]:


lst= [x+y for x in [1,2,3] for y in [10,20,30]]
print(lst)


# In[11]:


i = 0
while i<3:
    j = 3
    while j>0:
        print(i,j)
        j-=1
    i+=1


# In[12]:


i = 0
while i<4:
    j=0
    while j<4:
        if i==2:
            break
        print(i,j)
        j+=1
    i+=1


# In[13]:


lst = [x*y for x in range(3) for y in range(3)]
print(lst)


# In[17]:


def convert_weight(value, from_unit, to_unit):
    # Định nghĩa các hệ số chuyển đổi từ các đơn vị về kilogram
    conversion_factors_to_kg = {
        'kilogram': 1,
        'gram': 1e-3,
        'milligram': 1e-6,
        'metric ton': 1e3,
        'long ton': 1016.0469088,
        'short ton': 907.18474,
        'pound': 0.45359237,
        'ounce': 0.02834952,
        'carat': 0.0002,
        'atomic mass unit': 1.66053906660e-27
    }
    
    # Chuyển đổi giá trị đầu vào về kilogram
    value_in_kg = value * conversion_factors_to_kg[from_unit]
    
    # Chuyển đổi từ kilogram về đơn vị đích
    conversion_factors_from_kg = {k: 1/v for k, v in conversion_factors_to_kg.items()}
    value_in_target_unit = value_in_kg * conversion_factors_from_kg[to_unit]
    
    return value_in_target_unit

# Nhận đầu vào từ người dùng
from_unit = input("Nhập tên đơn vị: ").strip()
to_unit = input("Nhập tên đơn vị cần chuyển đổi: ").strip()
value = float(input("Nhập số đơn vị: "))

# Thực hiện chuyển đổi
converted_value = convert_weight(value, from_unit, to_unit)

# Hiển thị kết quả
print(f'Kết quả: {value} {from_unit} = {converted_value} {to_unit}')


# In[ ]:


def convert_weight(value, from_unit, to_unit):
    # Định nghĩa các hệ số chuyển đổi từ các đơn vị về kilogram
    conversion_factors_to_kg = {
        'Kilogram': 1,
        'Gram': 1e-3,
        'Milligram': 1e-6,
        'Metric Ton': 1e3,
        'Long Ton': 1016.0469088,
        'Short Ton': 907.18474,
        'Pound': 0.45359237,
        'Ounce': 0.02834952,
        'Carat': 0.0002,
        'Atomic mass unit': 1.66053906660e-27
    }

    # Kiểm tra tính hợp lệ của đơn vị đầu vào
    if from_unit not in conversion_factors_to_kg:
        raise ValueError(f"Đơn vị '{from_unit}' không hợp lệ.")
    if to_unit not in conversion_factors_to_kg:
        raise ValueError(f"Đơn vị '{to_unit}' không hợp lệ.")
    
    # Chuyển đổi giá trị đầu vào về kilogram
    value_in_kg = value * conversion_factors_to_kg[from_unit]

    # Chuyển đổi từ kilogram về đơn vị đích
    value_in_target_unit = value_in_kg / conversion_factors_to_kg[to_unit]

    return value_in_target_unit

# Nhận đầu vào từ người dùng
from_unit = input("Enter Starting Unit of Measurement(Kilogram, Gram, Milligram, Metric Ton, Long Ton, Short Ton, Pound, Ounce, Carat, Atomic mass unit): ").strip()
to_unit = input("Enter Unit of Measurement to Convert to(Kilogram, Gram, Milligram, Metric Ton, Long Ton, Short Ton, Pound, Ounce, Carat, Atomic mass unit): ").strip()
value = float(input(f"Enter Starting Measurement in ({from_unit}): "))

# Thực hiện chuyển đổi
try:
    converted_value = convert_weight(value, from_unit, to_unit)
    # Hiển thị kết quả
    print(f'Result [alue} {from_unit} = {converted_value} {to_unit}')
except ValueError as e:sad
    print(e)


# In[37]:


def convert_weight(value, from_unit, to_unit):
    conversion_factors_to_kg = {
        'Kilogram': 1,
        'Gram': 1000,
        'Milligram': 1000000,
        'Metric Ton': 0.001,
        'Long Ton': 0.0009842073,
        'Short Ton': 0.0011023122,
        'Pound': 2.2046244202,
        'Ounce': 35.273990723,
        'Carat': 5000,
        'Atomic mass unit': 6.022136652e+26
    }

    # Convert Starting value to kilogram
    value_in_kg = value * conversion_factors_to_kg[from_unit]

    # Convert from kilogram to the target unit
    value_in_target_unit = value_in_kg / conversion_factors_to_kg[to_unit]

    # Round to the nearest integer
    return round(value_in_target_unit)

# Receive input
from_unit = input("Enter Starting Unit of Measurement (Kilogram, Gram, Milligram, Metric Ton, Long Ton, Short Ton, Pound, Ounce, Carat, Atomic mass unit): ").strip()
to_unit = input("Enter Unit of Measurement to Convert to (Kilogram, Gram, Milligram, Metric Ton, Long Ton, Short Ton, Pound, Ounce, Carat, Atomic mass unit): ").strip()
value = int(input(f"Enter Starting Measurement in {from_unit}: "))

# Starting convert
try:
    converted_value = convert_weight(value, from_unit, to_unit)
    # Result
    print(f'Result: {value} {from_unit} = {converted_value} {to_unit}')
except KeyError:
    print("Error: Invalid unit entered. Please check your units and try again.")
#final


# In[36]:


def convert_weight(value, from_unit, to_unit):
    conversion_factors_to_kg = {
        'Kilogram': 1,
        'Gram': 1000,
        'Milligram': 1000000,
        'Metric Ton': 0.001,
        'Long Ton': 0.0009842073,
        'Short Ton': 0.0011023122,
        'Pound': 2.2046244202,
        'Ounce': 35.273990723,
        'Carat': 5000,
        'Atomic mass unit': 6.022136652e+26
    }

    # Convert Starting value to kilogram
    value_in_kg = value * conversion_factors_to_kg[from_unit]

    # Convert from kilogram to the target unit
    value_in_target_unit = value_in_kg / conversion_factors_to_kg[to_unit]

    return value_in_target_unit

# Receive input
from_unit = input("Enter Starting Unit of Measurement (Kilogram, Gram, Milligram, Metric Ton, Long Ton, Short Ton, Pound, Ounce, Carat, Atomic mass unit): ").strip()
to_unit = input("Enter Unit of Measurement to Convert to (Kilogram, Gram, Milligram, Metric Ton, Long Ton, Short Ton, Pound, Ounce, Carat, Atomic mass unit): ").strip()
value = int(input(f"Enter Starting Measurement in {from_unit}: "))

# Starting convert
try:
    converted_value = convert_weight(value, from_unit, to_unit)
    # Result
    print(f'Result: {value} {from_unit} = {converted_value} {to_unit}')
except KeyError:
    print("Error: Invalid unit entered. Please check your units and try again.")


# Day 13 Functions - Part 1
# 
# A function is a block of organized(khối tổ chức), reusable(tái sử dụng) code that is used to perform(biểu diễn) a single, related(có liên quan) action. Functions provide better modularity(mo-dun hóa) for your application(ứng dụng) and a high degree of code reusing.
# 
# You can define(định nghĩa) functions to provide the required(yêu cầu) functionality. Here are simple rules to define a function in Python:
# 
# Function blocks begin with the keyword def followed by the function name and parentheses ().
# 
# Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.
# 
# The code block within every function starts with a colon : and is indented.
# 
# 
# The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

# # 

# In[38]:


def add(a,b):
    return a+b
result = add(2,3)+add(4,5)
print(result)


# In[39]:


def mul(x,y=2):
    return x*y
result = mul(3)
print(result)


# In[40]:


def func(x,y):
    x = x+ y
    y = x - y
    x = x-y
    return x,y
result = func(5,10)
print(result)


# In[45]:


def outer():
    x = 5
    def inner():
        nonlocal x
        x = 10
    inner()
    return x

resul = outer()
print(result)


# In[47]:


def func(a,b=5,c=10):
    return a+b+c
result = func(1,c=2)
print(result)


# In[48]:


def func(a,b, *args):
    return a+b+sum(args)
result = func(1,2,3,4,5)
print(result)


# In[49]:


def func(a,b,**kwargs):
    return a+b+kwargs['c']
result = func(1,2,c=3)
print(result)


# In[50]:


def func(a,b=2,c=3):
    return a+b+c
result = func(c=5, a=1)
print(result)


# In[52]:


def func(a,b, c=1):
    return a*b*c
result = func(2,3)
print(result)


# In[54]:


def func(a,b=0):
    return a-b
result = func(b=2,a=5)
print(result)


# Day 14 Functions - Parts 2
# 
# Default and Arbitrary(tuy y) Arguments(lap luan) 
# 
# Default arguments are used to provide default values for parameters(tham so) in a funtion(ham). If an Argument is not provided when the function is called, the defailt value will be used instead(thay the). This allows(cho phep_ for more flexible(linh hoat) function calls.
# 
# Arbitrary arguments, also known as varargs or variable(bien doi)-length arguments, allows a function to accept an arbitrary number of arguments. This is useful when you dont know advance(huu ich) how many arguments will be passed to the function.
# 
# 

# In[1]:


def func(a,b):
    """this function adds two numbers"""
    return a+b
result = func.__doc__
print(result)


# In[2]:


def multiply(x,y=1):
    return x*y
result = multiply(4,3)
print(result)


# In[14]:


def func(*args):
    return sum(args)
result = func([1,2,3,4,5])
print(result)


# In[4]:


def mul(*args):
    return args*2
result = mul([1,2,3,4,5])
print(result)


# In[8]:


def func():
    """
    """
    return
result = func.__doc__
print(result)


# In[9]:


def func(a,b=1,*,c=2, d=3):
    return a+b+c+d
result=func(1,d=4)
print(result)


# In[13]:


def func(*args):
    return sum(*args)
result = func([4, 5])
print(result)



# In[15]:


def func(a,b=1, *args):
    return a+b+sum(args)
result = func(1,2,[3,4])
print(result)


# In[16]:


def func(a, *args):
    return a+ sum(args)
result = func(1,2,3,x=4,y=5)
print(result)


# Day 15 Functions Part 3
# 
# Keyword arguments(doi so), also known as named arguments, allow you to pass arguments to a function using the parameter(tham so) names. This provides clarity(ro rang) and avoids confution(su nham lan) when calling functions with multiple arguments.
# 
# Arbitrary(bat ky) keyword arguments, also known as kwargs (keyword arguments), allow a function to accept an arbitrary number of named arguments. This is useful when you want to provide flexibility and handle(xu ly) various(nhieu) parameters without explicitly(ro rang) defining(xac dinh) them.
# 
# Lambda Functions
# 
# Lambda functions, also known as anonymous(vo danh) functions allow you to create small. one-line funtions without a formal(chinh thuc) funtions definition(su dinh nghia).
# 
# They are typically(tieu bieu) used for simple and short operations(hoat dong) where a named function is not necessary(can thiet). Lambda keyword followed by the funtions's parameters and a single expression(biet thuc).
# 
# print and return are both used in funtions, but they a serve different purposes(muc dich) and have different effects on the program's behavior. Let's explore(kham pha) the differences between print and return in functions.
# 
# Print Statement
# 
# The print Statement in Python is used to display text or the value of an expression to the console(bang dieu khien). It outputs the specified(chi dinh) information as text, which is visible(de thay) when the program is excuted(thuc thi). The primary purpose of print is to provide information to the user or to assist in debugging.
# 
# Note that when you use print inside a function, it will only display the output the console. It does not affect the flow of program or the value returned by the function.
# 
# Return Statement
# 
# The return statement in Python is used to specify(chi dinh) the value that a function should return. It allows you to obtain(dat duoc) the result of a function's computation(tinh toan) and use it for further processing or assignments(gian tiep). When a return statement is encountered(tra ve), the function immediately(ngay lap tuc) exits, and the specified value is returned to the caller

# In[1]:


def func(a,b=2,c=3):
    return a*b+c
result = func(4,c=5)
print(result)


# In[2]:


add = lambda x,y: x+y
result = add(5,10)
print(result)


# In[3]:


log = lambda*args: print(*args)
has_money = False
def func():
    if not has_money:
        log("you are poor", "hehe")
func()


# In[4]:


def func(**kwargs):
    return sum(kwargs.values())
result = func(a=1,b=2,c=3)
print(result)


# In[7]:


def outer(x):
    def inner(y):
        return x+y
    return inner
result = outer(5)(10)
print(result)


# In[8]:


nums=[1,2,3,4]
result = list(map(lambda x:x**2, nums))
print(result)


# In[9]:


func = lambda x,y: x if x > y else y
print(func(5,10))


# In[10]:


def make_incrementor(n):
    return lambda x:x-n
f = make_incrementor(10)
result = f(5)
print(result)


# In[11]:


make_multiplier = lambda n: lambda x:x*n
double = make_multiplier(2)
trible = make_multiplier(3)
print(double(5)*trible(5))


# Day 16 - Built-in-Modules
# 
# Import Modules and Exloring(kham pha) The Standard Library
#  In this Python Beginer Tutorial, welcome to our second tutor, Corey Shafer. We will begin learning how to import modules in Python. We will learn how to import modules we have written, as well as modules from the Standard Library. We will also explore sys.path and how imported modules are found.
# 
# OS Module - Use Underlying Operating System Functionality.
# 
# In this Python tutorial, we will be going over the 'os' module. the os module allows us to access(truy cap) functionality(chuc nang) of the underlying operating system. So we can perform(thuc hien) task such as: navigate(dieu huong) the file systeam, obtain(dat duoc) file information, rename files, search diretory trees, fetch(tim ve) enviroment variables, and many other operations. We will cover alot of what the os module has to offer in this rutorial, so let's get started.
#  

# In[1]:


One parameter will be the how much we sell something for and the other is how much it costs to purchase for us.

the funtion will take the sell price and subtract the cost price


# In[4]:


def calculate_profit(price, cost):
    profit = price - cost
    return profit

# Get user input for price and cost
price = float(input("Enter the selling price: "))
cost = float(input("Enter the cost price: "))

# Calculate profit
profit = calculate_profit(price, cost)

# Print the profit
print(f"The profit is: {profit}")


# In[5]:


create a function that takes all ò the values being pased through, adds themtogether, and then prints the output. There could be any number of values passed in so use an arbitrary argument to be flexible.


# In[15]:


def calculate_sum(*args):
    total = sum(args)
    print(f"The sum is: {total}")

# Get user input for numbers, separated by spaces
user_input = input("Enter the numbers separated by spaces: ")

# Convert the input string to a list of floats
numbers = list(map(float, user_input.split()))

# Call the function with the list of numbers unpacked
calculate_sum(*numbers)


# In[16]:


def calculate_sum(*args):
    total = sum(args)
    print(f"The sum is: {total}")
    
#Input for numbers
calculate_sum(5, 10, 15, 20)



# In[17]:


def calculate_profit(price, cost):
    profit = price - cost
    return profit

# Get user input for price and cost
price =  150
cost = 100

# Calculate profit
profit = calculate_profit(price, cost)

# Print the profit
print(f"The profit is: {profit}")



# Day 17 Built - In Functions - Parts
# 
# Built-in functions in Python are pre-defined functions that are always available for use, providing essential operations like input/output, data type conversion, mathematical calculations, and data manipulation, without requiring any additional imports. They help simplify coding tasks and improve efficiency by offering commonly used functionality directly within the language.
# 
# Input, Enumerate, and Append
# First of all, let's get started with input, enumerate, and append. 
# 
# Len
# The built-in len function in Python returns the number of items in an object, such as a list, string, or dictionary, providing a simple way to determine the size or length of various data structures.
# Range
# The built-in range function in Python generates a sequence of numbers, commonly used for iterating a specific number of times in for-loops, with customizable start, stop, and step values.
# 
# Slice
# The built-in slice function in Python creates a slice object representing a set of indices specified by start, stop, and step, which can be used to extract portions of sequences like lists, tuples, or strings.
# Round
# The built-in round function in Python returns a floating-point number rounded to a specified number of decimal places, with the default being zero decimal places, making it useful for simplifying numerical values.

# In[2]:


lst=[]
for i in range(3):
    item = input("enter item: ")
    lst.append(item)
print(lst)





# In[3]:


lst = [10,20,30,40,50]
result = len(range(len(lst)))
print(result)


# In[4]:


lst = [1,2,3,4,5]
s = slice(1,4)
print(lst[s])


# In[5]:


result = round(3.14159, 2)
print(result)


# In[8]:


user_input = input("enter a string: ")
result = len(user_input)
print(result)


# In[9]:


words = ['hello', 'world', 'python']
lengths = list(map(len, words))
print(lengths)


# In[10]:


result = round(1234.5678, -2)
print(result)


# In[14]:


original_list = [10,20,30,40,50]
new_list = []
for i in range(3):
    new_list = new_list.append(original_list[i])
print(new_list)


# In[15]:


original_list = [10, 20, 30, 40, 50]
new_list = []
for i in range(3):
    new_list.append(original_list[i])
print(new_list)


# In[23]:


age = int(input("enter your age: "))
if age > 18:
    print("you are an adult.")
else:
    print("you are a minor")
        



# Day 18 Build-In Functions Part 2:
# 
# Format
# The built-in format function in python allows for complex(to hop) variable substitutions(su thay the) and value formatting, enabling(cho phep) the creation of formatted strings with specified(duoc chi dinh) precision(do chinh xac), alignment(can chinh), and type conversions.
# 
# Strip
# the built-in strip function in python removes leading and trailing whitespace or specified characters from a string, making it useful for cleaning and formatting text data.
# 
# Replace
# the built-in replace function in python returns a copy of a string with all occurrences(lan xuat hien) of a specified substring replaced by another substring, useful for modifying and updating text data.
# 
# Join
# the built-in join function in python concatenates a sequence of strings into a single string, with a specified separator between each element making it useful for combining lists of strings in to formatted text

# In[2]:


result = "the numer : {}".format(42)
print(result)


# In[4]:


items = ['apple', 'banana', 'cherry']
result = ", ".join(items)
print(result)


# In[5]:


def is_palindrome(text):
    text = text.strip().lower()
    return text == text.join(reversed(text))
word = "madam"
print(f"is '{word}' a palindrome {is_palindrome(word)}")


# In[6]:


def is_palindrome(text):
    text = text.strip().lower()
    return text == ''.join(reversed(text))

word = "madam"
print(f"is '{word}' a palindrome? {is_palindrome(word)}")


# In[10]:


def is_palindrome(text):
    text = text.strip().lower()
    if len(text) <= 1:
        return True
    result = text[0] == text[-1]
    result = result and is_palindrome(text[1:-1].replace(" ", ""))
    return result

word = "race car"
print(f"is '{word}' a palindrome? {is_palindrome(word)}")


# In[11]:


def process_text(text, old, new, sep):
    text = text.strip(old)
    text = text.replace(new, old)
    return sep.join(text)
my_string = "  ***Hello, world!***  "
result = process_text(my_string, "*", "!", "_")
print(result)


# In[14]:


def process_text(text, old, new, sep):
    text = text.strip(old)        # Remove leading and trailing `old` characters
    text = text.replace(old, new) # Replace `old` characters with `new` characters
    return text                   # Return the modified text

my_string = "  ***Hello, world!***  "
result = process_text(my_string, "*", "!", "")
print(result)


# In[15]:


name ="bob"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)


# In[16]:


word = {
    "fruits": ['apple', 'banana', 'orange'],
    "colors": ['red', 'green', 'blue'],
    "animals": ['dog', 'cat', 'bird']
}

result = "fruits: apple, banana, orange; colors: red, green, blue; animals: dog, cat, bird"


# Day 19 Variable Scope(pham vi)
# 
# In this Python Tutorial, we will be going over variable scope in python. Scope is important because we need to understand it in just about every program we write. It allows us to understand where our variables can be seen from within our program and also what values these variables hold. It also helps with debugging, because scope is a common problem when errors are thrown.
# 
# 

# In[2]:


x = 10
def my_function():
    x=5
    print(x, end=', ')
my_function()
print(x)


# In[3]:


y = 20
def modify_y():
    y+=10
    print(y)
modify_y()


# In[5]:


def outer_function():
    z = 15
    def inner_function():
        print(z)
    inner_function()
outer_function():
    


# In[6]:


def outer_function():
    z = 15
    def inner_function():
        print(z)
    inner_function()

outer_function()


# In[12]:


num=50

def change_num():
    global num
    num=100
    
change_num()
print(num)


# In[17]:


def outer_func():
    var = 25
    
    def inner_func():
        nonlocal var
        var =75
    inner_func()
    print(var)
outer_func()


# In[18]:


def outer_function():
    name = "Alice"
    
    def inner_function():
        print("Hello,", name)
        name = "Bob"
        
    inner_function()
    print("Goodbye,", name)
outer_function()


# In[19]:


def outer_function():
    name = "Alice"
    
    def inner_function():
        nonlocal name
        print("Hello,", name)
        name = "Bob"
        
    inner_function()
    print("Goodbye,", name)

outer_function()


# In[26]:


count = 100
def setup(n):
    count = n
    def increment():
        nonlocal count
        count+=5
        print("Incremented:", count)
    increment()
    return count
def display():
    print("Count:", count)
setup(50)
increment()
display()


# In[25]:


count = 100

def setup(n):
    def increment():
        nonlocal n
        n += 5
        print("Incremented:", n)
    increment()
    return n

def display():
    print("Count:", count)

# Sử dụng giá trị trả về của setup để cập nhật count toàn cục
count = setup(50)
display()


# In[29]:


global_var = "Im gloval"
def my_function(param1):
    local_var = "IM local"
    print(global_var, param1, local_var)
my_function("Argument")


# In[32]:


def outer_function():
    x = 10
    def inner_function():
        x=20
    inner_function()
x=30
outer_function()


# Day 20 - Project 2 - Calculator
# 
# 
# Project #2 is to create a Calculator. Specific points for project 2 are as follows:
# 
# 1 bonus point: Successfully create an input-output for the four basic operations: addition, subtraction, multiplication, and division.
# 
# 2 bonus points: Add the modulo (%) operation.
# 
# 3 bonus points: Allow inputting calculations with 3 or more number pairs, e.g., aa + bb + cc.
# 
# 4 bonus points: Group operations together, e.g., (A+b) x c.
# 
# 5 bonus points: Include all the above bonus requirements and add continuous calculation functionality, e.g., A + B = AB, AB + C = ABC.

# In[ ]:


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, *args):
        self.result = sum(args)
        return "+".join(map(str, args)) + f" = {self.result}"

    def subtract(self, *args):
        self.result = args[0]
        for num in args[1:]:
            self.result -= num
        return "-".join(map(str, args)) + f" = {self.result}"

    def multiply(self, *args):
        self.result = args[0]
        for num in args[1:]:
            self.result *= num
        return "*".join(map(str, args)) + f" = {self.result}"

    def divide(self, *args):
        self.result = args[0]
        for num in args[1:]:
            if num != 0:
                self.result /= num
            else:
                return "Lỗi, không chia được cho 0"
        return "/".join(map(str, args)) + f" = {self.result}"

    def modulo(self, *args):
        self.result = args[0]
        for num in args[1:]:
            self.result %= num
        return "%".join(map(str, args)) + f" = {self.result}"

# Main

if __name__ == "__main__":
    calc = Calculator()
    while True:
        print("Enter 'A' for Addition")
        print("Enter 'S' for Subtraction")
        print("Enter 'M' for Multiplication")
        print("Enter 'D' for Division")
        choice = input("Enter choice (A, S, M, D): ").upper()

        if choice in ['A', 'S', 'M', 'D']:
            try:
                num_inputs = int(input("How many numbers do you want to enter? "))
                numbers = [float(input(f"Enter number {i+1}: ")) for i in range(num_inputs)]

                if choice == 'A':
                    print("Result:", calc.add(*numbers))
                elif choice == 'S':
                    print("Result:", calc.subtract(*numbers))
                elif choice == 'M':
                    print("Result:", calc.multiply(*numbers))
                elif choice == 'D':
                    print("Result:", calc.divide(*numbers))
            except ValueError:
                print("Lỗi: Định dạng đầu vào không hợp lệ")
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")


# Day 21 Working with files - part 1
# 
# Context managers
# context managers provide several benefits, including:
# Automatic resource management: context managers ensure that resources are properly allocated and released, even if exceptions occur within the block
# 
# Readability: The with statement makes the code more readable by clearly indicating the scope of resoutce usage
# 
# Error handling: context managers simplyfy error handling by automatically releasing resources in case of exceptions

# In[1]:


"""
Roses are red,
violets are blue,
python is pun,
and so are you
"""
with open("poem.txt", "r")as f:
    line1 = f.readline()
    line3=f.readline()
    print(line3)


# In[2]:


numbers = [1,2,3,4,5]
with open ("numbers.txt", "w") as f:
    for number in numbers:
        f.write(str(number) + "\n")


# In[1]:


def modify_line(filename, line_number, new_line):
    with open(filename, 'r+') as f:
        f.readline()
    f.write(new_line)
    
filename = 'mydata.txt'
with open(filename, 'w') as f:
    f.write("line 1\nline 2\nline3\n")
modify_line(filename, 2, "modified line\n")
with open(filename, 'r') as f:
    print(f.read())


# In[2]:


import os
import shutil


# In[3]:





# In[5]:





# In[10]:


import shutil

path = r'C:\Users\chuho\Desktop\notebook\diamond.csv'
destination = r'C:\Users\chuho\Desktop\notebook\clean data\diamond_change.csv'

shutil.copy(path, destination)


# In[13]:


def write_data(filename, data, mode='w'):
    with open(filename, mode) as f:
        f.write(data)

# Corrected function calls
write_data('data.txt', 'line1\n')          # Writes 'line1\n' to data.txt (mode 'w' by default)
write_data('data.txt', 'line2\n', mode='a') # Appends 'line2\n' to data.txt (explicit 'a' mode)
write_data('data.txt', 'line3\n')          # Writes 'line3\n' to data.txt (mode 'w' by default)
print(write_data)


# In[14]:


import os
def creatae_folder(folder_name):
    os.mkdir(folder_name)
    
create_folder('myfolder')
create_folder('myfolder/subfolder')


# In[15]:


import shutil
source_file = 'source.txt'
fest_file = 'destination.txt'

shutil.copy(source_file, dest_file)
os.rename(source_file, 'renamed.txt')
shutil.move(dest_file, 'moved.txt')


# In[16]:


import ó

if not os.path.exists('data'):
    os.makedirs('data/backup/logs')
else:
    os.rmdir('data')


# In[17]:


get_ipython().run_line_magic('pinfo', 'code')

def append_data(filename, data):
    with open(filename, 'r+') as f:
        f.seek(o,2)
        f.write(data)
with open('myfile.txt', 'w') as f:
    f.write("initial content\n")
append_data('myfile.txt', "append data\n")
with open('myfile.txt', 'r') as f:
    print(f.read())


# In[18]:


def read_binary(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data
image_data = read_binary('image.jpg')
print(f"image data: {image_data}"")


# Day 23: CSV Module
# 
# In this Python Programming Tutorial, we'll be learning how to parse a CSV file and output the data to an HTML unordered list. This is a real world problem I ran into with my website. The list was becoming too large for me to maintain manually, so writing a Python script to automate this process saved me a lot of time in the future. Let's get started.
# 
# Link: https://www.youtube.com/watch?v=bkpLhQd6YQM
# 
# In this Python Programming Tutorial, we will be learning how to work with csv files using the csv module. We will learn how to read, parse, and write to csv files. CSV stands for "Comma-Separated Values". It is a common format for storing information. Knowing how to read, parse, and write this information to files will open the door to working with a lot of data throughout the world.
# Link: https://www.youtube.com/watch?v=q5uM4VKywbA

# In[2]:


import csv

html_output = ''

name = []

with open('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)
    print(list(csv_data))


# In[11]:


import csv

# Đường dẫn đầy đủ đến file CSV
file_path = 'C:\\Users\\chuho\\Desktop\\notebook\\diamond.csv'

# Mở và đọc file CSV
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    # Mở file mới để ghi
    with open('new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        
        # Duyệt qua từng dòng trong file gốc và ghi vào file mới
        for line in csv_reader:
            csv_writer.writerow(line)


# In[13]:


import csv

# Đường dẫn đầy đủ đến file CSV
file_path = 'C:\\Users\\chuho\\Desktop\\notebook\\diamond.csv'

# Mở và đọc file CSV
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    
    for line in csv_reader:
        print(line)


# In[14]:


import csv

with open('test.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

Assuming test.csv contains:
name, age 
Alice, 30 
Bob, 25


# In[15]:


import csv

with open('test.csv', 'r') as file:
    reader = csv.dictreader(file)
    for row in reader:
        print(row)


# In[16]:


import csv
data = [
    ['name', 'age'].
    ['alice', '30'],
    ['bob', '25']
]
with open('test.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerrows(data)


# In[1]:


import csv
with open('test.csv', 'r') as file:
    reader = csv.reader(file,delimiter = ';')
    for row in reader:
        print(row)


# Day 24 - Project 3 - Automatic File Sorter Project
# 
# 
# Organize files into separate folders.
# 3 file types: 1 bonus point
# 4 file types: 2 bonus points
# 6 file types: 3 bonus points
# 
# Link: https://forms.gle/XFrRGsWVszA3heQw8
# 
# In simpler terms:
# 
# You will earn bonus points based on the number of different file types you can correctly sort into separate folders. The more file types you can handle, the higher your score.
# 
# If you can sort 3 different types of files: You'll earn 1 bonus point.
# If you can sort 4 different types of files: You'll earn 2 bonus points.
# If you can sort 6 different types of files: You'll earn 3 bonus points.
# 
# For example:
# 
# If you can sort images, documents, and videos into separate folders, you'll earn 1 bonus point. However, if you can additionally sort compressed files, audio files, and executable files..etc, you'll earn 3 bonus points.
# 
# Does this explanation clarify the requirements? Let me know if you have any other questions.
# 
# Files examples here: https://drive.google.com/drive/folders/1StlwIEQZH9HQ5_cdTaU3hS1EXchzi0MP?usp=sharing (use file types according to your choice)

# In[2]:


import os
import shutil

# Đường dẫn tới thư mục chứa các tệp
duong_dan_thu_muc = r"C:\Users\chuho\Desktop\35 days challenge\Project\Project 3"

def sap_xep_tap_tin_theo_phan_mo_rong(thu_muc):
    # Đảm bảo thư mục tồn tại
    if not os.path.exists(thu_muc):
        print(f"Thư mục {thu_muc} không tồn tại.")
        return

    # Lấy tất cả các tệp trong thư mục
    tap_tin = [f for f in os.listdir(thu_muc) if os.path.isfile(os.path.join(thu_muc, f))]

    for file in tap_tin:
        # Lấy phần mở rộng của tệp
        phan_mo_rong_tap_tin = os.path.splitext(file)[1][1:]  # [1:] để bỏ qua dấu chấm

        # Nếu tệp không có phần mở rộng, bỏ qua nó
        if not phan_mo_rong_tap_tin:
            continue

        # Tạo một thư mục mới cho phần mở rộng tệp nếu nó chưa tồn tại
        thu_muc_phan_mo_rong = os.path.join(thu_muc, phan_mo_rong_tap_tin)
        if not os.path.exists(thu_muc_phan_mo_rong):
            os.makedirs(thu_muc_phan_mo_rong)

        # Di chuyển tệp vào thư mục mới
        shutil.move(os.path.join(thu_muc, file), os.path.join(thu_muc_phan_mo_rong, file))

    print("Các tệp đã được sắp xếp theo phần mở rộng của chúng.")

# Gọi hàm để sắp xếp các tệp
sap_xep_tap_tin_theo_phan_mo_rong(duong_dan_thu_muc)


# In[5]:


import os
import shutil

#link_folder
link_folder = r"C:\Users\chuho\Desktop\35 days challenge\Project\Project 3"

def sort_file(folder):
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    
    #lấy data type
    for file in files:
        file_extension = os.path.splitext(file)[1][1:]
        
        if not file_extension:
            continue
        
   #Tạo thư mục của data type
    folder_data_type = os.path.join(folder, file_extension)
    if not os.path.exists(folder_data_type):
        os.makedirs(folder_data_type)
        
    #Di chuyển tệp vào folder_data tương ứng
            # Di chuyển tệp vào thư mục mới
    shutil.move(os.path.join(folder, file), os.path.join(file_extension, file))
    
print("Files have been sorted.")


# In[6]:


import os
import shutil

link_folder = r"C:\Users\chuho\Desktop\35 days challenge\Project\Project 3"

def sort_file(folder):
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    
    for file in files:
        file_extension = os.path.splitext(file)[1][1:]
        
        if not file_extension:
            continue
        
        folder_data_type = os.path.join(folder, file_extension)
        if not os.path.exists(folder_data_type):
            os.makedirs(folder_data_type)
        
        shutil.move(os.path.join(folder, file), os.path.join(folder_data_type, file))
    
    print("Files have been sorted.")




# In[ ]:




