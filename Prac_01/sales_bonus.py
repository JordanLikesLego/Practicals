try:
    sales = float(input("Enter sales: $"))
    bonus = 0
    while sales > 0:
        if sales >= 1000:
            bonus = 1.15
            total = sales * 1.15
            print("Total = $", total)
            sales = float(input("Enter sales: $"))
        else:
            bonus = 1.10
            total = sales * 1.10
            print("Total = $", total)
            sales = float(input("Enter sales: $"))
except ValueError:
    sales = float(input("Please enter valid number: $"))

