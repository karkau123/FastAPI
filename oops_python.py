# #CLASS

#1 class Student:
#     college_name = "ABCD"   # class attribute , this is same for everyone in the class
#     name = "Anonymous" # class Attribute
#     def __init__(self):  #Constructor
#           pass
        

#     def __init__(self , name , age):  #Constructor
#             self.name = name   # a new variable name created 
#             self.age = age     # object attribute
            
# # self ---> It refers to the instance of the class itself.
# # Precedence ----->        Object attribute >> Class Attribute 
  
#     def welcome(self):   # self is must Note this point
#         print("Welcome" , self.name)      # above declared vars can be used here => Syntax is slightly diff as comapred to cpp

#     def getmarks(self):
#           print ("Marks" +" " +  str(self.age))

# s1 = Student("ROSHU" , 22)
# print(s1.name)        
# print(s1.name)
# s1.welcome()
# s1.getmarks()
 

# class Student:
#     def __init__(self , name , marks):
#         self.name = name
#         self.marks = marks
         
      


#     def avg(self):
#             sum = 0
#             for val in self.marks:
#                 sum+=val
#             print("hi" , self.name , "your marks is " , sum/3)

            
# first = Student("Roshni" , [12 ,13 ,13 ])
# first.avg()



#3 static methods

# these methods dont use self

# class Student:
#     def __init__(self , name , marks):
#         self.name = name
#         self.marks = marks
         
      

#     @staticmethod   # decorator -> Decorators allow us to wrap another function in order to extend the behaviour 
#     # of the wrapped function , without permannetly modifying
#     def hello():
#         print("Hello World")
           

            
# first = Student("Roshni" , [12 ,13 ,13 ])
# # first.avg()
# first.hello()



# Abstractiom




# Encapsulation



# QUES 2

# class Account:
#     def __init__(self , balance , accno):
#         self.balance = balance
#         self.accno = accno
        
#     def debit(self , amt):
#         self.balance -=amt
#         print("You new balance of" , self.accno , "is " , self.balance)


#     def credit (self , amt):
#         self.balance+=amt
#         print("You new balance of" , self.accno , "is " , self.balance)



# a1 = Account(100 , 1010)
# a1.debit(40)
# a1.credit(30)




# PART 2

# del Keyword


# class Student:
#     def __init__(self , name , marks):
#         self.name = name
#         self.marks = marks
         
      

#     @staticmethod    
#     def hello():
#         print("Hello World")
           

            
# first = Student("Roshni" , [12 ,13 ,13 ])
# del first



#private 

# class Student:
#     def __init__(self , name , marks):
#         self.name = name
#         self.__marks = marks   # use __ (Double underscore) to make private(methoda and var both)
         
      

#     @staticmethod    
#     def hello():
#         print("Hello World")
           


# #inheritence

class Car:
    def __init__(self , type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car Started")
    
    @staticmethod
    def stop():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self , name):       
        self.name = name
        super().type = type   # super
 
# car1 = ToyotaCar("Fortuner")        
# car2 = ToyotaCar("Prius")

# print(car1.start())
 

    # multi level inheritence

class Fortuner(ToyotaCar):
    def __init__(self , type):
        self.type = type 

car1 = Fortuner("Diesel")
car1.start()

    #multiple inheritence

class A:
    varA  = "WELCOME TO CLASS A"
class B:
    varB = "WELCOME TO CLASS B"
class C (A , B):
    varC = "WELCOME TO CLASS C"


c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


#super method
#used tto access the methods of parent class


# class method
    #@staticmethod  -> Common for all members of class

# class Person:
#     name = "anonymous"

#     # def changeName (self , name):
#     #     self.__class__.name = "Roshni kumari"

#     @classmethod
#     def changename (cls ,  name):
#         cls.name = name

# p1 = Person()
# p1.changename("ROSHNI")
# print(p1.name)


# A static method can not acccess or modify class state & general for utility
# Thus for this we use  class methods

#@classmethod

# class Person:
#     name = "anonymous"

#     # def changeName (self , name):
#     #     self.__class__.name = "Roshni kumari"

#     @classmethod
#     def changename (cls ,  name):
#         cls.name = name

# p1 = Person()
# p1.changename("ROSHNI")
# print(p1.name)


######## static methods  -  
######## class methods - cls
######## instance methods - self


# @property - t will reflect the changes as soon as a vaue changes

# class Student:
#     def __init__(self , phy , chem , math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         # self.percentage = str( (self.phy + self.chem + self.math) / 3 ) + "%"
#     @property
#     def percentage(self):
#           return  str( (self.phy + self.chem + self.math) / 3 ) + "%"


# student1 = Student(23 , 24 ,25)
# student1.phy = 43
# print(student1.phy)
# print(student1.percentage)

    # More decorators
    #@getter
    #@setter


#Polymorphism 

    #operatoe overleading
    # when the same operator is allowed to have different meanings according to context
    # + -> for both addition and concatenation

