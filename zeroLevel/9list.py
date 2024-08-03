# Basic of list in python
guest =  ["Ram","Shiva","Ganesh","Nandi"]
# #update a value
# guest.append("Parvati")
# print(guest[-1])
# #add a value
# guest[4] = 'Gora'
# print(guest[-1])
# #remove a value
# guest.remove("Nandi")
# del guest[0]
# print(guest)

nbr = len(guest)
for steps in range(nbr):
    print((guest[steps]))
guest.sort()
for guests in guest:
    print(guests)
length = len(guest)
for i in range(length):
    for j in range(length-i-1):
        if guest[j]>guest[j+1]:
            guest[j],guest[j+1]= guest[j+1],guest[j]
print(guest)
