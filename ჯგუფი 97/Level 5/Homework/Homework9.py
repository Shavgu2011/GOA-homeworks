age = int(input("how old are you: "))
balance = float(input("What's your balance: "))
VIP = input("VIP status True/False: ")

print(age >= 18 and balance >= 100 or VIP == "True")
