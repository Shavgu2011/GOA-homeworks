def greet_user():
    name = input("შეიყვანე შენი სახელი: ")
    if name.strip() == "":
        name = "Guest"
    print(f"Hello, {name}!")
    

greet_user()
