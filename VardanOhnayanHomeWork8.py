#Problem 1

#Create 3 dictionaries for your favourite top 3 cars. Dict should contain information like brand, model, year, and color.
#Add all those dicts in one dict and print items.

# meqenanerov hetaqrqrvac chem, nuyn bany kanem uxaki guitarnerov

d = {"d1": {"brand": "Gibson", "model": "Flying V", "year": "1970",},
     "d2": {"brand": "Fender", "model": "Fender Yngwie Malmsteen Stratocaster", "color": "vintage white"},
     "d3": {"brand": "B.C. Rich", "model": "Mockinbird", "year": "1982"}
     }
print(d)

#Problem 2

#You have a list of lists. Each list in the list contains a key and a value. Transform it into a list of dictionaries.
#Use loops.

ls = [['Bob', 45,], ['Anna', 4], ['Luiza', 24], ['Martin', 14]]
d = {x[0]: x[1:] for x in ls}
print(d)

#Problem 3

#Check if value 1000 exists in the dict values. If yes delete all other items except that one.

dt = {'hundred': 100, 'million': 1000000, 'thousand': 1000, 'ten': 10}
if 1000 in dt.values():
    [dt.pop(k) for k in list(dt.keys()) if k != "thousand"]
print(dt)


#Problem 4

#Change Narine's salary to 10000

sampleDict = {
     'employee1': {'name': 'Marine', 'salary': 7500},
     'employee2': {'name': 'Karine', 'salary': 8000},
     'employee3': {'name': 'Narine', 'salary': 6500}
}
sampleDict['salary'] = 10000
print(sampleDict)


#Problem 5

#Write a function that will get a dict of employees and their salaries. It will return a new dict with
#the same keys (employees) and all values will be the average of their salaries.

def d(dict1):
     a = 0
     for i in dict1:
          a = (a + (dict1[i])) / len(dict1.values())
     d = {'ann': a, 'bob': a, 'lily': a, 'molly': a, 'some_intern': a}
     print(d)



dict1 = {'ann': 3000, 'bob': 4000, 'lily': 5000, 'molly': 5500, 'some_intern': 500}
d(dict1)








