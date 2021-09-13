#Problem 1

#Write a function that gets a set and an item. It returns the set without the item if it was present in the set.


def s(set,item):
    if item in set:
        set.remove(item)
    print(set)


set = {2, 3, 4}
item  = 3
s(set,item)

#Problem 2

#Write a program that gets two sets. If they have the same items it deletes those items from both sets
#and prints them.

s1 = {'banana', 'orange', 'gazar', 'malina'}
s2 = {'pc', 'xbox', 'ps', 'nintendo', 'gazar'}
s = s2 - s1
ss = s1 - s2
print(ss)
print(s)


#Problem 3

#You have a list of tuples. Remove the tuples that have length 1.

test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
a = 1
remove = [x for x in test_list if len(x) != a]
print(remove)

#Problem 4

#You have two tuples.
#Create tuples of all combinations of those tuple elements and store them in a list.

tuple1 = (1, 5)
tuple2 = (7, 2)
fin = [(x, y) for x in tuple1 for y in tuple2]
fin = fin + [(x, y) for x in tuple2 for y in tuple1]
print(fin)


#Problem 5
#Convert a tuple to a float data type.

tp = (11, 75)
t = float('.'.join(str(x) for x in tp))
print(t)

#Problem 6

#Write a program that will sort tuples by their maximum element.

l1 = [(4, 5, 20, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2)]
l1.sort(key=lambda x: max(x), reverse=True)
print(str(l1))



