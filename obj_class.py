class student:
  name="shihab" 

  def __init__(self):
    print("this is constructor")
    
s1=student()
print(s1.name)

s2=student()
print(s2.name)

class Person:

  # A constructor is a special method that is called when an object is instantiated.
  # The __init__() method is used to initialize the object's attributes.

  def __init__(self, name, age): 
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

p2 = Person("Alice", 30)
print(p2.name)
print(p2.age)

p3 = Person("Bob", 25)
print(p3.name,p3.age)

# default constructor

class Car:
  # default constructor
  # def __init__(self):
  #   pass

# parameterized constructor
 def __init__(self, name, model):
    self.name = name
    self.model = model

car1 = Car( "Toyota", "2020")

print(car1.name)
print(car1.model)

# methods

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    # print("Woof!")
    return self.name + " says Woof!"
  



dog1= Dog("Buddy", 3)
print(dog1.name)
print(dog1.age)
print(dog1.bark())

# static method

# not using self,class level method,just after class name we should create static method

class Math:
  @staticmethod
  def add(x, y):
    return x + y
  
result = Math.add(5, 3)
print(result)

# abstraction hiding the internal details and showing only the functionality,hide unnecessary details from the user

class carr:
  def __int__(self):
    self.acc=False
    self.brk=False
    self.steering=False

  def start(self):
    self.acc=True

    self.steering=True
    print("car started")
    
cars=carr()
cars.start()

# encapsulation  ,binding the data and methods that operate on the data within a single unit,wrapping the data and methods into a single unit


class Student:
    def __init__(self, name, age):
        # Private attributes (encapsulation)
        self.name = name
        self.age = age

    # Getter for name
    def get_name(self):
        return self.name

    # Setter for name
    def set_name(self, name):
        self.name = name

    # Getter for age
    def get_age(self):
        return self.age

    # Setter for age
    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print("Age must be positive!")

# Example usage
s1 = Student("Alice", 20)

print(s1.get_name())  # ✅ Access via getter
print(s1.get_age())

s1.set_age(21)  # ✅ Update via setter
print(s1.get_age())

s1.set_age(-5)  # ❌ Invalid update


# del keyword

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person1("John", 36)
print(p1.name)
print(p1.age)
del p1.age
# print(p1.age) # this will raise an AttributeError since age has been deleted
del p1
# print(p1.name) # this will raise an NameError since p1 has been deleted


# private attributes and methods

class Account:
   def __init__(self,acc_no,acc_pass):
      self.acc_no = acc_no          # public attribute
      self.__acc_pass = acc_pass      # private attribute

acc1=Account("123456789", "mypassword")
print(acc1.acc_no)          # Accessing public attribute
# print(acc1.__acc_pass)      # Trying to access private attribute (will raise an AttributeError)



# inheritance

class Car:
   @staticmethod
   def start():
        print("car started")

   @staticmethod
   def stop():
       print("car stopped")

class toyota(Car):  # inheritance
         def __init__(self,name):
            self.name=name
          
car1=toyota("corolla")
print(car1.name)
print(car1.start())

