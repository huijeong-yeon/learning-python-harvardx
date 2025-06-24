amount_due = 50

while amount_due > 0:
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        amount_due -= coin
    if amount_due > 0:
        print(f"Amount Due: {amount_due}")
    else:
        print(f"Change Owed: {abs(amount_due)}")
