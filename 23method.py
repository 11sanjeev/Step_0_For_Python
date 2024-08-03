class Empolyee:
    company = 'learn2code'
    def __init__(self,name,age,salary,gender) :
        self.name =name
        self.age = age
        self.salary =salary
        self.gender = gender
        self.email = self.generateEmail(Empolyee)
    def generateEmail(self,cls):
        return f'{self.name}@{cls.company}.com'
    def showInfo(self):
        print(self.name,self.age,self.salary,self.gender,self.email)
    @classmethod
    def changeCompanyName(cls,newName):
        cls.company = newName
    @staticmethod
    def info():
        print('This is a class for method demonstration')
Empolyee.changeCompanyName('learnTOcode')
obj = Empolyee('Shiva',34,'$320000','M')
Empolyee.info()
obj.showInfo()