import re
import fractions
from calc_input_cleaner import clean_input


class Calculator:
    def __init__(self, user_input):
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
        self.MESSAGE_TO_FUNCTS = [['Absolute Value Output: ', self.abs_val_calc], ['Paranthesis Output: ', self.paran_calc],
                              ['Factorial Output: ', self.factorial_calc], ['Sine Output: ', self.sin_calc], ['Cosine Output: ', self.cos_calc],
                              ['Tangent Output: ', self.tan_calc], ['Logaritm Output: ', self.log_calc], ['Square Root Output: ', self.square_root_calc],
                              ['Exponent Output: ', self.exponent_calc], ['Multiplication Output: ', self.multiplication_calc],
                              ['Division Output: ', self.division_calc], ['Addition/Subtraction Output: ', self.addition_subtraction_calc]]


    # replaces list by consecutive indexes, eg. (['12', '+', '2'], 14.0, [0,2]) -> [14.0]
    def replace_list(self, replacement, indexes_to_replace):
        del self.input[indexes_to_replace[0]:indexes_to_replace[1]+1]
        self.input.insert(indexes_to_replace[0], replacement)


    # redefines the output as a list, seperated by the operators. eg. ['1','1','+','2','2'] -> ['11', '+', '22']
    def seperate_by_operators(self): 
        self.input = re.split(r'([+*^\/()\|\&\!\@\#\`\_])',
                            "".join([str(x) for x in self.input]))
        for x in self.input: # gets rid of nospace characters that may occur due to the re.split
            if x == '':
                del self.input[self.input.index(x)]


    # returns dictionary of all indexes of the operators eg. {'MULTIPLY': [1], "DIVISION": [3, 5], "ADDITION": []}
    def determine_which_operation(self):
        self.operator_indexes = {self.DICT_OF_OPERATORS[symbol]:
                                [int(i) for i, x in enumerate(self.input)
                                if x == symbol] for symbol in r"*/+()^|&!@#`_"}


    # carries out operations based off of the operator, and the index of the operator, and the input
    def emda_calc_and_substitute(self, operator_index,
                                index_in_operator_index, operator):
        self.determine_which_operation()
        if operator == '^':
            temp_output = float(self.input[self.operator_indexes[operator_index]
                                [index_in_operator_index]-1]) \
                                ** float(self.input[self.operator_indexes[operator_index]
                                        [index_in_operator_index]+1])
        elif operator == '*':
            temp_output = float(self.input[self.operator_indexes[operator_index]
                                [index_in_operator_index]-1]) \
                                * float(self.input[self.operator_indexes[operator_index]
                                        [index_in_operator_index]+1])
        elif operator == '/':
            left_num = float(self.input[self.operator_indexes[operator_index]
                                    [index_in_operator_index]-1])
            right_num = float(self.input[self.operator_indexes[operator_index]
                                        [index_in_operator_index]+1])
            temp_output = left_num / right_num
        elif operator == '+':
            left_num = float(self.input[self.operator_indexes[operator_index]
                                            [index_in_operator_index]-1])
            right_num = float(self.input[self.operator_indexes[operator_index]
                                            [index_in_operator_index]+1])
            temp_output = left_num + right_num

        left_index = self.operator_indexes[operator_index][index_in_operator_index]-1
        right_index = self.operator_indexes[operator_index][index_in_operator_index]+1
        self.replace_list(temp_output, [left_index, right_index])


    # input function, string, and returns or possibly displays results
    def stage(self, message, function, print_bool, arg=None):
            self.seperate_by_operators()
            if arg is None:
                function()
            else:
                self.input = function(arg)
            if print_bool:
                print(message, "".join([str(x) for x in self.input]))


    # calculates all absolute values
    def add_parens_for_abs_val(self):
        characters_inserted = 0
        self.determine_which_operation()
        indexes = self.operator_indexes["ABS_VAL"]
        for i in range(len(indexes)):
            if i % 2 == 0:
                self.input.insert(indexes[i]+1+characters_inserted, '(')  # makes |(
            else:
                self.input.insert(indexes[i]+characters_inserted, ')')  # makes )|
            characters_inserted += 1


    def abs_val_calc(self):
        self.determine_which_operation()
        if not self.operator_indexes['ABS_VAL']:
            return
        self.add_parens_for_abs_val()
        self.paran_calc()
        self.determine_which_operation()
        while self.operator_indexes['ABS_VAL']:
            first_abs = self.operator_indexes['ABS_VAL'][0]
            second_abs = self.operator_indexes['ABS_VAL'][1]
            inside_abs = float("".join(self.input[first_abs+1:second_abs]))
            inside_abs = (inside_abs**2)**0.5
            self.replace_list(inside_abs, [first_abs, second_abs])
            self.determine_which_operation()


    # evaluates paranthesis, including nested ones
    def paran_calc(self):
        temp_input = ''
        self.seperate_by_operators()
        self.determine_which_operation()
        while self.operator_indexes['LPARAN']:
            num_of_nested_lparan, num_of_nested_rparan = -1, -1
            for i in enumerate(self.input[self.operator_indexes['LPARAN'][0]:]): #can looping through a changing dict cause problems? probaly not in this case
                if i[1] == '(':
                    num_of_nested_lparan += 1
                elif i[1] == ')':
                    num_of_nested_rparan += 1
                elif len(self.input)-1-i[0] == self.operator_indexes['LPARAN'][0]:
                    while num_of_nested_lparan != num_of_nested_rparan:
                        self.input.append(')')
                        self.determine_which_operation()
                        num_of_nested_rparan += 1

                if num_of_nested_rparan == num_of_nested_lparan:
                    for z in self.operator_indexes['RPARAN']:
                        if z > self.operator_indexes['LPARAN'][num_of_nested_lparan]:
                            right_paran_place = z
                            break

                    temp_input = self.input[self.determine_which_operation()
                                        ['LPARAN'][num_of_nested_lparan]+1:
                                        right_paran_place]

                    paran_calculator_object = Calculator(temp_input)
                    paran_calculator_object.calculation(print_bool=False)
                    temp_input = paran_calculator_object.input
                    left_paran = self.determine_which_operation()['LPARAN'] \
                        [num_of_nested_lparan]
                    self.replace_list(str(temp_input),
                                [left_paran, right_paran_place])
                    break


    # calculates all factorials
    def factorial_calc(self):
        for i in self.determine_which_operation()['FACTORIAL']:
            num_to_factorial = int(self.input[i-1])
            current_product = 1
            for z in range(1, num_to_factorial+1):
                current_product *= z
            self.input[i-1] = current_product
            del self.input[i]


    # calculates all sine functions
    def sin_calc(self, alt_input=None):
        indexes = self.determine_which_operation()
        if alt_input is not None:
            alt_input = float(alt_input)*self.PI/180
            alt_input = alt_input - (alt_input**3/(3*2)) + (alt_input**5/(5*4*3*2)) - \
                    (alt_input**7/(7*6*5*4*3*2)) + (alt_input**9/(9*8*7*6*5*4*3*2)) \
                    - (alt_input**11/(11*10*9*8*7*6*5*4*3*2)) + \
                    (alt_input**13/(13*12*11*10*9*8*7*6*5*4*3*2)) - \
                    (alt_input**15/(15*14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
                    (alt_input**17/(17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
            alt_input = round(alt_input, 10)
            return alt_input

        while indexes['SIN']:
            for i in indexes['SIN']:
                answer = float(self.input[i+1])*self.PI/180
                answer = answer - (answer**3/(3*2)) + (answer**5/(5*4*3*2)) - \
                    (answer**7/(7*6*5*4*3*2)) + (answer**9/(9*8*7*6*5*4*3*2)) \
                    - (answer**11/(11*10*9*8*7*6*5*4*3*2)) + \
                    (answer**13/(13*12*11*10*9*8*7*6*5*4*3*2)) - \
                    (answer**15/(15*14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
                    (answer**17/(17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
                answer = round(answer, 10)
                self.input[i+1] = answer #can maybe use replace function
                del self.input[i]
            indexes = self.determine_which_operation() 


    # calculates all cosine functions # need to do nochangeunput bool
    def cos_calc(self, alt_input=None):
        if alt_input is not None:
            alt_input = float(alt_input)*self.PI/180
            alt_input = 1 - (alt_input**2/(2)) + (alt_input**4/(4*3*2)) - \
                    (alt_input**6/(6*5*4*3*2)) + (alt_input**8/(8*7*6*5*4*3*2)) - \
                    (alt_input**10/(10*9*8*7*6*5*4*3*2)) + \
                    (alt_input**12/(12*11*10*9*8*7*6*5*4*3*2)) - \
                    (alt_input**14/(14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
                    (alt_input**16/(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
            alt_input = round(alt_input, 10)
            return alt_input

        indexes = self.determine_which_operation()
        while indexes['COS']:
            for i in indexes['COS']:
                answer = float(self.input[i+1])*self.PI/180
                answer = 1 - (answer**2/(2)) + (answer**4/(4*3*2)) - \
                    (answer**6/(6*5*4*3*2)) + (answer**8/(8*7*6*5*4*3*2)) - \
                    (answer**10/(10*9*8*7*6*5*4*3*2)) + \
                    (answer**12/(12*11*10*9*8*7*6*5*4*3*2)) - \
                    (answer**14/(14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
                    (answer**16/(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
                answer = round(answer, 10)
                self.input[i+1] = answer
                del self.input[i]
            indexes = self.determine_which_operation()


    # calculates all tangent functions in a string
    def tan_calc(self):
        indexes = self.determine_which_operation()
        while indexes['TAN']:
            for i in indexes['TAN']:
                answer = self.sin_calc(alt_input=float(self.input[i+1])) / self.cos_calc(alt_input=float(self.input[i+1]))
                self.input[i+1] = answer
                del self.input[i]
            indexes = self.determine_which_operation()


    # calculates all logs (base 10 only)
    def log_calc(self):
        indexes = self.determine_which_operation()

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
        while indexes['LOG']:
            for i in indexes['LOG']:
                answer = find_log(float(self.input[i+1]))
                self.input[i+1] = answer
                del self.input[i]
                indexes = self.determine_which_operation()


    # calculates square roots
    def square_root_calc(self):
        indexes = self.determine_which_operation()
        while indexes['SQUARE_ROOT']:
            if indexes['RPARAN']:
                end_of_sqroot = [x for x in indexes['RPARAN']
                                if x > indexes['SQUARE_ROOT'][0]][0]
                temp_output = self.input[indexes['SQUARE_ROOT'][0]+1:end_of_sqroot]
                del self.input[indexes['SQUARE_ROOT'][0]:end_of_sqroot+1]
            else:
                temp_output = self.input[indexes['SQUARE_ROOT'][0]+1::]
                del self.input[indexes['SQUARE_ROOT'][0]::]
            temp_output = float(self.calculation(temp_output, False))**0.5
            self.input.insert(indexes['SQUARE_ROOT'][0], temp_output)
            indexes = self.determine_which_operation()


    # calculates all exponent operations
    def exponent_calc(self):
        while self.determine_which_operation()['EXPONENT']:
            self.emda_calc_and_substitute('EXPONENT', -1, '^')

    def multiplication_calc(self):
        while self.determine_which_operation()['MULTIPLY']:
            self.emda_calc_and_substitute('MULTIPLY', 0, '*')


    def division_calc(self):
        while self.determine_which_operation()['DIVIDE']:
            self.emda_calc_and_substitute('DIVIDE', 0, '/')


    def addition_subtraction_calc(self):
        while self.determine_which_operation()['ADD']:
            self.emda_calc_and_substitute('ADD', 0, '+')


    # calls all functions in proper order
    def calculation(self, print_bool=True, return_val=False):

        self.stage('Input Correction Output: ', clean_input, print_bool, (self.input))
        for message, funct in self.MESSAGE_TO_FUNCTS:
            self.stage(message, funct, print_bool)

        if float(self.input[0]) % 1 == 0: #if an integer
            self.input = int(float(self.input[0]))
        else:
            self.input = float(self.input[0])

        if return_val:
            pass


# main function, thats called when it is the file opened.
def main():
        import time
        user_input = None
        while user_input != '':
            time_start = time.time()
            user_input = input("Please enter an expression for me to evaluate: ")
            main_calculator = Calculator(user_input)
            main_calculator.calculation()
            print('\nthe final output as a decimal: ',
                  round(float(main_calculator.input), 10))
            print('The final output as a fraction: ',
                  fractions.Fraction(main_calculator.input).limit_denominator())

            time_end = time.time()

            print('It took ', round((time_end-time_start)*100000, 2),
                  'microseconds for the program to run!\n\n\n\n')
if __name__ == '__main__':
    main()

#messes up when it goes in e form
#cannot do nested abs vals


#could potentially capitalize on a/b == a*(1/b)