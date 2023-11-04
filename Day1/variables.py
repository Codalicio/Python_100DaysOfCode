# Variables :

name = input("What is your name?\n") 
print(name)

firstName = "Amit"
print(firstName)

firstName = "Angela"
print(firstName)

# print(len(input("What is your name?\n"))) :
name = input("What is your name?\n")
length = len(name)
print(length)

# Interactive Coding Exercise - variables :
# Method - 1 :
a = input()
b = input()
a,b = b, a
print("a: " + a)
print("b: " + b)

# Method - 2 :
a = input()
b = input()
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)

# Variables naming :

# The no.1 priority of naming variables is to make code readable.
# The name of the variable has to be one single unit.

user_name = input("Enter your name :\n")
length_of_username = len(user_name)
print(length_of_username)


