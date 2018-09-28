import mymodule

#Now we can use the module we just created, by using the import statement:
mymodule.greeting("Tony")

print(mymodule.person1["name"])

#You can create an alias when you import a module, by using the as keyword:
#Create an alias for mymodule called mx:
import mymodule as mx
print(mx.person1["name"])

#There are several built-in modules in Python, which you can import whenever you like.
#Import and use the platform module:

import platform

x = platform.system()
print(x)

#There is a built-in function to list all the function names (or variable names)
#in a module. The dir() function:
#Note: The dir() function can be used on all modules,
#also the ones you create yourself.

print(dir(platform))
print(platform.processor())

#You can choose to import only parts from a module, by using the from keyword.
from mymodule import person1

print(person1["name"])

#Note: When importing using the from keyword, do not use the module name
#when referring to elements in the module. Example: person1["age"],
#not mymodule.person1["age"]

"""
Python Dates
A date in Python is not a data type of its own, but we can import a module
named datetime to work with dates as date objects.
"""

#Import the datetime module and display the current date:
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)

#To create a date, we can use the datetime() class (constructor) of the
#datetime module. The datetime() class requires three parameters to create
#a date: year, month, day.
#Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)
print(x)

#The datetime() class also takes parameters for time and timezone
#(hour, minute, second, microsecond, tzone), but they are optional, and has
#a default value of 0, (None for timezone).

#The datetime object has a method for formatting date objects into
#readable strings. The method is called strftime(), and takes one parameter,
#format, to specify the format of the returned string:
#Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))

#JSON in Python
#Python has a built-in package called json, which can be use to work with
#JSON data. Import the json module:

import json

#If you have a JSON string, you can parse it by using the json.loads() method.
#The result will be a Python dictionary.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

#Convert from Python to JSON
#If you have a Python object, you can convert it into a JSON string by
#using the json.dumps() method.
#Convert from Python to JSON:

import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

"""
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
Example
Convert Python objects into JSON strings, and print the values:
"""

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

"""
When you convert from Python to JSON, Python objects are converted into the
JSON (JavaScript) equivalent:

Python	JSON
dict	Object
list	Array
tuple	Array
str	String
int	Number
float	Number
True	true
False	false
None	null
"""

#Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

#Use the indent parameter to define the numbers of indents:
json.dumps(x, indent=4)

#Use the separators parameter change the default separator:
json.dumps(x, indent=4, separators=(". ", " = "))

#Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)

"""
What is PIP?
PIP is a package manager for Python packages, or modules if you like.

Note: If you have Python version 3.4 or later, PIP is included by default.

What is a Package?
A package contains all the files you need for a module.

Modules are Python code libraries you can include in your project.

"""
import camelcase

c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

"""
Python Try Except

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the
try- and except blocks.

When an error occurs, or exception as we call it, Python will normally stop
and generate an error message.

These exceptions can be handled using the try statement:
"""
#The try block will generate an exception, because xyz is not defined:

try:
  print(xyz)
except:
  print("An exception occurred")
  
#You can define as many exception blocks as you want, e.g.
#if you want to execute a special block of code for a special kind of error:
#Print one message if the try block raises a NameError and another for other errors:

try:
  print(xyz)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#You can use the else keyword to define a block of code to be executed if no errors were raised:
#In this example, the try block does not generate any error:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
  print(xyz)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
