#errors 1.compiling errors 2.logical errors 3. run time errors
try:
    print('opened')
    a = int(input("~ "))
#except Exception as error:
#    print("User error: " + str(error))
except ValueError:
    print('invalid value')
except TypeError:
    print('type error')
except KeyboardInterrupt:
    print("Keyboard Interrupt")
finally:
    print('closed')