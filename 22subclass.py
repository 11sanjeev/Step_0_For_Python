class Employee:
    company = 'learn2code'
    def __init__(self,name,age,salary,gender,desig,dept,responsibility,cpu,gpu,ram):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail(Employee)
        self.job = self.Job(desig,dept,responsibility)
        self.computer = self.Computer(cpu,gpu,ram)
        
    def generateEmail(self,cls):
        return f'{self.name}@{cls.company}.com'
    def showInfo (self):
        print(self.name,self.age,self.salary,self.gender,self.email)
    class Job:
        def __init__(self,designation,department,responsibility):
            self.designation = designation
            self.department=department
            self.responsibility = responsibility

        def showInfo(self):
            print(self.designation,self.department,self.responsibility)
    class Computer:
        def __init__(self,cpu,gpu,ram):
            self.cpu = cpu
            self.gpu = gpu
            self.ram = ram

        def showInfo(self):
            print(self.cpu,self.gpu,self.ram)
            

obj = Employee('Shiva',43,'$430000','M',"Manager",'IT','Servers','i7','gtx1060','32')
obj.showInfo()
obj.job.showInfo()
obj.computer.showInfo()
    