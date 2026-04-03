class BankAccount:
    def __init__(self, acc_num, holder, initial_balance):
       
        self.__account_number = acc_num
        self.__account_holder = holder
        # Initial validation
        if initial_balance < 0:
            print("Warning: Initial balance cannot be negative. Setting to 0.")
            self.__balance = 0
        else:
            self.__balance = initial_balance

    @property
    def account_number(self):
       
        return self.__account_number

    @property
    def balance(self):
       
        return self.__balance

    @balance.setter
    def balance(self, value):
        
        if value < 0:
            print("Error: Balance cannot be negative.")
        else:
            self.__balance = value

    def deposit(self, amount):
      
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
        else:
            self.__balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
       
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print(f"Error: Insufficient funds. Current balance: ${self.__balance}")
        else:
            self.__balance -= amount
            print(f"Successfully withdrew ${amount}. Remaining balance: ${self.__balance}")

    def display_account_info(self):
       
        print("-" * 30)
        print("BANK ACCOUNT DETAILS")
        print(f"Holder: {self.__account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")
        print("-" * 30)

# Example
if __name__ == "__main__":
    # Create an account
    my_acc = BankAccount("123456789", "Jayden Christopher", 1000)

    #  initial info
    my_acc.display_account_info()

    # Deposit
    my_acc.deposit(500)
    my_acc.deposit(-50) # Should show error

    # Withdrawal
    my_acc.withdraw(200)
    my_acc.withdraw(2000) # Should show error

   
    my_acc.display_account_info()
