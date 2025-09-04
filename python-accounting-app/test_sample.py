import unittest
from operations import Operations

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.ops = Operations(initial_value=1000)

    def test_view_current_balance(self):
        result = self.ops.process_transaction('BALANCE')
        self.assertEqual(result, "Current balance: 1000")

    def test_credit_account_valid_amount(self):
        result = self.ops.process_transaction('CREDIT', 100)
        self.assertEqual(result, "Credited 100. New balance: 1100")

    def test_credit_account_zero_amount(self):
        result = self.ops.process_transaction('CREDIT', 0)
        self.assertEqual(result, "Credited 0. New balance: 1000")

    def test_debit_account_valid_amount(self):
        result = self.ops.process_transaction('DEBIT', 50)
        self.assertEqual(result, "Debited 50. New balance: 950")

    def test_debit_account_amount_greater_than_balance(self):
        result = self.ops.process_transaction('DEBIT', 2000)
        self.assertEqual(result, "Insufficient funds")

    def test_debit_account_zero_amount(self):
        result = self.ops.process_transaction('DEBIT', 0)
        self.assertEqual(result, "Debited 0. New balance: 1000")

    def test_invalid_operation_type(self):
        result = self.ops.process_transaction('UNKNOWN')
        self.assertEqual(result, "Invalid operation type")

    def test_integration_credit_and_debit(self):
        # Credit 200
        self.ops.process_transaction('CREDIT', 200)
        # Debit 150
        result = self.ops.process_transaction('DEBIT', 150)
        self.assertEqual(result, "Debited 150. New balance: 1050")
        # Check balance
        result = self.ops.process_transaction('BALANCE')
        self.assertEqual(result, "Current balance: 1050")

if __name__ == "__main__":
    unittest.main()