
# Classes in Python
import random

class Person:
    def __init__(self, firstname, lastname, health, status):
        '''initialize attributes to be used in/available for all
        objects/classes methods in this class and for class
        objectes created by this class'''

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        print("Hello! My name is {} {}".format(self.firstname, self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print("{} is happy today".format(self.firstname))
        elif emotion == 2:
            print("{} is sad today".format(self.lastname))
        else:
            print("{} is neither happy nor sad today".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy".format(self.firstname))
        elif self.health >=75:
            print("{} is not 100% fit today".format(self.firstname))
        elif self.health >= 50:
            print("{} needs to go to the doctor at once".format(self.firstname))
        else:
            print("{} is unconscious".format(self.firstname))

Mary = Person("Mary", "Ray", 95, status=True)
Rey = Person("Rey","Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is {}".format(Mary.firstname, Mary.status))
print("{} is {}".format(Rey.firstname, Rey.status))

Mary.introduce()
Rey.introduce()
Lee.introduce()

Mary.status_change()
Lee.status_change()
Rey.status_change()

# Inheritance: the enemy class inherits from the person class
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status) #coming from the parent class
        self.weapon = weapon

   # Polymorphism -- child introduce method overrides parent introduce method
    def introduce(self):
        print("I am a mortal enemy to all of you")
    # Polymorphism -- child introduce method overrides parent introduce method

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self,other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("{}, I have your stuff".format(other.firstname))
        if other.status == True:
            other.status = False

Alex = Enemy('rock', "Alex", "Wayne", 75, status = False)
Alex.hurt(Mary)
Alex.insult(Rey)
Alex.steal(Lee)
Alex.introduce()

def my_func():
    global v
    v = 'fantastic'
    print("I am " + v)
my_func()
print("She is " + v)