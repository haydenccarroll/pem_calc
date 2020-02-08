import unittest
import calc_files.f_to_d

class TestFracDec(unittest.TestCase):
    def test_f_to_d(self):
        output = calc_files.f_to_d.frac_to_dec(sys_args=False, input_param='3/2')
        self.assertEqual(output, 1.5)

        output = calc_files.f_to_d.frac_to_dec(sys_args=False, input_param='0.5')
        self.assertEqual(output, '1/2')

        output = calc_files.f_to_d.frac_to_dec(sys_args=False, input_param=str(0.125))
        self.assertEqual(output, '1/8')

        output = calc_files.f_to_d.frac_to_dec(sys_args=False, input_param=str(1.999))
        self.assertEqual(output, '1999/1000')

        output = calc_files.f_to_d.frac_to_dec(sys_args=False, input_param=str(3.141592653589793238462641))
        self.assertEqual(output, '15707963/5000000')