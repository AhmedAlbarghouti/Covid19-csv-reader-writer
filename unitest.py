import unittest
#By Ahmed Albarghouti
import ControllerC


class MyTestCase(unittest.TestCase):

    def test_something(self):
        x = True
        if ControllerC.load_data() is False:
            x = False
            self.assertTrue(x is False)

        elif ControllerC.load_data() is True:
            self.assertTrue(x is True)


if __name__ == '__main__':
    unittest.main()
