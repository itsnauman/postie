import unittest
from postie import Postie
from postie import create_parser
import os


class TestPostie(unittest.TestCase):

    def setUp(self):
        self.parser = create_parser()

    def test_no_args(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_no_csv_arg(self):
        with self.assertRaises(SystemExit):
            arg = self.parser.parse_args(['-t', 'test.txt'])
            self.assertIsNone(arg.csv)

    def test_no_template_arg(self):
        with self.assertRaises(SystemExit):
            arg = self.parser.parse_args(['-csv', 'test.csv'])
            self.assertIsNone(arg.template)

if __name__ == '__main__':
    unittest.main()
