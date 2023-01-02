# Open the file in read mode
with open('file.txt', 'r') as f:
    # Perform some actions with the file
    for line in f:
        print(line)

# The file is automatically closed when the block of code is exited


#=================================
# more detailed:

# Define a context manager class
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        # Open the file and return the file object
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        # Close the file
        self.file.close()

# Use the FileManager context manager to open and close a file
with FileManager('file.txt', 'r') as f:
    # Perform some actions with the file
    for line in f:
        print(line)

# The file is automatically closed when the block of code is exited


#================================== 
# less detailed:

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with FileManager('example.txt', 'w') as f:
    f.write('Hello, world!')
