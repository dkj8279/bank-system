stored_pin = "123"
bank = 5000
wallet = 1000

while True:
    print("\n--- welcom to ma bank ---  ")
    pin_attempt = input("whats your pin ")

    if pin_attempt == stored_pin:
        print("acces granted")
        print("1. check bank")
        print("2. withdraw")
        print("3. deposit")
        print("4. check wallet")

        choice = input("choose 1, 2, 3 or 4 ")

        if choice == "1":
            print("your balance is " + str(bank) + "$ ")

        elif choice == "2":
            amount = int(input("how much cash u want "))
            if amount <= bank:
                bank = bank - amount
                wallet = wallet + amount
                print("gotcha bro. u got " + str(bank) + "$ left in the bank ")

            else:
                print("u dont have anough ")

        elif choice == "3":
            amount = int(input("how much?" ))
            if amount <= wallet:
                wallet = wallet - amount
                bank = bank + amount
                print("aightt bet. u got " + str(wallet) + " $ left in your wallet ")
            
            else:
                print("u dont have enough")

        if choice== "4":
            print("you have " + str(wallet) + "$ left in ur wallet")
    else:
        print("wrong pin")