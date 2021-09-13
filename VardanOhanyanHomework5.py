#Problem 1

#You have a list, you want to iterate over it and return the numbers that are divisible by 5.
#If you iterate over a number larger than 500, stop the loop.

ls = [5, 11, 30, 45, 175, 99, 106, 300, 490, 512, 890, 1000]

for x in ls:
    if x < 500:
        if x % 5 == 0:
            print(x)


#Problem 2

#reate a loop to print the reverse of a list.

list1 = [1, 2, 3, 4, 5]
for x in reversed(list1):
    print(x)
                              #2 dzevov vorosheci pordzel
#for x in list1[:: -1]:
#    print(x)


#Problem 3

#Write a function to get a number and return the factorial of the number. Use loops.
#ex. factorial of 5 is 1*2*3*4*5
#You can't count factorial of negative numbers, and the factorial of 0 is 1.

def fact(n):
    factorial = 1
    if n < 0:
        print("factorial does not exist for negative numbers")
    elif n == 0:
        print("factorial of 0 is 1")
    else:
        for x in range(1, n + 1):
            factorial = factorial * x
        print(factorial)


n = int(input("enter your number"))
fact(n)

#Problem 4

#Write a code that would print list items that are at even positions.
#ex. in list = [10, 11, 12], 10 is at index 0, 11 - index 1 (odd), 12 - index 2 (even)
#Use loops.

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
for x in lst:
    if x % 2 > 0 and x > 1:                              #0-n chem yndunel vorpes even
     print(x)

#Problem 5

#Write a function that gets a list of names and returns the ones that start with A.
#Notice that some list items begin and end with spaces, or start with @. Get rid of space and @ before printing the name.


def n(names):
    matches = []
    for match in names:
        if "A" in match:
            matches.append(match.strip(" ""@"))

    print(matches)

names = [' Anna', "Lily", " Anahit ", "@Bob", "@Ani@", " Luiza@", "@@Armen"]
n(names)


#Problem 6

#Write a program that checks if a number is prime (պարզ) or not. Try not to google. :)

x = int(input("enter your number"))
for i in range(2, x):
    if x % i == 0:
        print('its a non prime number')
        break
else:
    print('its a prime number')