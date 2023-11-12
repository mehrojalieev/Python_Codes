# cost_bread = 3500
# mijoz = int(input("How many bread do you want to buy ? "))
# output = mijoz * cost_bread

# print(output)

# price = 100
# mijoz = int(input("How much do you need ?"))
# result = (price * mijoz)**2
# print(result)


first_customer = int(input(" First: Enter your price ?"))
second_customer = int(input(" Second: Enter your price ?"))

if first_customer > second_customer :
    print("Your profit", first_customer * 2)
elif first_customer < second_customer :
    print("Your profit", second_customer * 3)
else:print("You have to enter number")
