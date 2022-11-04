import unittest
from genlib.core import parse_column_data


class GenLibTest(unittest.TestCase):

    def test_correct_structure(self):
        """
        column_data must be list of tuples (name, type)
        type = integer | string
        """
        input_column_data = '[("hello","integer"), ("world","string")]'
        expect = [("hello", "integer"), ("world", "string")]
        result = parse_column_data(input_column_data)
        self.assertEqual(result, expect)

        input_column_data = '[("hello","INVALID"), ("world","string")]'
        expect = [("hello", "integer"), ("world", "string")]
        with self.assertRaises(ValueError):
            parse_column_data(input_column_data)
        self.assertEqual(result, expect)

        # TODO: Test wrong size of tuple
        # TODO: Test wrong shape of list


if __name__ == '__main__':
    unittest.main()
