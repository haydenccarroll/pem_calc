import re
import fractions
import input_cleaner
import f_to_d

class Calculator:
    def __init__(self, user_input):
        self.original_input = user_input
        self.PI = 3.1415926535897932384626433832795
        self.DICT_OF_OPERATORS =  {'*': 'MULTIPLY',
                                   '/': 'DIVIDE',
                                   '+': 'ADD',
                                   '(': 'LPARAN',
                                   ')': 'RPARAN',
                                   '^': 'EXPONENT',
                                   '|': 'ABS_VAL',
                                   '&': 'SQUARE_ROOT',
                                   '!': 'FACTORIAL',
                                   '@': 'LOG',
                                   '#': 'SIN',
                                   '`': 'COS',
                                   '_': 'TAN'}
        self.input = list(user_input)
        self.operator_indexes = dict()
        self.operator_symbols = r"*/+()^|&!@#`_"
        self.MESSAGE_TO_FUNCTS = [['Absolute Value Output:       ', self.abs_val_calc],
                                  ['Paranthesis Output:          ', self.paran_calc],
                                  ['Factorial Output:            ', self.factorial_calc],
                                  ['Sine Output:                 ', self.sin_calc],
                                  ['Cosine Output:               ', self.cos_calc],
                                  ['Tangent Output:              ', self.tan_calc],
                                  ['Logarithm Output:            ', self.log_calc],
                                  ['Square Root Output:          ', self.square_root_calc],
                                  ['Exponent Output:             ', self.exponent_calc], 
                                  ['Multiplication Output:       ', self.multiplication_calc],
                                  ['Division Output:             ', self.division_calc], 
                                  ['Addition/Subtraction Output: ', self.addition_subtraction_calc]]


    # inserts value by consecutive indexes, eg. ['12', '+', '2'] replace_with_value(14.0, [0,2]) -> [14.0]
    def replace_with_value(self, replacement, indexes_to_replace):
        del self.input[indexes_to_replace[0]:indexes_to_replace[1]+1]
        self.input.insert(indexes_to_replace[0], replacement)


    # redefines the output as a list, seperated by the operators. eg. ['1','1','+','2','2'] -> ['11', '+', '22']
    def seperate_by_operators(self): 
        self.input = re.split(f'([{self.operator_symbols}])', # splits input on every operator
                            "".join([str(x) for x in self.input]))
        for x in self.input: # gets rid of nospace characters that may occur due to the re.split
            if x == '':
                del self.input[self.input.index(x)]


    # updates operator_index as dictionary of all indexes of the operators eg. {'MULTIPLY': [1], "DIVISION": [3, 5], "ADDITION": []}
    def refresh_operator_indexes(self):
        self.operator_indexes = {self.DICT_OF_OPERATORS[symbol]:
                                [int(i) for i, x in enumerate(self.input)
                                if x == symbol] for symbol in self.operator_symbols} # matches symbol with list of location of symbol


    # carries out operations based off of the operator, and the index of the operator, and the input
    def binary_operator_calc_and_sub(self, operator_name, operator_index_in_dict):
        self.refresh_operator_indexes()
        left_operand = float(self.input[self.operator_indexes[operator_name][operator_index_in_dict]-1])
        right_operand = float(self.input[self.operator_indexes[operator_name][operator_index_in_dict]+1])
        left_index = self.operator_indexes[operator_name][operator_index_in_dict]-1
        right_index = self.operator_indexes[operator_name][operator_index_in_dict]+1
        
        if operator_name == 'EXPONENT':
            temp_output = left_operand ** right_operand
        if operator_name == 'MULTIPLY':
            temp_output = left_operand * right_operand
        elif operator_name == 'DIVIDE':
            temp_output = left_operand / right_operand
        elif operator_name == 'ADD':
            temp_output = left_operand + right_operand

        self.replace_with_value(temp_output, [left_index, right_index])


    # input function, string, and returns or possibly displays results
    def stage(self, message, function, print_bool, arg=None):
            self.seperate_by_operators()
            if arg is None:
                function()
            else:
                self.input = function(arg)
            if print_bool:
                print(message, "".join([str(x) for x in self.input]))


    def abs_val_calc(self):
        self.refresh_operator_indexes()
        while self.operator_indexes['ABS_VAL']:
            first_abs = self.operator_indexes['ABS_VAL'][0]
            second_abs = self.operator_indexes['ABS_VAL'][1]
            inside_abs = self.calculation(substr="".join(self.input[first_abs+1:second_abs]))
            inside_abs = (inside_abs**2)**0.5
            self.replace_with_value(inside_abs, [first_abs, second_abs])
            self.refresh_operator_indexes()


    # evaluates paranthesis, including nested ones
    def paran_calc(self):
        self.refresh_operator_indexes()
        while self.operator_indexes['LPARAN'] and self.operator_indexes['RPARAN']: #while paranthesis exist
            if len(self.operator_indexes['LPARAN']) != len(self.operator_indexes['RPARAN']): #unequal left and right paranthesis
                return "unequal left and right parans"
            
            first_sub_index = self.operator_indexes['LPARAN'][-1]

            #calculates number of unresolved left paranthesis before the last one
            left_parans_before_last = self.input[:first_sub_index].count('(')
            right_parans_before_last = self.input[:first_sub_index].count(')')
            num_of_unresolved_paran = left_parans_before_last - right_parans_before_last

            #calculates proper rparan to get rid of
            last_sub_index = self.operator_indexes['RPARAN'][-1-num_of_unresolved_paran]

            #calculates answer between paranthesis, replaces input, and updates operator indexes
            temp_input = ''.join(map(str, self.input[first_sub_index+1:last_sub_index])) #applies str to all input, since ''.join cant join ints or floats
            calculate_inside = Calculator(temp_input)
            calculate_inside.calculation(print_bool=False)
            answer = calculate_inside.input
            self.replace_with_value(answer, [first_sub_index, last_sub_index])
            self.refresh_operator_indexes()


    # calculates all factorials
    def factorial_calc(self):
        self.refresh_operator_indexes()
        for i in self.operator_indexes['FACTORIAL']:
            num_to_factorial = int(self.input[i-1])
            current_product = 1
            for z in range(2, num_to_factorial+1):
                current_product *= z
            self.input[i-1] = current_product
            del self.input[i]
            self.refresh_operator_indexes()



    # calculates all sine functions
    def sin_calc(self, alt_input=None):
        if alt_input is not None:
            alt_input = float(alt_input)*self.PI/180
            sign = -1
            for i in range(3, 16, 2):
                alt_input += sign*(alt_input**i) / self.calculation(substr=str(i) + '!') #uses own calculator to calculate factorial
                sign *= -1 #flips sign to positive, or negative but starts at negative

            alt_input = round(alt_input, 10)
            return alt_input
                
        self.refresh_operator_indexes() 
        while self.operator_indexes['SIN']:
            for i in self.operator_indexes['SIN']:
                answer = self.sin_calc(alt_input=self.input[i+1])
                self.replace_with_value(answer, [i, i+1])
                self.refresh_operator_indexes() 



    # calculates all cosine functions
    def cos_calc(self, alt_input=None):
        if alt_input is not None:
            alt_input = float(alt_input)*self.PI/180
            sign = 1
            for i in range(17, 2):
                alt_input += sign*(alt_input**i) / self.calculation(substr=str(i) + '!') #uses own calculator to calculate factorial
                sign *= -1 #flips sign to positive, or negative but starts at negative
            alt_input = round(alt_input, 10)
            return alt_input
        
        self.refresh_operator_indexes() 
        while self.operator_indexes['COS']:
            for i in self.operator_indexes['COS']:
                answer = self.cos_calc(alt_input=self.input[i+1])
                self.replace_with_value(answer, [i, i+1])
                self.refresh_operator_indexes() 

    # calculates all tangent functions in a string
    def tan_calc(self):
        self.refresh_operator_indexes()
        while self.operator_indexes['TAN']:
            for i in self.operator_indexes['TAN']:
                answer = self.sin_calc(alt_input=float(self.input[i+1])) / self.cos_calc(alt_input=float(self.input[i+1]))
                self.input[i+1] = answer
                del self.input[i]
                self.refresh_operator_indexes()


    # calculates all logs (base 10 only)
    def log_calc(self):
        self.refresh_operator_indexes()

        def find_log(to_log):
            guess_log = 1
            z = 1
            gone_higher = False
            while True and to_log > 0:
                if round(10**guess_log, 5) == to_log:
                    return guess_log
                elif 10**guess_log > to_log:
                    guess_log += -0.25/z
                    gone_higher = True
                elif 10**guess_log < to_log:
                    if gone_higher:
                        guess_log += 0.25/z
                    else:
                        guess_log += 1
                z += 1.5
            return 'Undefined'
        while self.operator_indexes['LOG']:
            for i in self.operator_indexes['LOG']:
                answer = find_log(float(self.input[i+1]))
                self.input[i+1] = answer
                del self.input[i]
                self.refresh_operator_indexes()


    # calculates square roots
    def square_root_calc(self):
        self.refresh_operator_indexes()
        while self.operator_indexes['SQUARE_ROOT']:
            if self.operator_indexes['RPARAN']:
                end_of_sqroot = [x for x in self.operator_indexes['RPARAN']
                                if x > self.operator_indexes['SQUARE_ROOT'][0]][0]
                temp_output = self.input[self.operator_indexes['SQUARE_ROOT'][0]+1:end_of_sqroot]
                del self.input[self.operator_indexes['SQUARE_ROOT'][0]:end_of_sqroot+1]
            else:
                temp_output = self.input[self.operator_indexes['SQUARE_ROOT'][0]+1::]
                del self.input[self.operator_indexes['SQUARE_ROOT'][0]::]
            temp_output = float(self.calculation(substr=temp_output, print_bool=False))**0.5
            self.input.insert(self.operator_indexes['SQUARE_ROOT'][0], temp_output)
            self.refresh_operator_indexes()


    # calculates all exponent operations
    def exponent_calc(self):
        self.refresh_operator_indexes()
        while self.operator_indexes['EXPONENT']:
            self.binary_operator_calc_and_sub('EXPONENT', -1)
            self.refresh_operator_indexes()


    def multiplication_calc(self):
        self.refresh_operator_indexes()
        while self.operator_indexes['MULTIPLY']:
            self.binary_operator_calc_and_sub('MULTIPLY', 0)
            self.refresh_operator_indexes()


    def division_calc(self):
        self.refresh_operator_indexes()
        while self.operator_indexes['DIVIDE']:
            self.binary_operator_calc_and_sub('DIVIDE', 0)
            self.refresh_operator_indexes()


    def addition_subtraction_calc(self):
        self.refresh_operator_indexes()
        while self.operator_indexes['ADD']:
            self.binary_operator_calc_and_sub('ADD', 0)
            self.refresh_operator_indexes()

    # calls all functions in proper order
    def calculation(self, print_bool=False, substr=''):
        if substr:
            substrCalc = Calculator(substr)
            substrCalc.calculation()
            return substrCalc.input
    
        self.stage('Input Correction Output: ', input_cleaner.clean_input, print_bool, (self.input))
        for message, funct in self.MESSAGE_TO_FUNCTS:
            self.stage(message, funct, print_bool)

        if float(self.input[0]) % 1 == 0: #if an integer
            self.input = int(float(self.input[0]))
        else:
            self.input = float(self.input[0])


# main function, thats called when it is the file opened.
def from_console():
        import time
        user_input = None
        while user_input != '':
            user_input = input("Please enter an expression for me to evaluate: ")
            time_start = time.time()
            main_calculator = Calculator(user_input)
            main_calculator.calculation(print_bool=True)
            print('\nthe final output as a decimal: ',
                  round(float(main_calculator.input), 10))
            print('The final output as a fraction: ',
                  f_to_d.frac_to_dec(main_calculator.input))
            time_end = time.time()
            print('It took ', round((time_end-time_start)*100000, 2),
                  'microseconds for the program to run!\n\n\n\n')
def for_electron_calc():
    user_input = sys.argv[2]
    try:
        calculator = Calculator(user_input)
        calculator.calculation()
        output = calculator.input
    except:
        output = "Error"
    finally:
        with open("../log/previous_calculations.txt", 'a') as file:
            file.write(f'{user_input}, {output}\n')

if __name__ == '__main__':
    import sys
    if sys.argv[1] == '-e':
        for_electron_calc()
    else:
        from_console()
