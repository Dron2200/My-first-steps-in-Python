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



