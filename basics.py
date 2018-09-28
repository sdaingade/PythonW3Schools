#This is a comment
""" This is a
    multi line comment (also called as docstring)
"""
print("Hello World!")

if 5 > 2:
    print("Five is greater than two")

#Variable declaration
"""
Variables do not need to be declared with any particular type
and can even change type after they have been set.

Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

x = 5
y = "John"

print(x)
print(y)

#To combine both text and a variable, Python uses the + character:

x = "awesome"
print("Python is " + x)

"""
There are three numeric types in Python:

int
float
complex
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#To verify the type of any object in Python, use the type() function
print(type(x))
print(type(y))
print(type(z))

"""
Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

"""
Like many other popular programming languages, strings in Python are arrays of
bytes representing unicode characters. However, Python does not have a character
data type, a single character is simply a string with a length of 1.
Square brackets can be used to access elements of the string.
"""

a = "Hello, World!"
print(a[1])
print(type(a[1]))

#Substring. Get the characters from position 2 to position 5 (not included)
b = "Hello, World!"
print(b[2:5])

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The len() method returns the length of a string:
a = "Hello, World!"
print(len(a))

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

""" The following example asks for the user's name, then, by using the input()
    method, the program prints the name to the screen """
print("Enter your name:")
#username = input() #Does not work in 2.7
#username = raw_input()
#print("Hello, " + username)

"""
Python Arithmetic Operators

Op	Name	        Example
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	 
//	Floor division	x // y

Python Assignment Operators
Op	Example	Same As
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3

Python Comparison Operators
Op	Name	                        Example
==	Equal	                        x == y	
!=	Not equal	                x != y	
>	Greater than	                x > y	
<	Less than	                x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	        x <= y	

Python Logical Operators
Op      Description	                                            Example
and 	Returns True if both statements are true	    x < 5 and  x < 10	
or	Returns True if one of the statements is true	    x < 5 or x < 4	
not	Reverse the result, returns False if the result is true not(x < 5 and x < 10)

Python Identity Operators
Identity operators are used to compare the objects, not if they are equal,
but if they are actually the same object, with the same memory location:

Operator    Description	                                                Example
is 	    Returns true if both variables are the same object	        x is y	
is not	    Returns true if both variables are not the same object	x is not y	

Python Bitwise Operators
Operator	Name	Description
& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""

"""
Python Collections
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable.
Allows duplicate members.

Tuple is a collection which is ordered and unchangeable.
Allows duplicate members.

Set is a collection which is unordered and unindexed.
No duplicate members.

Dictionary is a collection which is unordered, changeable and indexed.
No duplicate members.
"""

"""
List
A list is a collection which is ordered and changeable.
In Python lists are written with square brackets.
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)

#You access the list items by referring to the index number
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#To determine how many items a list have, use the len() method:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To add an item at the specified index, use the insert() method:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#The pop() method removes the specified index,
#(or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
#print(thislist) #this will cause an error because "thislist" no longer exists.

#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
#thislist.clear() #python 3.x ???
print(thislist)

"""
Python has a set of built-in methods that you can use on lists.

Method	        Description
append()	Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	        Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	        Sorts the list
"""

"""
Tuple
A tuple is a collection which is ordered and unchangeable.
In Python tuples are written with round brackets.
"""

thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Access Tuple Items
#You can access tuple items by referring to the index number:

histuple = ("apple", "banana", "cherry")
print(thistuple[1])

#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable.

thistuple = ("apple", "banana", "cherry")
#thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)

#Loop Through a Tuple
#You can loop through the tuple items by using a for loop.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Tuple Length
#To determine how many items a list have, use the len() method:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#Add Items
#Once a tuple is created, you cannot add items to it. Tuples are unchangeable.

#Remove Items
#Note: You cannot remove items in a tuple.
#Tuples are unchangeable, so you cannot remove items from it,
#but you can delete the tuple completely:
#The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

"""
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""

"""

Set
A set is a collection which is unordered and unindexed.
In Python sets are written with curly brackets.
"""

#Create a Set:
#Sets are unordered, so the items will appear in a random order.

thisset = {"apple", "banana", "cherry"}
print(thisset)

#Access Items
#You cannot access items in a set by referring to an index,
#since sets are unordered the items has no index.
#But you can loop through the set items using a for loop,
#or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#Check if "banana" is present in the set:

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Add Items
#To add one item to a set use the add() method.
#To add more than one item to a set use the update() method.

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)

#To determine how many items a set have, use the len() method.
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#Remove Item
#To remove an item in a set, use the remove(), or the discard() method.
#Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Remove "banana" by using the discard() method:
#Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#You can also use the pop(), method to remove an item,
#but this method will remove the last item.
#Remember that sets are unordered, so you will not know what item that gets
#removed. The return value of the pop() method is the removed item.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)

#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

"""
Python has a set of built-in methods that you can use on sets.

Method	Description
add()	Adds an element to the set
clear()	Removes all the elements from the set
copy()	Returns a copy of the set
difference()	Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	Remove the specified item
intersection()	Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	Returns whether two sets have a intersection or not
issubset()	Returns whether another set contains this set or not
issuperset()	Returns whether this set contains another set or not
pop()	Removes the specified element
remove()	Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	Return a set containing the union of sets
update()	Update the set with the union of this set and others

"""

"""
Dictionary
A dictionary is a collection which is unordered, changeable and indexed.
In Python dictionaries are written with curly brackets, and they have keys
and values.
"""

#Create and print a dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#You can access the items of a dictionary by referring to its key name:
x = thisdict["model"]
print(x)

#There is also a method called get() that will give you the same result:
x = thisdict.get("model")

#You can change the value of a specific item by referring to its key name
thisdict["year"] = 2018

#You can loop through a dictionary by using a for loop.
for x in thisdict:
    print(x)

#Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

#You can also use the values() function to return values of a dictionary:
for x in thisdict.values():
    print(x)

#Loop through both keys and values, by using the items() function:
for x, y in thisdict.items():
  print(x, y)

#Print the number of items in the dictionary:
print(len(thisdict))

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#The del keyword removes the item with the specified key name:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#The pop() method removes the item with the specified key name:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The del keyword can also delete the dictionary completely:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict

#The clear() keyword empties the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#It is also possible to use the dict() constructor to make a dictionary:
thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)

"""
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and values
get()	Returns the value of the specified key
items()	Returns a list containing the a tuple for each key value pair
keys()	Returns a list contianing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
print("A") if a > b else print("B")

#One line if else statement, with 3 conditions:
print("A") if a > b else print("=") if a == b else print("B")

#Test if a is greater than b, AND if c is greater than a:
#if a > b and c > a:
#  print("Both conditions are True")

#Test if a is greater than b, OR if a is greater than c:
#if a > b or a > c:
#  print("At least one of the conditions are True")

"""
Python has two primitive loop commands:

while loops
for loops
"""
i = 1
while i < 6:
  print(i)
  i += 1

#With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Continue to the next iteration if i is 3:
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#Loop through the letters in the word "banana":

for x in "banana":
  print(type(x))

#With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

#With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.

#The range() function defaults to 0 as a starting value, however it is possible
#to specify the starting value by adding a parameter: range(2, 6),
#which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
  print(x)

#The range() function defaults to increment the sequence by 1,
#however it is possible to specify the increment value by adding a third
#parameter: range(2, 30, 3):
#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

"""
Functions
"""

#In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")

#Information can be passed to functions as parameter.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#The following example shows how to use a default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

"""
lambda function
A lambda function is a small anonymous function.
A lambda function can take any number of arguments,
but can only have one expression.

lambda arguments : expression
"""

#A lambda function that adds 10 to the number passed in as an argument,
#and print the result:
x = lambda a : a + 10
print(x(5))

#A lambda function that multiplies argument a with argument b and print the result:

x = lambda a, b : a * b
print(x(5, 6))

#The power of lambda is better shown when you use them as an anonymous function
#inside another function.

#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n

#Use that function definition to make a function that always doubles
#the number you send in:
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
