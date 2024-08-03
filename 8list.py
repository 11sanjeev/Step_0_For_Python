char = ['a','b','c','d']
print(char)
char[2]= 'e'
print(char)
print(len(char))
char.append('g')
print(char)
char.remove('d')
print(char)
char.pop(3)
print(char)
if 'a' in char:
    print ("True")
else:
    print("False")
char.append("c")
char.sort()
char.reverse()