#Modules

# -> script.py
def greeting():
    print('Hello')

#--------------------------

#os module:
import os

print(os.listdir())
#os.mkdir('Test')
print(os.listdir())

os.rmdir('Test')
print(os.listdir())

#--------------------------

# subprocess module:
import subprocess

print(subprocess.run(['ls']))

#subprocess.run(['git', 'clone', 'githubwebadressetilcloning'])

