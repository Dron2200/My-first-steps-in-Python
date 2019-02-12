def rectangle ():
    a = int(input("Please write first side of the rectangle a = "))
    b = int(input("Please write second side of the rectangle b = "))
    for i in range(a):
        print("!", end="")
        for c in range(b):
            if c == b-1:
                print("!")
            elif i==a//2 and ( b-6 >= c >= 3  ):
                print("_", end="")
            elif i==a//4 and (c==b//2 or c==b//4):
                print("O", end="")
            elif i == 0 or i == a-1:
                print("-", end="")
            else: print(" ", end="")
def factorial():
    n = int(input("Please enter your number n = "))
    c = 1
    for i in range(1, n + 1):
        c *= i
    print(n, c, sep="! = ")
def sum():
    a = int(input("Please enter your number a = "))
    b = int(input("Please enter your number b = "))
    c = 0
    for i in range(a, b+1, 1):
        c += i
    print(c, sep="! = ")
while True:
    print('Home work4:')
    print('1. First task')
    print('2. Second task')
    print('3. Third task')
    print('4. Exit')
    response = input('Выберите пункт: ')

    print()
    if response == '1':
        print("You choose 1 task: you will see rectangle with bonus :)")
        rectangle()
    elif response == '2':
        print("You choose 2 task: you can calculate any factorial :)")
        factorial()
    elif response == '3':
        print("You choose 3 task: you can fin sum between two numbers :)")
        sum()
    elif response == '4':
        break
    else:
        print('Please choose one of the list below: ')
    print()





