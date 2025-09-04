class Account:
    def __init__(self, initial_value=1000):
        self.value = initial_value
        self.name = "Account Value"
    
    def read(self):
        """Return the current account balance."""
        return self.value
    
    def write(self, amount):
        """Update the balance by adding the amount (can be negative for withdrawal)."""
        self.value += amount
        return self.value