"""
Python File Open

The key function for working with files in Python is the open() function.

The open() function takes two parameters; filename, and mode.

There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""

#To open a file for reading it is enough to specify the name of the file:
#Because "r" for read, and "t" for text are the default values, you do not need to specify them.
#Note: Make sure the file exist, or else you will get an error.
f = open("demofile.txt")

#The open() function returns a file object,
#which has a read() method for reading the content of the file:
f = open("demofile.txt", "r")
print(f.read())

#By default the read() method returns the whole text,
#but you can also specify how many character you want to return:
#Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))

#You can return one line by using the readline() method:
#Read one line of the file:
f = open("demofile.txt", "r")
print(f.readline())

#By looping through the lines of the file, you can read the whole file,
#line by line:
#Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)

"""
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content

"""

#Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")

#Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")

"""
Create a New File
To create a new file in Python, use the open() method, with one of the following parameters:

"x" - Create - will create a file, returns an error if the file exist

"a" - Append - will create a file if the specified file does not exist

"w" - Write - will create a file if the specified file does not exist

"""
#Create a file called "myfile.txt":
#f = open("myfile.txt", "x")

#Create a new file if it does not exist:
f = open("myfile.txt", "w")
