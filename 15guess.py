import random as rn
randomnumber = rn.randint(1,20)
score =10
while True:
    userNumberInput = int(input("Guess:"))
    
    if userNumberInput == randomnumber:
        print("correct guess:"+str(score))
        break
    else:
        print('Better luck next time')
        score -= 1