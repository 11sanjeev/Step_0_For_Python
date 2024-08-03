#def myfunction(string = 'no parameter default'):
#    for char in string:
#        print(char)
#myfunction('HELLO')
#x = 20
#def fun():
#    global x
#    x =23
#fun()
#print(x)
#def reverse(string):
#    return(string[::-1])
#rev=reverse("Hello")
#print(rev)
def iterativefact(n):
    result = 1
    for i in range(n,0,-1):
        result = result*i
    return result
print(iterativefact(5))
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))