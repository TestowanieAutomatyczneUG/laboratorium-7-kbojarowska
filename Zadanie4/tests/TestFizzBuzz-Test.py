import unittest
from src.main import FizzBuzz


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.temp = FizzBuzz()

    def testFizz_Buzz_positive_num5(self):
        self.assertEqual("Buzz", self.temp.game(5))

    def test_Fizz_Buzz_positive_num3(self):
        self.assertEqual("Fizz", self.temp.game(3))

    def test_Fizz_Buzz_positive_num15(self):
        self.assertEqual("FizzBuzz", self.temp.game(15))

    def test_Fizz_Buzz_positive_num4(self):
        self.assertEqual(4, self.temp.game(4))

    def test_Fizz_Buzz_positive_negative_5(self):
        self.assertEqual("Buzz", self.temp.game(-5))

    def test_Fizz_Buzz_positive_negative_3(self):
        self.assertEqual("Fizz", self.temp.game(-3))

    def test_Fizz_Buzz_positive_negative_15(self):
        self.assertEqual("FizzBuzz", self.temp.game(-15))

    def test_Fizz_Buzz_positive_negative_19(self):
        self.assertEqual(-19, self.temp.game(-19))

    def test_Fizz_Buzz_positive_big_Fizz(self):
        self.assertEqual("Fizz", self.temp.game(333333333333333333333))

    def test_Fizz_Buzz_positive_big_Buzz(self):
        self.assertEqual("Buzz", self.temp.game(417401738177137415))

    def test_Fizz_Buzz_positive_big_FizzBuzz(self):
        self.assertEqual("FizzBuzz", self.temp.game(14220))

    def test_Fizz_Buzz_positive_negative_big_Fizz(self):
        self.assertEqual("Fizz", self.temp.game(-333333333))

    def test_Fizz_Buzz_positive_negative_big_Buzz(self):
        self.assertEqual("Buzz", self.temp.game(-19778137490))

    def test_Fizz_Buzz_positive_negative_big_FizzBuzz(self):
        self.assertEqual("FizzBuzz", self.temp.game(-17027014125))


    def test_Fizz_Buzz_Exceptions_string_with_number(self):
        self.assertRaises(Exception, self.temp.game, "7")

    def test_Fizz_Buzz_Exceptions_list(self):
        self.assertRaises(Exception, self.temp.game, [1, 2, 3])

    def test_Fizz_Buzz_Exceptions_dict(self):
        self.assertRaises(Exception, self.temp.game, {"a": 1, "b": 2})

    def test_Fizz_Buzz_Exceptions_string(self):
        self.assertRaises(Exception, self.temp.game, "test")

    def test_Fizz_Buzz_Exceptions_empty_list(self):
        self.assertRaises(Exception, self.temp.game, [])

    def test_Fizz_Buzz_Exceptions_empty_dict(self):
        self.assertRaises(Exception, self.temp.game, {})

    def test_Fizz_Buzz_Exceptions_tuple(self):
        self.assertRaises(Exception, self.temp.game, (1, 2, 3))

    def test_Fizz_Buzz_Exceptions_float(self):
        self.assertRaises(Exception, self.temp.game, 3.14159)

    def test_Fizz_Buzz_Exceptions_negative_float(self):
        self.assertRaises(Exception, self.temp.game, -5.1352)

    def test_Fizz_Buzz_Exceptions_complex_numbers(self):
        self.assertRaises(Exception, self.temp.game, 5 + 2j)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
