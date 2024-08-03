class A:
    def __init__(self):
        print('A')
    def method1(self):
        print('method1')
    def method2(self):
        print('method2')
class B:
    def __init__(self):
        print('B')
    def method3(self):
        print('method3')
    def method4(self):
        print('method4')

class C(A,B):
    def __init__(self):
        super().__init__()# first class runs 'A' not "B" because METHOD RESOLUTION ORDER
        print('C')
    def method5(self):
        print('method5')
    def method6(self):
        print('method6')
# a = A()
# b = B()
c = C()
c.method1()
c.method2()
