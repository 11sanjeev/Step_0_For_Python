#Get factors of given integer
def factors(n):
    factorlist = []
    for i in range(1,n+1):
        if n%i == 0:
            factorlist = factorlist + [i]
    return(factorlist)
#Return given number is prime or nor
def isPrime(n):
    return(factors(n) == [1,n])
#Return list of prime number upto n
def primeUpto(n):
    primelist =[]
    for i in range(1,n+1):
        if isPrime(i):
            primelist = primelist + [i]
    return(primelist)
#Return List of first n prime numbers
def nPrimes(n):
    count,i,plist = 0,1,[]
    while count<n:
        if isPrime(i):
            count,plist = count+1,plist+[i]
        i+=1
    return(plist)
print(factors(19))
print(isPrime(19))
print(primeUpto(19))
print(nPrimes(19)) #Get first 19 prime numbers