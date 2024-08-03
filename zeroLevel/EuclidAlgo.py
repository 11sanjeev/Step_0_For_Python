"""Demonstration of Euclid Algorithm and return highest common divisor."""
'''All function return same value choose any one which you want'''
# def gcd(m,n):
#     if m<n:
#         m,n = n,m
#     if m%n == 0:
#         return(n)
#     else:
#         diff = m-n
#         return(gcd(max(n,diff),min(n,diff)))
def gcd(m,n):
    if m<n:
        m,n = n,m
    if m%n == 0:
        return(n)
    else:
        return(gcd(n,m%n))

# def gcd(m,n):
#     if m<n:
#         m,n = n,m
#     while m%n !=0:
#         diff = m-n
#         m,n = max(n,diff),min(n,diff)
#     return (n)
# def gcd(m,n):
#     if m<n:
#         m,n = n,m
#     while m%n !=0:
#         m,n = n,m%n
#     return (n)
Value1 = int(input("Enter first value:"))
Value2 = int(input("Enter second value"))
print(gcd(Value1,Value2))