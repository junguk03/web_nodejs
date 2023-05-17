n = int(input("Enter the number of menus to order: "))
total_price = 0
i = 0
while i < n:
    menu = input()
    if menu == "steak":
        total_price += 24000
        i += 1
    elif menu == "tomato pasta":
        total_price += 8000
        i += 1
    elif menu == "oil pasta":
        total_price += 7500
        i += 1
    elif menu == "risotto":
        total_price += 10000
        i += 1
    else:
        print("Wrong order!")

print("The total price is", total_price)