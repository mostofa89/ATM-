def atm():
    print("Welcome to the ATM")
    pin = "1234"
    balance = 1000

    while True:
        enter_pin = input("Please enter your four-digit PIN or type 'exit' to quit: ")

        if enter_pin == pin:
            print("\n1. Check Balance")
            print("2. Withdraw Money")
            print("3. Deposit Money")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("\nPlease select a number: ")
            
            if choice == "1":
                print(f"Your balance is ${balance}")
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient balance")
                else:
                    balance -= amount
                    print(f"${amount} has been withdrawn, remaining balance is ${balance}")
            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                balance += amount
                print(f"${amount} has been added successfully, new balance is ${balance}")
            elif choice == "4":
                new_pin = input("Please enter a new four-digit PIN: ")
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN number updated successfully")
                else:
                    print("Invalid PIN format. PIN must be four digits")
            elif choice == "5":
                print("Thank you for using our ATM")
                break
            else:
                print("Invalid selection, please try again")
        
        elif enter_pin.lower() == "exit":
            print("Bye")
            break
        else:
            print("\nIncorrect PIN, please try again")

atm()
