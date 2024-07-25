
import getpass

class Wallet:
    def __init__(self, account_name, account_number, phone_number, username, password, login_pin, transaction_pin):
        self.account_name = account_name
        self.account_number = account_number
        self.phone_number = phone_number
        self.username = username
        self.password = password
        self.login_pin = login_pin
        self.transaction_pin = transaction_pin
        self.balance = 0.0

class BankApplication:
    def __init__(self):
        self.accounts = {}

    def create_account(self, wallet_type, account_name, account_number, phone_number, username, password, login_pin, transaction_pin):
        if account_number in self.accounts:
            print(f"Account number {account_number} already exists.")
            return
        self.accounts[account_number] = Wallet(account_name, account_number, phone_number, username, password, login_pin, transaction_pin)
        print(f"{wallet_type} account created successfully for {account_name}.")

    def get_wallet_by_account_number(self, account_number):
        return self.accounts.get(account_number, None)

    def transfer_funds(self, from_account, to_account_number, amount, transaction_pin):
        to_account = self.get_wallet_by_account_number(to_account_number)
        if not to_account:
            print(f"Target account number {to_account_number} not found.")
            return

        if from_account.transaction_pin != transaction_pin:
            print("Incorrect transaction PIN.")
            return

        total_amount = amount * 1.075  # Including 7.5% VAT
        if from_account.balance < total_amount:
            print("Insufficient balance.")
            return

        from_account.balance -= total_amount
        to_account.balance += amount
        print(f"Transferred {amount} from {from_account.account_name} to {to_account.account_name}. Bank charge: {total_amount - amount}")

    def check_balance(self, account, transaction_pin):
        if account.transaction_pin != transaction_pin:
            print("Incorrect transaction PIN.")
            return
        print(f"Current balance: {account.balance}")

    def fund_account(self, account, amount, transaction_pin):
        if account.transaction_pin != transaction_pin:
            print("Incorrect transaction PIN.")
            return
        account.balance += amount
        print(f"Account funded with {amount}. Current balance: {account.balance}")

def main():
    bank_app = BankApplication()
    
    # Sample account creation
    bank_app.create_account("Debit", "John Doe", "123456", "555-1234", "johndoe", "password123", "1234", "5678")
    bank_app.create_account("Credit", "Jane Doe", "789012", "555-5678", "janedoe", "password456", "5678", "1234")
    
    while True:
        print("\nBanking Application")
        print("1. Check Account Balance")
        print("2. Transfer Funds")
        print("5. Fund Account")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '0':
            break
        
        account_number = input("Enter your account number: ")
        account = bank_app.get_wallet_by_account_number(account_number)
        if not account:
            print("Account not found.")
            continue
        
        login_pin = getpass.getpass("Enter login PIN: ")
        if account.login_pin != login_pin:
            print("Incorrect login PIN.")
            continue
        
        if choice == '1':
            transaction_pin = getpass.getpass("Enter transaction PIN: ")
            bank_app.check_balance(account, transaction_pin)
        
        elif choice == '2':
            to_account_number = input("Enter target account number: ")
            amount = float(input("Enter amount to transfer: "))
            transaction_pin = getpass.getpass("Enter transaction PIN: ")
            bank_app.transfer_funds(account, to_account_number, amount, transaction_pin)
        
        elif choice == '5':
            amount = float(input("Enter amount to fund: "))
            transaction_pin = getpass.getpass("Enter transaction PIN: ")
            bank_app.fund_account(account, amount, transaction_pin)
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
