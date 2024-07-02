#!/usr/bin/env python
# coding: utf-8

# # Day-9 Python Challenge

# # Tuples in Python

# # Creating a Tuple

# In[1]:


my_tuple = (1,2,4)
print(my_tuple)
print(type(my_tuple))


# # Mixed DataType 

# In[4]:


a = (1, "Apple", 1.2, True)
print(a)
print(type(a))


# # Empty Tuple

# In[3]:


a = () ## Tuble access the empty 
print(a)
print(type(a))


# # Nested Tuple

# In[5]:


a = ("String", [1,2], {1,2}, (1,2)) ## tuple access the all the data types
print(a)
print(type(a))


# # Creating a tuple with only one item

# In[6]:


num1 = ("Appple") ## Tuple access the only one item with their data type
print(num1)
print(type(num1))


# # Tuple Constructor

# In[7]:


a = tuple(("B", "C", "A"))
print(a)
print(type(a))


# # Indexing in Tuple

# In[8]:


a = (1,2,3,5,6,7,8,9,5,3,4)
print(a[4])


# In[9]:


a = (1,2,3,5,6,7,8,9,5,3,4)
print(a[-4])


# # Slicing in Tuple

# In[10]:


a = (12, 14, 15, 3, 56, 76, 87, 80)
print(a[0:3])


# In[11]:


a = (12, 14, 15, 3, 56, 76, 87, 80)
print(a[0:3:2])


# # Reverse the Tuple

# In[15]:


a = (12, 14, 15, 3, 56, 76, 87, 80)
print(a[::-1])


# # Add function in tuple

# In[16]:


a = (1,2,3,4)
b = list(a)
b.append(5)
a = tuple(b)
print(a)


# # Remove function in tuple

# In[17]:


a = (1,2,3,4)
b = list(a)
b.remove(1)
a = tuple(b)
print(a)


# # Loop in tuple

# In[20]:


a = ("B", "C", "A")
for x in a:
    print(a)


# # Join two tuple

# In[21]:


tuple1 = ("A", "B","c")
tuple2 = (1,2,3)
tuple3 = tuple1+tuple2
print(tuple3)


# # Multiply the tuple

# In[22]:


a = ("Apple", "Mango")
b = a*3
print(b)


# In[23]:


t = (1,2,3,4,5,6,7,8)
print(t*2)
print(t+t+t)
print(t+t)
print(len(t))


# # Write a programe to take 5 input from the user and store it in a tuple.

# In[24]:


t = ()
i = 0
while i<=5:
    num = int(input("Enter the values: "))
    t = t+(num,)
    i = i+1
    print(t)

