stored_pin = "123"
bank = 5000
wallet = 1000

while True:
    print("\n--- welcom to ma bank ---")
    pin_attempt = input("was ur pin ")

    if pin_attempt == stored_pin:
        print("acces granted")
        print("1. check bank")
        print("2. withdraw")
        print("3. deposit")

        choice = input("choose 1, 2 or 3")

        if choice == "1":
            print("ur balance is " + str(bank) + "$")

        elif choice == "2":
            amount = int(input("how much cash u wan twin"))
            if amount <= bank:
                bank = bank - amount
                wallet = wallet + amount
                print("gotcha bro. u got " + str(bank) + "$ left in da bank")

            else:
                print("u aint got anough")

        elif choice == "3":
            amount = int(input("how much?"))
            if amount <= wallet:
                wallet = wallet - amount
                bank = bank + amount
                print("aightt bet. u got " + str(wallet) + " $ left in yo wallet")
            
            else:
                print("u aint got anough")

    else:
        print("wrong pin brotein shake😂")