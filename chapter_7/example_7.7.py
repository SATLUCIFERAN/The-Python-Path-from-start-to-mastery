
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

status = withdraw(5000, 1000)
print(status)  # 4000

status = withdraw(500, 1000)
print(status)  # Raises ValueError: Insufficient funds