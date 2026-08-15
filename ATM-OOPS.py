class ATM:
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.transactions = []

    # login with attempts and 4-digit validation
    def login(self):
        attempts = 3

        while attempts > 0:
            user_pin = input("Enter your Pin: ")

            # check pin length
            if len(user_pin) != 4:
                print("Please enter only a 4-digit PIN")
                continue

            # check correct pin
            if user_pin == self.pin:
                print("Login Successful\\n")
                return True

            else:
                attempts -= 1

                if attempts > 0:
                    print(f"Wrong PIN. You have {attempts} attempts left")
                else:
                    print("Your card is temporarily blocked")
                    return False

    # deposit money
    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print(f"₹{amount} deposited successfully")

    # withdraw money
    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount}")
            print(f"₹{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    # check balance
    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    # transaction history
    def show_transactions(self):
        print("Transaction History:")

        if self.transactions == []:
            print("No transactions found")
        else:
            for t in self.transactions:
                print(t)


# create object
atm = ATM("Lohitha", 90000, "9966")

# login first
if atm.login():

    while True:
        print("\\n----- ATM MENU -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.deposit()

        elif choice == "2":
            atm.withdraw()

        elif choice == "3":
            atm.check_balance()

        elif choice == "4":
            atm.show_transactions()

        elif choice == "5":
            print("Thank you for using our ATM")
            print("Visit Again...")
            break

        else:
            print("Invalid choice")
