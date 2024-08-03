#with open('data.txt','r') as file:
#    data = file.readlines()
#    print(data)

#userInput = input("Enter your message")
#with open('data.txt','w') as file:
#    file.write(userInput)

userInput = input("Enter message:")
with open('data.txt','a') as file:
    file.write(userInput + '\n')