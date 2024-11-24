'''
Create a program that reads a file and writes a modified version to a new file.  
Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
'''

# Create a new file
with open("tell_me_something.txt", 'w') as file:
    line = "Welcome to file handling with Python"
    file.write(line)

# Take the contents and modify them to a new file
with open("tell_me_something.txt", 'r') as file_read_only:
    entireFileContents = file_read_only.read()

# Change the text to uppercase
fileInfoModifications = entireFileContents.upper()

# New file
with open("uppertext.txt", 'w') as file_write:
    file_write.write(fileInfoModifications)

try:
    fileName = input("Enter an existing file name to view its contents: ")
    
    namedFile = open(fileName, 'r')

    fileContents = namedFile.read()

    print(fileContents)

except FileNotFoundError:
    print("Error: File does not exist.")
except OSError:
    print("Unable to read file.")