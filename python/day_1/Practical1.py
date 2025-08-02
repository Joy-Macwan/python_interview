#prg1
# x = 10
# y = "10" 
# print(x + int(y)) #20 because using int() function string convert into Int.


#prg2: Write a program to swap two numbers without using a third variable.
# a = 2
# b = 5
# c = 0
# c = a #c = 2
# a = b #b = 2
# a = c #a = 5
# print(a,b)

#prg 3: Predict output:
# x = True + 5
# print(x)
#X = 6 because "True = 1 " and 1+5 = 6


#prg4: Is this valid? 123abc = 5
#No because variable Start with char, and _


#prg5: Convert string '3.14' to float and print.
# pi = '3.14'
# print(float(pi)) # class float = 3.14


#prg6:Take age input and print if user is adult (>18).
# age = (int(input("Enter Age:")))
# if age >=18:
#     print("User is Adult")
# else:
#     print("User Not Adult") 


#prg7:What will print(bool("")) output?
# print(bool(""))
# False 

# | Value   | bool(Value) | Reason                      |
# | ------- | ----------- | --------------------------- |
# | `""`    | `False`     | Empty string                |
# | `0`     | `False`     | Zero (int)                  |
# | `0.0`   | `False`     | Zero (float)                |
# | `[]`    | `False`     | Empty list                  |
# | `{}`    | `False`     | Empty dictionary            |
# | `None`  | `False`     | Represents null or no value |
# | `set()` | `False`     | Empty set                   |

# print(bool("Hello"))   # True
# print(bool([1, 2, 3])) # True
# print(bool(42))        # True

#prg8: Predict: 
#print(type(3.)) #<class 'float'>
# class float because value has point.


#prg9: Write a program to print your name 5 times.
# for i in range(1,6):
#     print("Joy")

# name = input("Enter Your Name:") #with user Input
# for i in range(0, 5):
#     print(name)


#prg10:Create a variable and print memory id using id()
# a = 10
# print(id(a)) #4463564416 It gives in memory where value is stored


# #prg11:Use input() to take 2 numbers and add them.
# num1 = int(input("Enter First Number:"))
# num2 = int(input("Enter Second Number:"))
# add = num1 + num2
# print(add)


#prg12: Difference in output: print(5) vs print('5')
# print(type(5)) #<class 'int'>
# print(type('5'))#<class 'str'>

#prg13:Predict: 
#print(type(print("Hello")))

# O/P:Hello
#     <class 'NoneType'>

# Step by step:
# step 1:Python first evaluates the inner function:
# means: print("Hello") and its output is Hello

# 🔹 Step 2: What is the return value of print()?
# he print() function in Python:
#     prints to the screen
#     but returns None
# means:result = print("Hello")   # result will be None

#  Step 3: type(None) is <class 'NoneType'>
# So now your outer expression becomes:
# print(type(None))   # This prints: <class 'NoneType'>

#More Example:
# result = print("result")   # result will be None
# print(type(result))
# result
# <class 'NoneType'>


#Prg14:Get user input in int, convert to str, print type.
# num = int(input("Enter Number:"))
# print(type(str(num)))
# O/P:Enter Number:12
# <class 'str'>

#prg15:Write code: get radius, calculate area of circle.
# pi = 3.14
# radius = float(input("Enter Radius:")) //Must use float because pi is in float
# aoc = pi*radius*radius
# print(aoc) 
# O/p:Enter Radius:10
# 314.0


#prg16:Create variable pi and print it with 2 decimal places.
# import math
# print(f"{math.pi:.2f}")
#O/P:3.14
# What does f"{value:.2f}" mean?
#     This is an f-string for formatting.
#     :.2f means:
#     2 decimal places   
# f = fixed-point notation (for float)


#prg17:Predict: a = 5; a = "hello"; print(a)
# a = 5
# a = "hello"
# print(a) #O/P:hello

#prg18:Write a program to take input of 2 numbers and print greater.
# num1 = int(input("Enter First Number:"))
# num2 = int(input("Enter Second Number:"))
# if num1>num2:
#     print(num1," is Greater")
# else:
#     print(num2, " is Greater")
# O/P:Enter First Number:10
# Enter Second Number:15
# 15  is Greater

#prg19:Write a program to check if number is positive or negative.
# number = int(input("Enter Number:"))
# if number > 0:
#     print(number, " is positive")
# elif number < 0:
#     print(number, " is negative")
# else:
#     print(number, " is Zero")

# O/P:Enter Number:-5
# -5  is negative

#Prg20:Take string input and print in uppercase using str.upper()
str = input("Enter String Value: ")
print(str.upper())
# O/P:Enter String Value: Joy Macwan
# JOY MACWAN












