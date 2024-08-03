# How to write a file using python
fileName = 'guest.txt'
WRITE = 'w'
file = open(fileName,mode=WRITE)
guest = []
while True:
    name = input("Enter guest names if done then enter 'Done':").capitalize()
    if name == "Done":
        break
    guest.append(name)
guest.sort()

for guests in guest:
    file.write(guests +"\n")

file.close()