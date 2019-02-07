print("Homework-2 Task-3")
print("This program is more interesting that previous", '\n',
      "So, using this program you can resolve following formula", '\n',
      "ax^2 + bx + c = 0 ")
a = float(input("Please, write a :"))
b = float(input("Please, write b :"))
c = float(input("Please, write c :"))

x = (-b + (b**2 - 4*a*c)**0.5) / (2*a)

print(x)