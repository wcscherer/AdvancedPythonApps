import unittest
from main import Bill, Roommate

# Test Roommate class init
class TestRoommate(unittest.TestCase):
    """
    Test init of Roommate
    """
    def test_roommate_with_wrong_type(self):
        with self.assertRaises(TypeError):
            roommate = Roommate(name=10.0, days_in_unit='forty')

# Test Bill class init
class TestBill(unittest.TestCase):
    """
    Test init of Bill
    """
    def test_bill_with_wrong_type(self):
        with self.assertRaises(TypeError):
            bill = Bill(amount='one hundred', period=3)

# Test the pay_bill method for Roommate
class TestPayBill(unittest.TestCase):

    def test_pay_bill(self):
        """
        Test the pay_bill method of roommate correctly calculates the fraction of bill owed by each roommate
        """
        # Requires Bill instance and two Roommate instances
        bill = Bill(amount=100, period="Jan 2000")

        # initiate roommates
        roommate1 = Roommate(name="John", days_in_unit=10)
        roommate2 = Roommate(name="Jane", days_in_unit=10)

        # initiate amount each has to pay
        r1_pays = roommate1.pay_bill(bill_instance=bill, other_roommate=roommate2)
        r2_pays = roommate2.pay_bill(bill_instance=bill, other_roommate=roommate1)

        # verify each roommate pays same amount (50)
        self.assertEqual(r1_pays, 50.0)
        self.assertEqual(r1_pays, r2_pays)

#if __name__ == '__main__':
#    unittest.main(verbosity=2)