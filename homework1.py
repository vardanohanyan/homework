#Problem 1.

#Give examples of integer, string and float values.
#Then use type() function to prove it.

number = 6  #integer
text = "you have 6 missed calls"  #string
height = 1.76  #float

print(type(number)) #integer
print(type(text))  #string
print(type(height))  #float


#Problem 2.

#Create variables movie1 and movie2, assign your 2 favourite movies to those variables.
#Put the variables in the text "My 2 favourite movies are ____, ____." and print it.

movie1 = "Evil Dead"
movie2 = "Scary Movie"

print("My 2 favorite movies are " + movie1 + ", " + movie2 + ".")


#Problem 3.

#Calculate your age using the value of the year you were born and the value of current year.

current_year = 2021
year_i_was_born = 2004
my_age = current_year - year_i_was_born
print("I am " + str(my_age) + " years old.")

#Problem 4.

#What is wrong with this variable name? Correct it.

#2my-first_name = "Poghos"  sa eror kta qani vor popoxakanin anun taluc chenq karox dimac tiv dnel ev chenq karox ogtagorcel "-" nshany


#Problem 5.

#Petros is 20 years old.
#Print "Petros is younger than me." if his age is smaller than yours.
#Print "Petros is older than me." if his age is greater than yours.
#Print "Petros is my age" if his age equals yours.

petros_age = 20

if petros_age > 17:
    print("Petros is older than me")


#Problem 6.

#Create a string variable.
#Transform it into integer.

var = "66"
print(str(var))