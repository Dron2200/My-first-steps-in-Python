
x = None
def math1(a, b, c):
    for x in range(a, b):
        x +=c
        y = 3 * x / (x - 1) - 2 * x / (x + 2)
        print("x =", x, "y =", y)
    for x in range(a, b):
        if x == 1 or x == -2:
            continue
        else:
            y = 3 * x / (x - 1) - 2 * x / (x + 2)
            print("x =", x, "y =", y)
math1(-5, 5, 0.5)