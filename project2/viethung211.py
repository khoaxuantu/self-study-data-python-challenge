#!/usr/bin/env python
# coding: utf-8

# In[41]:


def calculation():
    print("""
    Enter 'A' for Addition. \n 
    Enter 'S' for Subtraction. \n 
    Enter 'M' for Multiplication. \n 
    Enter 'D' for Division. \n
    Enter 'M' for Modulo. \n""")
    e = "    Result: "
    d = input(
        '\n Enter Choice (A,S,M,D): ')
    x = int(input(
        '\n Enter first number: '))
    y = int(input(
        '\n Enter second number: '))
    if d == 'A':
        return e + str(x + y)
    elif d == 'S':
        return e + str(x - y)
    elif d == 'M':
        return e + str(x * y)
    elif d == 'D':
        return e + str(x/y)
    elif d == 'M':
        return e + str(x%y)
    else:
        print("\n Error. Enter your choice again")


# In[42]:


calculation()


# In[ ]:





# In[ ]:




