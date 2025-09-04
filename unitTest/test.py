import unittest
from data import Account
from operations import Operations

class TestCOBOLApp(unittest.TestCase):
    def setUp(self):
        self.initial_balance = 1000.00
        self.ops = Operations(self.initial_balance)

    # TC-1.1: View Current Balance
    def test_view_current_balance(self):
        result = self.ops.process_transaction('BALANCE')
        self.assertIn(str(self.initial_balance), result)

    # TC-2.1: Credit Account with Valid Amount
    def test_credit_account_with_valid_amount(self):
        amount = 100.00
        result = self.ops.process_transaction('CREDIT', amount)
        self.assertIn(str(self.initial_balance + amount), result)

    # TC-2.2: Credit Account with Zero Amount
    def test_credit_account_with_zero_amount(self):
        amount = 0.00
        result = self.ops.process_transaction('CREDIT', amount)
        self.assertIn(str(self.initial_balance), result)

    # TC-3.1: Debit Account with Valid Amount
    def test_debit_account_with_valid_amount(self):
        amount = 50.00
        result = self.ops.process_transaction('DEBIT', amount)
        self.assertIn(str(self.initial_balance - amount), result)

    # TC-3.2: Debit Account with Amount Greater Than Balance
    def test_debit_account_with_amount_greater_than_balance(self):
        amount = self.initial_balance + 1000.00
        result = self.ops.process_transaction('DEBIT', amount)
        self.assertEqual(result, "Insufficient funds")
        # Balance should remain unchanged
        balance_result = self.ops.process_transaction('BALANCE')
        self.assertIn(str(self.initial_balance), balance_result)

    # TC-3.3: Debit Account with Zero Amount
    def test_debit_account_with_zero_amount(self):
        amount = 0.00
        result = self.ops.process_transaction('DEBIT', amount)
        self.assertIn(str(self.initial_balance), result)

    # TC-4.1: Exit the Application (not applicable for unit test, but included for completeness)
    def test_exit_application(self):
        # Placeholder: nothing to test for CLI exit
        pass

if __name__ == '__main__':
    unittest.main()