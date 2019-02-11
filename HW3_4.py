print("This program is more interesting that previous", '\n',
      "So, using this program you can resolve following formula", '\n',
      "ax^2 + bx + c = 0 ")
a = float(input("Please, write a :"))
b = float(input("Please, write b :"))
c = float(input("Please, write c :"))
d = (b**2 - 4*a*c)
x = -(b/2*a)
x1 = None
x2 = None
if d < 0:
    print("you have no results D<0")
elif d == 0:
    print("You have one result x =", x)
elif d > 0:
    x1 = (-b + d ** 0.5) / 2 * a
    x2 = (-b - d ** 0.5) / 2 * a
    print("x1=", x1, "x2=", x2)