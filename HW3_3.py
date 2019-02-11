print("this app show you result of simple function")
x = float(input("Please write x: "))
y = None

from math import cos, pi

if pi >= x >= -pi:
    y = cos(x)
    print("y=", y)
elif x < -pi or x > pi:
    y = x
    print("y=", y)