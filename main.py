def withdraw(balance,amount):
    if amount < 0 :
        raise ValueError("Amount cannot be negative")

    if amount <= balance :
        return balance - amount

    return balance

import unittest

class TestWithdraw(unittest.TestCase):

    def setUp(self):
        self.balance = 1000

    def test_normal_withdraw(self):
        self.assertEqual(withdraw(self.balance,200),800)

    def test_full_withdraw(self):
        self.assertEqual(withdraw(self.balance,1000),0)

    def test_insufficient_withdraw(self):
        self.assertEqual(withdraw(self.balance,1500),1000)

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            withdraw(self.balance,-100)

if __name__ == "__main__":
    unittest.main()