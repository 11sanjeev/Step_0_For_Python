#It is a normal calculation for demonstration of if - else conditional statements
deposit = int(input ("deposit your money "))
freetoster = False
if deposit > 100:
    freetoster = True
if freetoster:
   print("enjoy tostar")  
else:
    print("Enjoy your free coffee ")
print("have a nice day")
userInput = int(input("Enter total amount of your purchase :"))
if userInput < 50:
    ShippingAmount = userInput + 10
    print("Your total shipping charges is :$%d"%ShippingAmount)
else:
    print("your total amount is :$%d"%userInput)