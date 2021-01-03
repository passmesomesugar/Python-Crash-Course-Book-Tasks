from employee import Employee
import unittest


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.manager = Employee('mr', 'Anderson', 55000)
        # name = "mr."
        # last_name = "Anderson"
        # self.salary = 55000

    def test_give_default_raise(self):
        self.manager.give_raise()
        self.assertEqual(self.manager.salary, 60000)

    def test_give_custom_raise(self):
        self.manager.give_raise(10000)
        self.assertEqual(self.manager.salary, 65000)


if __name__ == '__main__':
    unittest.main()
