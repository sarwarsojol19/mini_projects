name = input("Please, tell me your name: ")
sales = int(input("Please, input your total month sales: "))

commission= sales * 13 / 100
commission = round(commission, 2)

print(f"Hello {name}, your commissions this month are ${commission}")
