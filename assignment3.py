#!/usr/bin/env python
# coding: utf-8

# In[23]:


#Write a Python function to sum all the numbers in a list

def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total = total+number
    return total
sum_numbers((8,2,0,3,7))


# In[29]:


#Write a Python program to reverse a string.
s= "1234abcd"
def reverse(s):
    str=""
    for i in s:
        str = i + str
    return str
print("the string is:",end=" ")
print(s)
print("the reverse string is:",end=" ")
print(reverse(s))


# In[32]:


#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
string=input("Enter string:")
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)


# In[ ]:




