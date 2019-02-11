print("This app check and compare your name with mine ")
username = input("please write your name in English(remember that name must start with capital letter): ")

if username in("Andrey", "Andriy", "Andrew"):
    print("you have the same name as I have ")
elif username is "":
    print("Please, write your name correctly. You didn't write anything")
else: print("your name is: ", username, "and you must be happy that we have different names")
