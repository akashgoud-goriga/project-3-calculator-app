print("CALCULATOR")
print("here you can perform simple arithmetic operations")
print("press '1' to add ")
print("press '2' to subtract")
print("press '3' to multiply")
print("press '4' to divide")

def addition(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        if b == 0:
            print("error! can't divide with zero")
            return
    except:
        ValueError
    return a/b



try:
    hum = int(input("enter your choice:- "))
except ValueError:
    print("error! only numbers")
if hum == 1:
    a = int(input("enter the first number :- "))
    b = int(input("enter the second number:- "))
    print(addition(a,b))

elif hum == 2:
    a = int(input("enter the first number :- "))
    b = int(input("enter the second number:- "))
    print(subtract(a,b))

elif hum == 3:
    a = int(input("enter the first number :- "))
    b = int(input("enter the second number:- "))
    print(multiply(a,b))

elif hum == 4:
    a = int(input("enter the first number :- "))
    b = int(input("enter the second number:- "))
    print(divide(a,b))
