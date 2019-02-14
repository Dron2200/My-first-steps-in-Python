print("Welcome to the Dron's calculator")
print("This calculator have simple function +, -, *, /")


def add():
    c  = a+b
    print ("Your result is:", c)
def subs():
    c = a - b
    print ("Your result is:", c)
def mult():
    c = a * b
    print ("Your result is:", c)
def divis():
    if b == 0:
        print("It's impossible to divide by 0")
    else:
        c = a / b
        print("Your result is:", c)

while True:
    a = float(input("Please write your first number: "))
    z = input("What function you are going to choose: ")
    b = float(input("Please write your second number: "))

    if z == "+":
        add()
    elif z == "-":
        subs()
    elif z == "/":
        divis()
    elif z == "*":
        mult()
    elif z not in("-","+","/","*"):
        print("error, write correct function")
    print()

    ans = input("Do you want to continue: ")
    if ans in("no", "No", "NO"):
        break