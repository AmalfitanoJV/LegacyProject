from operations import Operations

def printMenu():
    print("--------------------------------")
    print("Account Management System")
    print("1. View Balance")
    print("2. Credit Account")
    print("3. Debit Account")
    print("4. Exit")
    print("--------------------------------")

def main():
    ops = Operations()
    while True:
        printMenu()
        choice = input("Select an option (1-4): ")
        
        
        if choice == '1':
            result = ops.process_transaction('BALANCE')
            print(result)
        
        elif choice == '2':
            amount = float(input("Enter credit amount: "))
            result = ops.process_transaction('CREDIT', amount)
            print(result)
        
        elif choice == '3':
            amount = float(input("Enter debit amount: "))
            result = ops.process_transaction('DEBIT', amount)
            print(result)
        
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")
    return 0

if __name__ == "__main__":
    main()