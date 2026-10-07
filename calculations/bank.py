def withdraw(balance,amount):
    if amount < 0:
        raise ValueError("amount can't be negative")

    if amount <= balance:
        return balance - amount
    return balance