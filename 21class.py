# class Employee:
#     def showEmployeeData(self):
#         print('Shiva','23','34000')

# obj=Employee()
# obj.showEmployeeData()/

# class Empolyee:
#     def __init__(self) :
#         print('new object created')

# obj1= Empolyee()

class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail()
    def generateEmail(self):
        return f'{self.name}@company.com'
    def showInfo(self):
        print(self.name,self.age,self.salary,self.gender,self.email)
        
obj = Employee('John',20,'$3400','M')
obj.showInfo()


