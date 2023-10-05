print("\nPlease insert your card!")
password = 1234
cash = 20000
choice = 0

print("*" * 50)
pin = int(input("Dear customer Enter your four digit PIN: "))

if pin == password:
    def withdraw():
        cash = 10000
        time = "12:23pm"
        date = "12/11/2022"
        password = 1234
        Agent = int(input("Enter the agent number: "))
        amount = int(input("Enter amount: "))
        if amount > 0 and amount <= cash:
            remainingCash = cash - amount
            print("$", amount, "withdraw successfully", Agent, "on", date, "at", time, "balance is: ", remainingCash)
        else:
            print("Not enough money in your account")
def transfer():
    cash = 10000
    time = "12:23pm"
    date = "12/11/2022"
    receiver = int(input("Enter the number: "))
    amount = int(input("Enter amount: "))
    if amount > 0 and amount <= cash:
        new_bal = cash - amount
        print("Amount ksh", amount, "sent to: ", receiver, "on", date, "at", time, "and your new balance is: ", new_bal)
    else:
        print("Not enough cash in your account!")

def buy_airtime():
    cash = 10000
    time = "12:23pm"
    date = "12/11/2022"
    amount = int(input("Enter amount: "))
    balance = cash - amount
    print("Airtime of", amount, "bought on", date, "at", time, "now balance is: ", balance)

def change_pin():
    cash = 10000
    amount = int(input("Enter amount: "))
    new_balance = cash + amount
    print("Amount", amount, "deposited successfully new balance is: ", new_balance)


while True:
    # print("*" * 50)
    print("Welcome!")
    print("*" * 50)
    print("1. Withdrawal")
    print("*" * 50)
    print("2. Transfer")
    print("*" * 50)
    print("3. Buy Airtime")
    print("*" * 50)
    print("4. Change PIN")
    print("*" * 50)
    print("5. Reset Account")
    print("*" * 50)

    user = int(input("Choose option: "))
    if user == 1:
        withdraw()
    elif user == 2:
        transfer()
    elif user == 3:
        buy_airtime()
    elif user == 4:
        change_pin()

    else:
        print("Enter a valid choice")