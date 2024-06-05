class ATM:
    def __init__(self):
        self.balance = 15000  # Default balance
        self.pin = "5454"  # Predefined PIN for the sample application
        self.is_authenticated = False

    def enter_pin(self, entered_pin):
        if entered_pin == self.pin:
            self.is_authenticated = True
            print("PIN entered correctly.")
        else:
            self.is_authenticated = False
            print("Incorrect PIN. Please try again.")

    def check_balance(self):
        if self.is_authenticated:
            print(f"Your current balance is: Rs. {self.balance}")
        else:
            print("Please enter the correct PIN first.")

    def withdraw(self, amount):
        if self.is_authenticated:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Rs. {amount} withdrawn successfully. New balance: Rs. {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Please enter the correct PIN first.")

    def deposit(self, amount):
        if self.is_authenticated:
            self.balance += amount
            print(f"Rs. {amount} deposited successfully. New balance: Rs. {self.balance}")
        else:
            print("Please enter the correct PIN first.")

    def exit_atm(self):
        print("Exiting. Thank you for using the ATM.")
        self.is_authenticated = False  # Log out the user


def main():
    atm = ATM()

    while True:
        print("\nWelcome to the ATM")
        entered_pin = input("Please enter your PIN: ")
        atm.enter_pin(entered_pin)

        if atm.is_authenticated:
            while True:
                print("\n1. Check Balance")
                print("2. Withdraw Amount")
                print("3. Deposit Amount")
                print("4. Exit")

                choice = input("Please select an option: ")

                if choice == '1':
                    atm.check_balance()
                elif choice == '2':
                    amount = int(input("Enter amount to withdraw: "))
                    atm.withdraw(amount)
                elif choice == '3':
                    amount = int(input("Enter amount to deposit: "))
                    atm.deposit(amount)
                elif choice == '4':
                    atm.exit_atm()
                    break
                else:
                    print("Invalid option. Please try again.")

        continue_using = input("Do you want to continue using the ATM? (yes/no): ")
        if continue_using.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
