#we can handle errors and exceptions by defining try and except blocks
try:
    print(10/0)
    text = "Hello"
    number = int(text)
except ZeroDivisionError:
    print("Code for ZDE")
except ValueError:
    print("Code for Value ERROR...")
except:
    print("Other exception")
#else statement runs when we return no errors to handle
else:
    print("other erorrs")
# finnaly is used to run something at the end regardless of exceptions even if they are undhandled
finally:
    print("I always run no matter what")