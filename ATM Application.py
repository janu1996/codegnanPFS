
details_ = {
    "Name": "Radha",
    "ATM PIN": "2286",
    "Balance": 100000
}

remaining_atp = 3

print("-------Welcome to ATM-------------")

while remaining_atp > 0:
    user_pin = input("Please enter your 4 digit pin:")

    if len(user_pin) == 4:
        if user_pin in details_["ATM PIN"]:
            func_ = int(input(" Please Select your option: \n1.Withdraw \n2.Deposit \n3.Balance \n4.Exit : "))

            # withdraw
            if func_ == 1:
                withdraw_m = int(input("Enter the amount you want to Withdraw:"))

                if withdraw_m <= details_['Balance'] and withdraw_m % 100 == 0:
                    details_["Balance"] -= withdraw_m
                    print(f"You have withdraw {withdraw_m} and total balance is {details_['Balance']}")
                else:
                    print("Insufficient Balance or change cannot be Withdrawn from the ATM")

            # deposit
            elif func_ == 2:
                deposit_m = int(input("Enter the amount you want to deposite:"))

                if deposit_m % 100 == 0:
                    details_["Balance"] += deposit_m
                    print(f"You have deposited {deposit_m} and total balance is {details_['Balance']}")
                else:
                    print("Change cannot be Deposited in the ATM")

            # balance
            elif func_ == 3:
                print(f"{details_['Balance']} is your balance amount...!")

            # exit
            elif func_ == 4:
                print("Thank you please visit again....!")
                break

            else:
                print("Please select from the above options:")

        else:
            remaining_atp -= 1
            if remaining_atp > 0:
                print(f"You have entered Incorrect pin and you have left with {remaining_atp} attempts")
            else:
                print("Your card is temporary blocked. Please contact bank!")
                break

    else:
        print("Please enter only 4 digit pin...!")
