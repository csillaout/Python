#inheritance creates a hierarchy of classes that share properties and methods. like parent and children
#base class is the parent class and the derived class is the child class

#1 we create a main/parent class with the common behaviours

class Robot: 
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print('My name is', self.name)

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print('New position :', self.position)
    
    #method overriding
    def eat(self):
        print("I am hungry!")

#2 creating the child class
class Robot_Dog(Robot):
    def make_noise(self):
        print('Woof Woof!')

    def eat(self):
        print('I like bacon!') #method overriding
        super().eat()
    
my_robot_dog = Robot_Dog('Bud')
my_robot_dog.eat()
my_robot_dog.walk(10)
my_robot_dog.make_noise()