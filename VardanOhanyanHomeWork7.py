#Problem 1

#Write a function that will multiply all the list items.
def mul(l):
    n = 1
    for i in l:
        n = n * i
    print(n)


l = [3, 5, 15, 2, 9, 11, 10]
mul(l)


#Problem 2

#write a program that removes duplicates from a list. DO NOT use set().

ll = ['a', 'b', 'ab', 'a', 'c', 'ab', 'd', 'hh', 'k', 'hh']
r = []
for i in ll:
    if i not in r:
        r.append(i)

print(r)

#Problem 3

#Write a program that will find the second smallest number of the list.

ls = [3, 5, 88, -1, 0, -1, 3, -7, -10, 3, 3, -7, 5, -10, 1]
length = len(ls)
ls.sort()
r = []
for i in ls:
    if i not in r:
        r.append(i)

print(r)
print(r[1])

#Problem 4

#Write a program that will add the string 'AAA' before every item of the list.

the_list = ['chrome', 'opera', 'mozilla', 'explorer']
a = "AAA"
new_list = [a + x for x in the_list]
print(new_list)


#Problem 5

#Try to divide a number by 0. Use try, except as a backup.

number = int(input("enter a number"))
try:
    number / 0
except:
    print("you cant divide a number by 0")

#Problem 6

#Make a list and then try to access an index that doesn't exist. Use try and except.

lll = ["xbox," "sidjfiosjd","valera"]
try:
    print(lll[3])
except:
    print("3rd object doesnt exists in list")

#Problem 7 (OPTIONAL)

#1. You have a list of lists. You need to flatten the list. (Make 1 list of all the items in all lists.)
#2. Do the same thing with list comprehension.

import itertools
list_of_list = [['anna', 'bob'], ['john', 'peter'], ['sarah', 'jess', 'ben'], ['ross']]
print(list(itertools.chain.from_iterable(list_of_list)))

#7.2
list_of_list = [['anna', 'bob'], ['john', 'peter'], ['sarah', 'jess', 'ben'], ['ross']]
flatten = []
for i in list_of_list:
    for x in i:
        flatten.append(x)
print(flatten)





