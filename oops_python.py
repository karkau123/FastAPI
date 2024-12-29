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

class Student:
    def __init__(self , name , marks):
        self.name = name
        self.marks = marks
         
      

    @staticmethod   # decorator -> Decorators allow us to wrap another function in order to extend the behaviour 
    # of the wrapped function , without permannetly modifying
    def hello():
        print("Hello World")
           

            
first = Student("Roshni" , [12 ,13 ,13 ])
# first.avg()
first.hello()



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
