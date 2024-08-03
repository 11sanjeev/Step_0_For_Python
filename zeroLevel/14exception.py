#Exception Handling and use of sys library for getting error name
import sys
first = float(input("Enter value:"))
second = float(input("Enter values:"))


try:
    result = first/second
    print(result)
except:
    error = sys.exc_info()[0]
    print('something went wrong')
    print(error)
    sys.exit()
finally:
    print("Finally")
print("out")