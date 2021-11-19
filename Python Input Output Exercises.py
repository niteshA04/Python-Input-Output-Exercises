#!/usr/bin/env python
# coding: utf-8

# # Exercise 1: Accept numbers from a user
# #### Write a program to accept two numbers from the user and calculate multiplication

# In[1]:


num1 = input("Enter the numbers: ")
num2 = input("Enter the numbers: ")

print("The numbers enter by you are:", num1, num2)


# # Exercise 2: Display three string “Name”, “Is”, “James” as “Name** Is** James”

# In[2]:


print("Name", "is", "James", sep='**')


# # Exercise 3: Convert Decimal number to octal using print() output formatting

# In[3]:


num = 10
print("The octol number is: "'%o' % num)


# # Exercise 4: Display float number with 2 decimal places using print()

# In[4]:


n = 458.541315
print(round(n,2))


# # Exercise 5: Accept a list of 5 float numbers as an input from the user

# In[1]:


list_inp = []
n = int(input("Enter the number of elements: "))

for i in range(n):
    ele = float(input("Enter the elements: "))
    list_inp.append(ele)
    
print("Your list is: ", list_inp)


# # Exercise 6 Accept any three string from one input() call

# In[4]:


name, age, height = input("Enter your name age and height: ").split()
print("Name: ", name)
print("Age: ", age)
print("Height: ", height)


# # Exercise 7: Format variables using a string.format() method.

# In[7]:


totalMoney = 1000
quantity = 2
price = 450

join_statement = "I have {0} rupees and I can buy {1} footballs of worth {2} rupees each"
print(join_statement.format(totalMoney, quantity, price))

