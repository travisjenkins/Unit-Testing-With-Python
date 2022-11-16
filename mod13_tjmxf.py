import unittest
import re
from datetime import datetime

def get_valid_symbol(symbol:str) -> str:
    try:
        expression_to_match = '^[a-zA-Z]{1,7}$'
        if re.search(expression_to_match, symbol):
            if symbol.isupper():
                return symbol
            else:
                return symbol.upper()
    except TypeError:
        raise TypeError("💥 ERROR:  Symbol can only be characters, and 1 - 7 in length. 💥")

def get_valid_chart_type(chart_type:str) -> int:
    try:
        int_chart_type = int(chart_type)
    except ValueError:
        raise ValueError("💥 ERROR:  Chart type must be a number. 💥")
    else:
        if int_chart_type == 1 or int_chart_type == 2:
            return int_chart_type
        else:
            raise ValueError("💥 ERROR:  Chart type must be either a 1 or 2. 💥")

def get_valid_time_series(time_series:str) -> int:
    allowed_list = [1, 2, 3, 4]
    try:
        int_time_series = int(time_series)
    except ValueError:
        raise ValueError("💥 ERROR:  Time series must be a number. 💥")
    else:
        if int_time_series in allowed_list:
            return int_time_series
        else:
            raise ValueError("💥 ERROR:  Time series must be a number in the 1 - 4 range. 💥")

def get_valid_date(user_date:str) -> datetime:
    try:
        valid_date = datetime.strptime(user_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("💥 ERROR:  Must be a valid date in the format YYYY-MM-DD. 💥")
    else:
        return valid_date

class TestUserDataInput(unittest.TestCase):
    def setUp(self):
        self.symbol = "abc"
        self.chart_type = 2
        self.time_series = 2
        self.start_date = "2022-10-01"
        self.end_date = "2022-10-31"

    def tearDown(self):
        self.symbol = ""
        self.chart_type = 0
        self.time_series = 0
        self.start_date = ""
        self.end_date = ""

    def test_symbol_between_1_and_7_characters_capitalized(self):
        # Arrange
        user_symbol = self.symbol
        expression_to_match = '^[A-Z]{1,7}$'
        # Act
        symbol = get_valid_symbol(user_symbol)
        # Assert
        self.assertRegex(symbol, expression_to_match)
        with self.assertRaises(TypeError) as err:
            get_valid_symbol(123)

        print(err.exception)

    def test_chart_type_one_number_either_1_or_2(self):
        # Arrange
        user_chart_type = self.chart_type
        # Act
        chart_type = get_valid_chart_type(user_chart_type)
        # Assert
        self.assertTrue(chart_type == 1 or chart_type == 2)
        with self.assertRaises(ValueError) as err:
            get_valid_chart_type("a")
        with self.assertRaises(ValueError) as err_2:
            get_valid_chart_type("3")

        print(err.exception)
        print(err_2.exception)

    def test_time_series_one_number_one_to_four(self):
        # Arrange
        user_time_series = self.time_series
        allowed_list = [1, 2, 3, 4]
        # Act
        time_series = get_valid_time_series(user_time_series)
        # Assert
        self.assertIn(time_series, allowed_list)
        with self.assertRaises(ValueError) as err:
            get_valid_time_series("a")
        with self.assertRaises(ValueError) as err_2:
            get_valid_time_series(5)

        print(err.exception)
        print(err_2.exception)

    def test_start_date_is_date_with_correct_format(self):
        # Arrange
        user_start_date = self.start_date
        # Act
        start_date = get_valid_date(user_start_date)
        # Assert
        self.assertIsInstance(start_date, datetime)
        with self.assertRaises(ValueError) as err:
            get_valid_date("2022-10-32")

        print(err.exception)

    def test_end_date_is_date_with_correct_format(self):
        # Arrange
        user_end_date = self.end_date
        # Act
        end_date = get_valid_date(user_end_date)
        # Assert
        self.assertIsInstance(end_date, datetime)
        with self.assertRaises(ValueError) as err:
            get_valid_date("2022-10-32")

        print(err.exception)

if __name__ == '__main__':
   unittest.main()