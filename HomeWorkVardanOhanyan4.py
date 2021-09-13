#Problem 1
#You have two strings. Put one in the middle of the other one.

s1 = "Environment"
s2 = "Earth"
n = s1[:5] + s2 + s1[5:]
print(n)


#Problem 2

#You have five strings. Create two strings, 1 containing all the beginning letters of the five strings,
#and 1 containing all the ending letter of the 5 strings.

s1 = "qwerty"
s2 = "asdfg"
s3 = "tyu"
s4 = "1234"
s5 = "p"

a1 = s1[0] + s2[0] + s3[0] + s4[0] + s5[0]
a2 = s1[5] + s2[4] + s3[2] + s4[3] + s5[0]
print(a1)
print(a2)


#Problem 3

#Create a function that gets a name. If the length of the name is odd (կենտ) it returns the name all in upper case.
#If the length of the name is even (զույգ) just return it.

def name(n):
    if len(n) % 2 > 0:
        print(n.upper() + " the length of your name is odd")
        return n
    else:
        print(n + " the length of your name is even")
        return n


n = str(input("enter your name"))
name(n)


#Problem 4

#You have a CNN article. You want to find out how many time the words 'university', 'vaccine',
#'student' (but not 'students') appear in the text.
#You also want to find out how many numbers from 1 to 5 can be found in the text.

txt = """ (CNN)The University of Virginia has disenrolled 238 students for its fall semester on Friday for not 
complying with the university's Covid-19 vaccine mandate, according to a university spokesperson.
UVA requires "all students who live, learn, or work in person at the university" to be fully vaccinated 
for the upcoming 2021-2022 academic year, according to current university Covid-19 policies.
Out of the 238 incoming Fall semester students, only 49 of them were actually enrolled in classes, and the remaining 
189 "may not have been planning to return to the university this fall at all," UVA spokesperson Brian Coy told CNN.
"Disenrolled means you're not eligible to take courses," Coy said. 
He added that students who were enrolled at the university on Wednesday still have a week to update their status 
at which point they can re-enroll."""

print(txt.count("university"))
print(txt.count("vaccine"))
print(txt.count("student"))
print(txt.find("1"))
print(txt.find("2"))
print(txt.find("3"))
print(txt.find("4"))
print(txt.find("5"))

#Problem 5

#Find out if there is '2021-2022' string in the article and slice it.

if '2021-2022' in txt:
    print(txt[323:])


#Problem 6

#Create a function that gets a string and returns the same string but the half of it UPPERCASE.
#(It's okay if the string has odd number of characters and half is not the exact half)

def s(phrase):
    a = phrase[:len(phrase) // 2]
    print(a.upper())



phrase = str(input("print something"))
s(phrase)


#Problem 7

#Write a function that takes a name and a (future) profession and returns the sentence
#"I am Ani Amirjanyan and I am a backend developer.".
#Use .format or f" "

def name(n1, n2):
    print(f"I am {n1} and I am a {n2}.")


n1 = input("enter your name")
n2 = input("enter your future profession")
name(n1, n2)


#Problem 8

#Create a function that takes a 3 digit number (can't take more or less digits) and returns the reverse number.
#Example: take "987" return 789. (It is okay if the result starts with 0)

def numbers(n1):
    if int(n1) > 99 and int(n1) < 999:
     print(n1[::-1])
    else:
     print("enter 3 digit number")


n1 = (input("enter 3 digit number"))
numbers(n1)