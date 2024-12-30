class Student:
    def __init__(self , phy , chem , math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str( (self.phy + self.chem + self.math) / 3 ) + "%"
        @property
        def percentage(self):
          return  str( (self.phy + self.chem + self.math) / 3 ) + "%"


student1 = Student(23 , 24 ,25)
student1.phy = 43
print(student1.phy)
print(student1.percentage)
