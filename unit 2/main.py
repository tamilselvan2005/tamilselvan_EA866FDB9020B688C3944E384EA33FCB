class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print(f"Deposited ${amount}. New balance: ${self.__account_balance:.2f}")
    else:
      print("Invalid deposit amount. Please enter a positive value.")

  def withdraw(self, amount):
    if amount > 0:
      if amount <= self.__account_balance:
        self.__account_balance -= amount
        print(
            f"Withdrew ${amount}. New balance: ${self.__account_balance:.2f}")
      else:
        print("Insufficient funds.")
    else:
      print("Invalid withdrawal amount. Please enter a positive value.")

  def display_balance(self):
    print(
        f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}"
    )


if __name__ == "__main__":
  account = BankAccount("12345", "John Doe", 1000.0)

  account.display_balance()
  account.deposit(500.0)
  account.withdraw(200.0)
  account.display_balance()
