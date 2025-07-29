# Bank ATM Simulator

def atm():
    pin = '1234'
    balance = 10000.0  # Initial balance

    print("🏧 Welcome to the ATM")
    entered_pin = input("Enter your 4-digit PIN: ").strip()

    if entered_pin != pin:
        print("❌ Incorrect PIN. Access denied.")
        return

    while True:
        print("\n------ ATM Menu ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        try:
            if choice == '1':
                print(f"💰 Current Balance: ₹{balance:.2f}")

            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                if amount <= 0:
                    print("Amount must be positive.")
                else:
                    balance += amount
                    print(f"✅ ₹{amount:.2f} deposited successfully.")

            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Amount must be positive.")
                elif amount > balance:
                    print("❌ Insufficient balance.")
                else:
                    balance -= amount
                    print(f"✅ ₹{amount:.2f} withdrawn successfully.")

            elif choice == '4':
                print("👋 Thank you for using the ATM. Goodbye!")
                break

            else:
                print("❗ Invalid choice. Please select between 1-4.")

        except ValueError:
            print("❌ Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    atm()
