#Problem 1

#Create a file manually with some text in it like "My favourite fruits are:".
#Then write a program to append the file with the fruits that you love.

import os
#f = open(r"C:\Users\ASUS\Desktop\problem1.txt", "a")
#f.write("banana, apple, mango, qiwi, orange")
#f.close()


#Problem 2

#Create a file that has 5 or more lines of text.
#Write a program to store each line in a variable

#with open(r"C:\Users\ASUS\Desktop\problem2.txt") as f:
#    line1 = f.readline()
#    line2 = f.readline()
#    line3 = f.readline()
#    line4 = f.readline()
#    line5 = f.readline()


#print(line1, line2, line3, line4, line5)

                                                        #uzeca listovel sarqel

#ls = []
#with open(r"C:\Users\ASUS\Desktop\problem2.txt") as f:
#    for line in f:
#        ls.append(line.rstrip("\n"))

#print(ls)



#Problem 3

#Find the longest word in the file pr3.txt.

#f = open(r"C:\Users\ASUS\Desktop\problem3.txt")
#s = f.read().split()
#print(max(s,key=len))


#Problem 4

#Create a list of names of all our group members.
#Loop over the list and create files (filename = name).
#Each file should contain the name of a person repeated as many times as the characters of the name.

#l = ["Vardan","Abraham","Alik","Ani","Aren","Armen","Ars","Arthur","Mark","Mary"]
#for x in l:
#    f = open(rf"C:\Users\ASUS\Desktop\{x}.txt","x")
#    f.write((x + "\n") * len(x))


#Problem 5

#After writing Problem 4 write a function that gets this list and checks if files with these names exist.
#If a file exists return True, otherwise False.

#new_names = ['Ani', 'Armen', 'Aren', 'Argishti', 'Arsen', 'Alik', 'Anahit', 'Anna']
#for x in new_names:
#    if os.path.exists(rf"C:\Users\ASUS\Desktop\{x}.txt"):
#        new_names = True
#    else:
#        new_names = False


#Problem 6

#Write a function that gets a file path and calculates how many upper case letters are in the text.
#Hint: use isupper() method.

#def count_letter():
#    file = open(r"C:\Users\ASUS\Desktop\problem3.txt")
#    data = file.read()
#    count = 0
#    for letter in data:
#        if letter.isupper():
#            count+=1
#    print(count)
#    file.close()

#count_letter()

#Problem 7 (OPTIONAL)

#Write a program to show the frequency(how many times a word appears in the text) of each word.
#Hint: set()

from collections import Counter

def word_count(fname):
    with open(r"C:\Users\ASUS\Desktop\problem7.txt") as f:
        return Counter(f.read().split())


print("Number of words in the file :", word_count(r"C:\Users\ASUS\Desktop\problem7.txt"))


