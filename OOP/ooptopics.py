# class Car:
#     #  brand =None
#     #  model = None

#     def __init__ (self, brand,model):
#         self.__brand = brand
#         self.model=model

#     def chai_brand(self):
#          return self.__brand 

#     def full_name(self):
#         return f"{self.__brand} {self.model}"
# ### Inherititace    
# class ElectricCar(Car):
#       def __init__ (self,brand,model,battery_size):
#            super().__init__(brand,model)
#            self.battery_size = battery_size

# my_tesla = ElectricCar("Tesla","Model S", "85 Kwh")
# print(my_tesla.__brand)
# print(my_tesla.full_name())
# print(my_tesla.chai_brand())



# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Tata","Safari")

# print(my_new_car.model)
# print(my_car.full_name())

# Encapsulation

#Exmaple 1
# class Person:
#     def __init__(self,name,age):
#         self.name= name
#         self.age=age


# p= Person("Alice",21)
# print(p.name)


# Protected member variable 
# class Vechile:
#     def __init__(self,brand,speed):
#         self._brand=brand
#         self._speed=speed

# class Car(Vechile):
#     def show_details(self):
#         print(f"Brand:{self._brand},Speed:{self._speed} km/h")

# car = Car("BMW",40)
# car.show_details()

##############Private Member variable########################

# class BankAccount:
#     def __init__(self,balance):
#         self.__balance= balance
    
#     def deposit(self,amount):
#         self.__balance+=amount
#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance())

#### Getter and Setter

# class Student:
#     def __init__(self,name,grade):
#         self.__name=name
#         self.__grade =grade

#     def get_grade(self):
#         return self.__grade
#     def set_grade(self,grade):
#         if 0<=grade<=100:
#             self.__grade=grade
#         else:
#             print("Invalid Grade")

# s1= Student("Alice",85)
# print(s1.get_grade())

# s1.set_grade(95)
# print(s1.get_grade())

# class Employee:
#     def __init__(self, name, salary):
#         self.__name = name
#         self.__salary = salary
    
#     @property
#     def salary(self):
#         return self.__salary
    
#     @salary.setter
#     def salary(self, value):
#         if value >= 0:
#             self.__salary = value
#         else:
#             print("Salary cannot be negative")

# emp = Employee("Bob", 5000)
# print(emp.salary)   # Acts like an attribute
# emp.salary = 6000   # Uses setter
# print(emp.salary)

### A banking system

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.__balance= balance
#     def deposit(self,amount):
#         if amount>0:
#          self.__balance += amount
#         else:
#            print("Invalid Deposit")
    
#     def withdraw(self,amount):
#        if 0<amount <= self.__balance:
#           self.__balance -= amount
#        else:
#           print("Insufficient Balance")
#     def get_balance(self):
#        return self.__balance

# account = BankAccount("Subash",2000)
# account.deposit(500)
# account.withdraw(200)
# print(account.get_balance())


########## ABSTRACTION #########################
# from abc import ABC, abstractmethod

# # Abstract class
# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

# # Concrete subclasses
# class CreditCardPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card")

# class PayPalPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using PayPal")


# # ✅ Usage (Polymorphism)
# payments = [CreditCardPayment(), PayPalPayment()]
# for p in payments:
#     p.pay(100)    # Each class implements pay() differently




## OOP Interview / LeetCode-Style Questions (Python)



# class BankAccount:
#     def __init__(self,balance):
#         self.__balance= balance
#     def deposit(self,amount):
#         self.__balance+=amount
    
#     def withdraw(self,amount):
#         self.__balance = self.__balance-amount

#     def get_balance(self):
#         return self.__balance

# #usage
# account =BankAccount(1000)
# account.deposit(500)
# account.withdraw(200)
# print(account.get_balance())

# from abc import ABC, abstractmethod
# class Shape(ABC):
#      @abstractmethod
#      def area(self):
#           pass
# class Circle(Shape):
#      def __init__(self,r):
#           self.r=r
#      def area(self):
#       return 3.14 * self.r* self.r
# class Square(Shape):
#      def __init__(self,length,height):
#           self.length=length
#           self.height =height
#      def area(self):
#       return self.length*self.height
# shape = [Circle(5),Square(4,5)]
# for s in shape:
#     print(s.area())
     
'''Q6. Employee Payroll System

Create an abstract class Employee with attributes name and salary.

Abstract method: calculate_bonus().

Subclasses:

Manager → Bonus = 20% of salary.

Developer → Bonus = 10% of salary.

Make salary a private variable (encapsulation).

Use a getter to access salary.
'''

# from abc import ABC,abstractmethod

# class Employee(ABC):
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#     def get_salary(self):
#         return self.__salary
     
#     @abstractmethod
#     def calculate_bonus(self):
#         pass
    
# class Manager(Employee):
#     def calculate_bonus(self):
#         # 20% bonus for Manager
#         return self.get_salary() * 0.2
 
# class Developer(Employee):
#     def calculate_bonus(self):
#         # 10% bonus for Developer
#         return self.get_salary() * 0.1


          
# employees = [Manager("Alice", 5000), Developer("Bob", 4000)]

# for e in employees:
#     print(e.name, e.calculate_bonus())


'''
Problem Restatement

Create a class Book with private attributes title and author.

Add a method get_details() to show book info.

Create a subclass EBook with an extra attribute file_size.

Override get_details() to include file size.'''

# class Book():
#     def __init__(self,title,author):
#         self.__title = title
#         self.__author =author
          
#     def get_details(self):
#         return f"Tile:{self.__title},Author :{self.__author}"
# class Ebook(Book):
#     def __init__(self,title,author,filesize):
#         super().__init__(title,author)
#         self.filesize = filesize
#     def get_details(self):
#         return f"{super().get_details()}, File Size: {self.filesize}"

  
    
# b = Book("1984","George Orwell")
# e= Ebook("Python101","subash","5 MB")
# print(b.get_details())  
# print(e.get_details())'

'''
You defined a base class Animal (though it doesn’t do much here).

Each subclass (Dog, Cat, Cow) overrides the speak() method.

When you loop through animals, Python calls the correct version of speak() depending on the object type.'''

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def speak(self):
#         pass
    
# class Dog(Animal):
#     def speak(self):
#         return "Bark"
 
# class Cat(Animal):
#     def speak(self):
#         return "Meow"

# class Cow(Animal):
#     def speak(self):
#         return "Moo"
# animals =[Dog(),Cat(),Cow()]

# for a in animals:
#     print(a.speak())
