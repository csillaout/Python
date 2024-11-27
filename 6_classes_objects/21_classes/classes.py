#before we create objects we need to define a class and then we can create instanses of that class which also called object

#1 create a class
class Robot_Dog:
    def __init__(self, name_val, breed_val):  #init let us initialise the properties like name, breed .... self is the first parameter  and it refer to the instance of the class we are creating or the current object. the other parameters are the other values of the properties we want to initialise we will have name an bree
        self.name = name_val
        self.breed = breed_val  #we initialise the properties of the new object, self, to the passed in values
    
    def bark(self): #we create a class method just like a function. Except a method has a self as the first parameter
        print('Woof Woof!')

#2 main program
my_dog = Robot_Dog('Spot', 'Chihuaha')

print(my_dog.name)
print(my_dog.breed)

my_dog.bark() #calling the method on our dog(which is the object) method is printed