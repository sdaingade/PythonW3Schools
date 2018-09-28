#To create a class, use the keyword class:
#Create a class named MyClass, with a property named x:

class MyClass():
    x = 5

p1 = MyClass()
print(p1.x)

#Create a class named Person, use the __init__() function to assign values
#for name and age:
#Note: The __init__() function is called automatically every time the class is
#being used to create a new object.
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

#Insert a function that prints a greeting, and execute it on the p1 object:

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

#The self parameter is a reference to the class itself, and is used to access
#variables that belongs to the class. It does not have to be named self ,
#you can call it whatever you like, but it has to be the first parameter of
#any function in the class:

class Person():
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc2(mysillyobject):
        print("Hello, my name is " + mysillyobject.name)

p1 = Person("John", 36)
p2 = Person("Will", 22)
p1.myfunc2()

#You can delete properties on objects by using the del keyword:
del p1.age
print(p2.age)
#print(p1.age) #Gives error

"""
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can
traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator
protocol, which consist of the methods __iter__() and __next__().

Lists, tuples, dictionaries, and sets are all iterable objects.
They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator:
"""

#Return a iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#print(next(myit)) #StopIteration

#Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

"""
Create an Iterator
To create an object/class as an iterator you have to implement the methods
__iter__() and __next__() to your object.

As you have learned in the Python Classes/Objects chapter, all classes have a
function called __init__(), which allows you do some initializing when the
object is being created.

The __iter__() method acts similar, you can do operations (initializing etc.),
but must always return the iterator object itself.

The __next__() method also allows you to do operations, and must return the
next item in the sequence.

"""

class MyNumbers():
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myclass:
    print(x)
    
