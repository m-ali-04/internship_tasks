#Example Tracker
t = 0
def ps():
    global t
    t = t+1
    print(f"\n{'=' * 10} Example {t} {'=' * 10}\n")

#------------------DECORATORS------------------------
#a way to wrap functions or methods to extend their behavior without changing their code
ps()

def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

#my own example

i = 0

def increment(func):
    def wrapper():
        global i
        i+=1
        print(i)
        func()
        i+=2
        print(i)
    return wrapper

@increment
def add_three():
    print(i)

for j in range(4):
    add_three()


#------------------@STATICMETHOD------------------------
# A method inside a class that does not need access to self or cls
ps()

class Utility:
    @staticmethod
    def greet(name):
        print(f"Hello, {name}!")


# You can call it without creating an object:
Utility.greet("Ali")  # Output: Hello, Ali!

# Or with an object, it still works:
u = Utility()
u.greet("Moaz")       # Output: Hello, Moaz!


#my own example 

class Car:
    miles = 0 #this is a class variable and is shared amongst all instances of the class, changes here will reflect in all subsequent instances

    @staticmethod 
    def add_mileage(m):
        Car.miles+=m
        print("Current miles:" + str(Car.miles))

Car.add_mileage(100)

car = Car()
car.add_mileage(50)

#------------------@STATICMETHOD------------------------
#a method that operates on the class itself rather than instances
ps()

#my own example

class Truck:
    miles = 0
    rent = 0

    @classmethod
    def add_mileage(cls, m):
        cls.miles += m #no need to hardcode using class name
        print("Truck mileage: " + str(cls.miles))

    @classmethod
    def set_rent_all(cls, r):
        cls.rent = r
        print("Set rent to: " + str(cls.miles))
    
    def set_rent(self, r):
        self.rent = r
        print("Set rent to: " + str(self.rent))

    def show_rent(self):
        print("Current rent: " + str(self.rent))

truck = Truck()
truck.add_mileage(150)

print()

truck.set_rent_all(50)
another_truck = Truck()

print()

another_truck.show_rent()
another_truck.set_rent(100)
another_truck.show_rent()

print()

another_one = Truck()
another_one.show_rent()
another_one.set_rent_all(25)

print()

truck.show_rent()
another_truck.show_rent()
another_one.show_rent()

# IMPORTANT LEARNING
# A class method will change the value of a class variable for all objects that have been or will be created,
# BUT ONLY IF that variable has not already been overridden at the instance level.
# Once the variable is set or modified directly on an instance (i.e., at the instance level),
# that instance creates its own copy of the variable, which will no longer reflect future changes made by class methods.


#------------------@PROPERTY------------------------
#lets you access a method like an attribute
ps()

#my own example

class Password:
    def __init__(self):
        self._password = input("Create a password: ")
        self.safety_q1 = "What is your pets name?"
        self.safety_q2 = "What is your Date of Birth? (dd/mm/yyyy)"
        self.safety_a1 = input(self.safety_q1)
        self.safety_a2 = input(self.safety_q2)

    @property
    def password(self):
        print("Answer the following Safety Questions to access password.")
        a1 = input(self.safety_q1)
        a2 = input(self.safety_q2)
        if a1 == self.safety_a1 and a2 == self.safety_a2:
            return self._password
        else:
            print("Wrong!")
            return None

    @password.setter
    def password(self, newpass):  # same name as property!
        attempt = input("Enter old password to change it: ")
        if attempt == self._password:
            self._password = newpass
            print("New password set.")
        else:
            print("Wrong password. Cannot change.")

print("Uncomment following lines for demo.")

#p = Password()
#print(p.password)
#p.password = input("Enter New Password:")

#propery lets you access a varaible with modifications made to it 
# which can be as simple as modified values every time you access it 
#or adding layers of security

