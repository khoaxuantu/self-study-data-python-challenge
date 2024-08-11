#!/usr/bin/env python
# coding: utf-8

# In[9]:


print('A - Addition')
print('S - Subtraction')
print('M - Multiplication')
print('D - Division')
options = str(input('Choose an operation: '))

if(options in ['A','S','M','D']):
    number_1 = int(input('Enter the first number: '))
    number_2 = int(input('Enter second number: '))
    
    if(options == 'A'):
        result = number_1 + number_2
    elif(options == 'S'):
        result = number_1 - number_2
    elif(options == 'M'):
        result = number_1 * number_2
    else:
        result = number_1 // number_2
else:
    print('Invalid operation entered')
print('The result of the operation is {}'.format(result))


# In[15]:


print('A - Addition')
print('S - Subtraction')
print('M - Multiplication')
print('D - Division')
options = str(input('Choose an operation: '))

if(options in ['A','S','M','D']):
    number_1 = int(input('Enter the first number: '))
    number_2 = int(input('Enter second number: '))
    
    if(options == 'A'):
        result = number_1 + number_2
    elif(options == 'S'):
        result = number_1 - number_2
    elif(options == 'M'):
        result = number_1 * number_2
    else:
        if number_1 % number_2 !=0:
            remainder = number_1 % number_2
            result = number_1 // number_2
            print('The remainder of operation is ' + str(remainder))
        else:
            result = number_1 // number_2
else:
    print('Invalid operation entered')
print('The result of the operation is {}'.format(result))

#You didn't include the MODULO choice in the options so it doesn't count towards your score
#Overall, good job!
# In[ ]:




