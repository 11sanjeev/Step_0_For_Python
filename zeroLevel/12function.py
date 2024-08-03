"""Declaration of function using def keyword and its use """
# def main():
#     name = ['Shiva','Parvati','Ram','sita']
#     newName = input("Enter last name:")
#     name.append(newName)
#     printMessage(name)
#     return
# def printMessage(content):   
#     for names in content:
#         print(names)
#     return
# main()
def main():
    names = getName()
    printName(names)
    return
def getName():
    name = ['Shiva','Parvati','Ganesha']
    newName = input("Enter new name: ")
    name.append(newName)
    return name
def printName(name):
    for names in name:
        print(names)

main()
