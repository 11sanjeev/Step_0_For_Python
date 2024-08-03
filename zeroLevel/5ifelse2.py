#demonstrate use of if elif else conditional ladder
team = input("Enter your favorite team ").upper()
if team == "INDIA":
    print("GO Play and Win")
elif team == "NEPAL":
    print("FOCUS on game")
elif team == "AMERICA":
    print("Best of Luck")
else:
    print("good luck!")
sport = input("Enter your favorite sport").upper()
team = input("Enter your favorite team").upper()
if sport == "CRICKET" and team == "INDIA":
    print("NICE")
else:
    print("It's your choice")
month = input("Enter month : ").lower()
favMovie = input("Enter your favorite movie name:")
if month == 'jan' or month == 'feb'\
   or month == 'march' or month == 'april':
    print('You are in first quator')
if favMovie == 'star wars' \
  and favMovie == 'lord of rings'\
  and favMovie == 'comicon':
    print("Let's watch")
monday = True 
freshCoffee = False
if monday:
    if not freshCoffee:
        print("Buy a coffee")
    print("Why it is monday")
