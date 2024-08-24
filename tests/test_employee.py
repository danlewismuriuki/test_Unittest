import unittest

from employee import Employee


class testEmployee(unittest.TestCase):
    def test_email(self):
        emp1 = Employee("Dan", "Lewis", 120)
        emp2 = Employee("Mike", "Tyson", 80)

        self.assertEqual(emp1.email, "Dan.Lewis@email.com")
        self.assertEqual(emp2.email, "Mike.Tyson@email.com")

        emp1.first = "Alex"
        emp2.last = "Muriuki"

        self.assertEqual(emp1.email, "Alex.Lewis@email.com")
        self.assertEqual(emp2.email, "Mike.Muriuki@email.com")
