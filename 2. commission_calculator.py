# Taking name & convert it to title case

name = input("Please, tell me your name: ")

name = name.title()

# Taking sales input from user

sales = int(input("Please, input your total month sales: "))
com_rate = int(input("Please, input your commision rate: "))

# Calculating commision 

commission= sales * com_rate / 100
commission = round(commission, 2)

# Showing the result

print(f"Hello {name}, your commissions this month are ${commission}")
