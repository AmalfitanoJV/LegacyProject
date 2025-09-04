from data import Account

class Operations:
    def __init__(self, initial_value=1000):
        self.account = Account(initial_value)
    
    def process_transaction(self, operation_type, amount=0):
        """Process a transaction based on the operation type."""
        if operation_type == 'DEBIT':
            current_balance = self.account.read()
            if amount > current_balance:
                return "Insufficient funds"
            new_balance = self.account.write(-amount)
            return f"Debited {amount}. New balance: {new_balance}"
        
        elif operation_type == 'CREDIT':
            new_balance = self.account.write(amount)
            return f"Credited {amount}. New balance: {new_balance}"
        
        elif operation_type == 'BALANCE':
            current_balance = self.account.read()
            return f"Current balance: {current_balance}"
        
        else:
            return "Invalid operation type"