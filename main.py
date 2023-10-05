print("\nPlease insert your card!")
password = 1234
balance = 20000
choice = 0

print("*" * 50)
pin = int(input("Dear customer Enter your four digit PIN: "))

if pin == password:

    while choice != 5:

        print("\n ========================= Select option =========================")
        print("1. Withrawal")
        print("2. Transfer")
        print("3. Buy Airtime")
        print("4. Change Pin")
        choice = int(input("Enter your option: "))

        if choice == 1:
            amount = int(input("Enter amount: "))
            if amount > 0 and amount <= balance:
                new_bal = balance - amount

                print("$", amount, "was successfully withdrawn from your account,", "Your account balance is $",
                      new_bal)
            else:
                print("Insufficient Fund!")

        elif choice == 2:
            print("1. Savings Account")
            print("2. Current Account")
            choose = int(input("Enter your option"))
            if choose == 1:
                receiver = int(input("Enter the account number: "))
                name = str(input("Enter the account name: "))
                amount = int(input("Enter amount: "))
                if amount > 0 and amount <= balance:
                    new_bal = balance - amount
                print("$", amount, "sent to ", name, "and your new balance is $", new_bal)
            elif choose == 2:
                receiver = int(input("Enter the account number: "))
                name = str(input("Enter the account name: "))
                amount = int(input("Enter amount: "))
                if amount > 0 and amount <= balance:
                    new_bal = balance - amount
                print("$", amount, "sent to ", name, "and your new balance is $", new_bal)
            else:
                print("Insufficient Fund!")
#
        elif choice == 3:
            receiver = int(input("Enter the Phone number: "))
            amount = int(input("Enter amount: "))
            if amount > 0 and amount <= balance:
                new_bal = balance - amount
                print("You have successfully sent", amount, "to ", receiver, "and your new balance is ", new_bal)
            else:
                print("Insufficient Fund!")
        elif choice == 4:
            current_pin = int(input("Enter your current PIN: "))
            if current_pin == pin:
                        new_pin = int(input("Enter your new PIN: "))
                        confirm_pin = int(input("Confirm your PIN: "))
                        if confirm_pin == new_pin:
                            print("Your new PIN is:", confirm_pin)
                        elif confirm_pin != new_pin:
                            print("Not matched, try again!")
                        elif current_pin != pin:
                            print("Re-enter your PIN")
            else:
                print("*****PIN incorrect!! Try again*****")