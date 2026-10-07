class BankAccount:
    def __init__(self,user,balance=0):
        self.user = user
        self.balance = balance

    def deposit(self,amount,notification_service=None):
        if amount <= 0:
            raise ValueError("must above 1Rs")
        self.balance += amount

        if notification_service:
            notification_service.send(f"Deposited{amount}")

        return self.balance

    def withdraw(self,amount):
        if amount<=0:
            raise ValueError("must above 1Rs")

        if amount > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= amount
        return self.balance
