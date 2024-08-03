# It is a basic program for  calculating monthly payment for loan
loanAmount = float(input("Enter your loan amount "))
l = loanAmount
i = 0.05
n = float(input("Enter number of payments "))
monthPayments = l*(i*(1+i)*n)/((1+i)*n-1)
print("Monthly payment is %f " % monthPayments)