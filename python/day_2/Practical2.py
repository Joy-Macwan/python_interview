# Truthy and Falsy values
# In conditions: Falsy: 0, 0.0, None, False, '', [], {}, set().
# Everything else is Truthy
# if []:
#     print("This won’t run")
# if [1, 2]:
#     print("This will run")
# O/P:This will run


#prg1:Predict: if "0": print("Yes") else: print("No")
# if "0":
#     print("Yes")
# else:
#     print("No")
# O/P:Yes
# because:"0" is a non-empty string.
# In Python, any non-empty string is considered truthy, even if it contains "0".


#prg2:Write code: check if number is divisible by 3 and 5
# number = int(input("Enter Number: "))
# if number % 3 == 0 and number % 5 == 0:
#     print("Number is Divisible by 3 and 5")
# else:
#     print("Number is Not Divisible by 3 and 5")

# O/P:Enter Number: 3
# Number is Not Divisible by 3 and 5

#prg3:if 5 > 4 or 3 < 2 and 1 == 1: → True or False?

# if 5 > 4 or 3 < 2 and 1 == 1:
#     print("Condition is True")
# else:
#     print("Condition is False")
# O/P:Condition is True
# because the last Condition is: if 5 > 4 or (3 < 2 and 1 == 1):
# first doing and because and operator is first execute and then or operator.








