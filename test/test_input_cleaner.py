import unittest
import calc_files.input_cleaner

class TestInputCleaner(unittest.TestCase):
    def test_clean_input(self):
        output = calc_files.input_cleaner.clean_input('2-22')
        self.assertEqual(output, list('2+-1*22'))

        output = calc_files.input_cleaner.clean_input('2(3-2)')
        self.assertEqual(output, list('2*(3+-1*2)'))


