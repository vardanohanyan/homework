# Problem 1

# Create a program to check if a number entered by a user is even or odd.
# Use input() function to save user's input.
num = int(input("enter a number"))

if num % 2 > 0:
  print("this is an odd number")
else:
 print("this is an even number")


# Problem 2

# Create a program to check if the number is divisible by 3.

 num = int(input("enter a number"))
 if num % 3 == 0:
   print("your number is divisible by 3")
 else:
    print("your number is not divisible by 3")


# Problem 3

# Write a program that allows user to enter their grade and tells them which letter they got.

grade = int(input("enter your grade"))

if grade > 95:
    print("you got A")
elif grade >= 85 and grade <= 95:
    print("you got B")
elif grade >= 65 and grade <= 84:
    print("you got C")
elif grade < 65:
    print("you got D")

#Problem 4

#Create a program that takes a number (1-7) from user and returns a day of the week.
#Like 1 for Monday, 2 for Tuesday, etc.

day = int(input("enter number from 1 to 7. "))

if day == 1:
    print("its monday")
elif day == 2:
    print("its tuesday")
elif day == 3:
    print("its wednesday")
elif day == 4:
    print("its thursday")
elif day == 5:
    print("its friday")
elif day == 6:
    print("its saturday")
elif day == 7:
    print("its sunday")
else:
    int(input("enter number from 1 to 7. "))


#Problem 5

#Create a program that tells if a person can get a driving license or no.
#Required age for driving license is 17.

#If they are older than 17, check the score of their test (which can be from 0 to 10).
#If the score is 9 or 10, they get a license, if it is less than 9 they don't get a license.

age = int(input("enter your age"))
score = int(input("enter your score"))

if age >= 17 and score == 9 or score == 10:
    print("you can get a driving license")
else:
    print("you cant get a driving license")


#Problem 6

#Write a program that takes 2 numbers from the user and prints the smaller one.

num1 = int(input("enter your first number"))
num2 = int(input("enter your second number"))

if num1 < num2:
   print(num1)
elif num1 > num2:
   print(num2)
else:
    print("numbers are equal to each other")


#Problem 7

#Create a program to check whether a number is negative or positive or equals to 0.

num = int(input("enter your number"))

if num > 0:
   print("its positive")
elif num < 0:
    print("its negative")
else:
   print("its equal 0")