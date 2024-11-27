#functions are like mini -rograms that complete a speific task.

from random import random
from unittest import result


print('Hello World')
name = input('Enter your name:\n')
amount =int(10.6)


#when you define a function you can use it over and over again

#define a function you use 'def' keyword, you need a name, a parameter in the () and the body in the second line.  This is using a local variable
input_name1=input('What is your name?\n')
input_name2=input('What is your name?\n')

def greeting(name):
    print('Hello', name)

greeting(input_name1)
greeting(input_name2)

#this is the same as the code below because the global variable - it can be messy
name = input('What is your name?\n')
def greeting():
    print('Hello', name)
greeting()

#reason to create a function you weant to reuse a chunk of code over and over. you want to organise your code by logical units

def addition(a,b):
    return a+b   #this is a function 

def main():
    num1 = float(input('Enter your 1st number:\n'))
    num2 = float(input('Enter your 2nd number:\n'))

    print(addition(num1, num2)) #or
    result = addition(num1, num2)
    print(result) # you can call the whole second part into a function 

main() #you have to call the function!!!!