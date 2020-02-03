import unittest
from calc_files.calculation import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc_object = Calculator("")
    
    def test_replace_with_value(self):
        self.calc_object.input = list('3+3*11')
        self.calc_object.replace_with_value(6, [0, 2])
        self.assertEqual(self.calc_object.input, [6, '*', '1', '1'])

    def test_seperate_by_operators(self):
        self.calc_object.input = list('1+2*3/3+-1#33')
        self.calc_object.seperate_by_operators()
        self.assertEqual(self.calc_object.input, ['1', '+', '2', '*', '3', '/', '3', '+', '-1', '#', '33'])

        self.calc_object.input = list('22*(3+-1*5)')
        self.calc_object.seperate_by_operators()
        self.assertEqual(self.calc_object.input, ['22', '*', '(', '3', '+', '-1', '*', '5', ')'])

    def test_refresh_operator_indexes(self):
        self.assertEqual(self.calc_object.operator_indexes, dict())
        self.calc_object.input = list('3|3+-1*22|*2+-2')

        self.calc_object.refresh_operator_indexes()
        expected_indexes = {'MULTIPLY': [6, 10], 'DIVIDE': [], 'ADD': [3, 12], 'LPARAN': [], 'RPARAN': [],
                            'EXPONENT': [], 'ABS_VAL': [1, 9], 'SQUARE_ROOT': [], 'FACTORIAL': [],
                            'LOG': [], 'SIN': [], 'COS': [], 'TAN': []}
        self.assertEqual(self.calc_object.operator_indexes, expected_indexes)

        self.calc_object.input = ['3', '|', '3', '+', '-1', '*', '22', '|', '*', '2', '+', '-2']
        self.calc_object.refresh_operator_indexes()
        expected_indexes = {'MULTIPLY': [5, 8], 'DIVIDE': [], 'ADD': [3, 10], 'LPARAN': [], 'RPARAN': [],
                            'EXPONENT': [], 'ABS_VAL': [1, 7], 'SQUARE_ROOT': [], 'FACTORIAL': [],
                            'LOG': [], 'SIN': [], 'COS': [], 'TAN': []}
        self.assertEqual(self.calc_object.operator_indexes, expected_indexes)

    def test_binary_operator_calc_and_sub(self):
        #, operator_name, operator_index_in_dict
        self.calc_object.input = list('3+-4*3+(3+-1*4445)')
        self.calc_object.seperate_by_operators()
        self.calc_object.binary_operator_calc_and_sub("ADD", 0)
        expected_output = [-1.0, '*', '3', '+', '(', '3', '+', '-1', '*', '4445', ')']
        self.assertEqual(self.calc_object.input, expected_output)

        self.calc_object.seperate_by_operators()
        self.calc_object.binary_operator_calc_and_sub("MULTIPLY", -1)
        expected_output = ['-1.0', '*', '3', '+', '(', '3', '+', -4445, ')']
        self.assertEqual(self.calc_object.input, expected_output)

    def test_stage(self):
        pass 
        #nothing really to be implemented

    def test_abs_val_calc(self):
        self.calc_object.input = list('|3+-1*33|+5')
        self.calc_object.seperate_by_operators()
        self.calc_object.refresh_operator_indexes()
        self.calc_object.abs_val_calc()
        self.assertEqual(self.calc_object.input, [30.0, '+', '5'])

    def test_paran_calc(self):
        self.calc_object.input = list('(2+-1*5)+4')
        self.calc_object.seperate_by_operators()
        self.calc_object.paran_calc()
        self.assertEqual(self.calc_object.input, [-3, '+', '4'])

    def test_factorial_calc(self):
        self.calc_object.input = list('3!+44')
        self.calc_object.seperate_by_operators()
        self.calc_object.factorial_calc()
        self.assertEqual(self.calc_object.input, [6, '+', '44'])

    def test_sin_calc(self):
        self.calc_object.input = list('#45+545')
        self.calc_object.seperate_by_operators()
        self.calc_object.sin_calc()
        self.assertEqual(self.calc_object.input, [0.7060831596, '+', '545'])
    
    def test_cos_calc(self):
        self.calc_object.input = list('`45+545')
        self.calc_object.seperate_by_operators()
        self.calc_object.cos_calc()
        self.assertEqual(self.calc_object.input, [0.7853981634, '+', '545'])

    def test_tan_calc(self):
        self.calc_object.input = list('_45+545')
        self.calc_object.seperate_by_operators()
        self.calc_object.tan_calc()
        self.assertEqual(self.calc_object.input, [0.8990130006713484, '+', '545'])

    def test_log_calc(self):
        self.calc_object.input = list('@45+545')
        self.calc_object.seperate_by_operators()
        self.calc_object.log_calc()
        self.assertEqual(self.calc_object.input, [1.653212485951589, '+', '545'])

    
    def test_square_root_calc(self):
        self.calc_object.input = list('&36')
        self.calc_object.seperate_by_operators()
        self.calc_object.square_root_calc()
        self.assertEqual(self.calc_object.input, [6])

    def test_exponent_calc(self):
        self.calc_object.input = list('2^5')
        self.calc_object.seperate_by_operators()
        self.calc_object.exponent_calc()
        self.assertEqual(self.calc_object.input, [32])        
        
        self.calc_object.input = list('2^5+1')
        self.calc_object.seperate_by_operators()
        self.calc_object.exponent_calc()
        self.assertEqual(self.calc_object.input, [32, '+', '1'])
    
    def test_multiplication_calc(self):
        self.calc_object.input = list('2*-1+5*3')
        self.calc_object.seperate_by_operators()
        self.calc_object.multiplication_calc()
        self.assertEqual(self.calc_object.input, [-2, '+', 15])
    
    def test_division_calc(self):
        self.calc_object.input = list('2/-1+6/3')
        self.calc_object.seperate_by_operators()
        self.calc_object.division_calc()
        self.assertEqual(self.calc_object.input, [-2, '+', 2])
    
    def test_addition_subtraction_calc(self):
        self.calc_object.input = list('2+6+-1')
        self.calc_object.seperate_by_operators()
        self.calc_object.addition_subtraction_calc()
        self.assertEqual(self.calc_object.input, [7])
    
    def test_calculation(self):
        self.calc_object.input = list('2(4+-2)*555/555-45')
        self.calc_object.seperate_by_operators()
        self.calc_object.calculation()
        self.assertEqual(self.calc_object.input, -41)
    
        self.calc_object.input = list('2^(2+3) / 2^6')
        self.calc_object.seperate_by_operators()
        self.calc_object.calculation()
        self.assertEqual(self.calc_object.input, 0.5)

        self.calc_object.input = list('2_(2#3) / 2@6')
        self.calc_object.seperate_by_operators()
        self.calc_object.calculation()
        self.assertEqual(self.calc_object.input, 1.2850959936853117)

        self.assertEqual(self.calc_object.calculation(substr='5+455'), 460)
        