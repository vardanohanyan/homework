#Problem 1

#Write a function that gets a name and a salary and prints 'Employee named --- earns ---.'
#If no salary is passed to the function, print the default salary which is 100.000.

def n_s(name, salary = 100000):
    print("Employee named " +  name + " earns " + str(salary))


n_s("bob", 87)

#Problem 2

#Create a function that gets 3 numbers then checks if the first number falls between the 2nd and 3rd numbers.

def numbers(num1, num2, num3):
    if num2 < num1 < num3:
        print("first number falls between the 2nd and 3rd numbers")
    elif num2 == num1 == num3:
        print("numbers are equal")
    else:
        print("first number didnt falls between the 2nd and 3rd numbers")


numbers(10, 5, 666)


#Problem 3

#Create a function that gets 3 numbers and returns the biggest of them.
#Hint: You can use a function inside a function.

def biggest(x, y, z):
    if x > y and x > z:
        return x
    elif y > z and y > x:
        return y
    else:
        return z


x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
z = int(input("Enter third number:"))
result = biggest(x, y, z)

print("largest is " + str(result))


#Problem 4

#Write a function that will return the volume (ծավալ) of a cylinder (գլան).
#You can pass the radius and the height to the function.
#Google how to calculate the volume of the cylinder.
#You are going to need sqrt(square root, արմատ) and pi (I show those below)

import math
Pi = math.pi

def volume_cylinder(r, h):
    volume = Pi * r ** 2 * h   #V=πr^2h
    return volume


r = float(input("enter value of radius"))
h = float(input("enter value of height"))
res = volume_cylinder(r, h)
print("volume of cylinder = " + str(res))


#Problem 5 (Calculator)

#Write a function that accepts 3 variables -> number1, number2, operation.
#operation can be +, -, *, /
#The function should return the result of the operation with the two number.

def calculator(num1, num2, operation):
   if operation == "+":
     s = num1 + num2
     return s
   elif operation == "-":
     s = num1 - num2
     return s
   elif operation == "*":
     s = num1 * num2
     return s


num1 = float(input("enter first number"))
num2 = float(input("enter second number"))
operation = str(input("enter operation"))
a = calculator(num1, num2, operation)
print(a)
