import re
import fractions
from calc_input_cleaner import clean_input


class Calculator:
    def __init__(self):
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



    def decimal_to_fraction(self, the_input):
            return fractions.Fraction(the_input).limit_denominator()


    # replaces list by consecutive indexes
    def replace_list(self, input_list, replacement_string, indexes_to_replace):
        if type(input_list) != list:
            input_list = list(input_list)
        del input_list[indexes_to_replace[0]:indexes_to_replace[1]+1]
        input_list.insert(indexes_to_replace[0], replacement_string)
        return input_list


    # redefines the output as a list and uses a regex to do this
    def seperate_by_operators(self, the_input):
        the_input = re.split(r'([+*^\/()\|\&\!\@\#\`\_])',
                            "".join([str(x) for x in the_input]))
        for x in the_input:
            if x == '':
                del the_input[the_input.index(x)]
        return the_input


    # determines the index of operators, and returns a list
    def determine_which_operation(self, the_input):
        indexes_of_operators = {self.DICT_OF_OPERATORS[symbol]:
                                [int(i) for i, x in enumerate(the_input)
                                if x == symbol] for symbol in r"*/+()^|&!@#`_"}
        return indexes_of_operators


    # carries out operations, and then deletes values, and adds values.
    def emda_calc_and_substitute(self, the_input, operator_index,
                                index_in_operator_index, operator):
        indexes = self.determine_which_operation(the_input)
        if operator == '^':
            temp_output = float(the_input[indexes[operator_index]
                                [index_in_operator_index]-1]) \
                                ** float(the_input[indexes[operator_index]
                                        [index_in_operator_index]+1])
        elif operator == '*':
            temp_output = float(the_input[indexes[operator_index]
                                [index_in_operator_index]-1]) \
                                * float(the_input[indexes[operator_index]
                                        [index_in_operator_index]+1])
        elif operator == '/':
            left_num = float(the_input[indexes[operator_index]
                                    [index_in_operator_index]-1])
            right_num = float(the_input[indexes[operator_index]
                                        [index_in_operator_index]+1])
            temp_output = left_num / right_num
        elif operator == '+':
            left_num = float(the_input[indexes[operator_index]
                                            [index_in_operator_index]-1])
            right_num = float(the_input[indexes[operator_index]
                                            [index_in_operator_index]+1])
            temp_output = left_num + right_num
        print()
        left_index = indexes[operator_index][index_in_operator_index]-1
        right_index = indexes[operator_index][index_in_operator_index]+1
        the_input = self.replace_list(the_input, temp_output, [left_index, right_index])
        indexes = self.determine_which_operation(the_input)
        return the_input, indexes


    # input function, string, and returns or possibly displays results
    def stage(self, message, function, the_input, print_bool):
            the_input = list(the_input)
            the_input = self.seperate_by_operators(the_input)
            the_input = function(the_input)
            if print_bool:
                print(message, "".join([str(x) for x in the_input]))
                return the_input
            return the_input


    # calculates all absolute values
    def add_parens_for_abs_val(self, the_input):
        characters_inserted = 0
        indexes = self.determine_which_operation(the_input)["ABS_VAL"]
        for i in range(len(indexes)):
            if i % 2 == 0:
                the_input.insert(indexes[i]+1+characters_inserted, '(')  # makes |(
            else:
                the_input.insert(indexes[i]+characters_inserted, ')')  # makes )|
            characters_inserted += 1
        return the_input


    def abs_val_calc(self, the_input):
        if not self.determine_which_operation(the_input)['ABS_VAL']:
            return the_input
        the_input = self.add_parens_for_abs_val(the_input)
        print('194', the_input)
        the_input = self.paran_calc(the_input)
        print(the_input, 'in abs val calc')
        while self.determine_which_operation(the_input)['ABS_VAL']:
            first_abs = self.determine_which_operation(the_input)['ABS_VAL'][0]
            second_abs = self.determine_which_operation(the_input)['ABS_VAL'][1]
            inside = float("".join(the_input[first_abs+1:second_abs]))
            inside = (inside**2)**0.5
            the_input = self.replace_list(the_input, inside, [first_abs, second_abs])
        return the_input


    # evaluates paranthesis, including nested ones
    def paran_calc(self, the_input):
        temp_input = ''
        the_input = self.seperate_by_operators(the_input)
        while self.determine_which_operation(the_input)['LPARAN']:
            num_of_nested_lparan, num_of_nested_rparan = -1, -1
            for i in enumerate(the_input[self.determine_which_operation(the_input)
                                        ['LPARAN'][0]:]):
                if i[1] == '(':
                    num_of_nested_lparan += 1
                elif i[1] == ')':
                    num_of_nested_rparan += 1
                elif len(the_input)-1-i[0] == self.determine_which_operation(
                                                the_input)['LPARAN'][0]:
                    while num_of_nested_lparan != num_of_nested_rparan:
                        the_input.append(')')
                        num_of_nested_rparan += 1

                if num_of_nested_rparan == num_of_nested_lparan:
                    for z in self.determine_which_operation(the_input)['RPARAN']:
                        if z > self.determine_which_operation(the_input)['LPARAN'][
                                                            num_of_nested_lparan]:
                            right_paran_place = z
                            break

                    temp_input = the_input[self.determine_which_operation(the_input)
                                        ['LPARAN'][num_of_nested_lparan]+1:
                                        right_paran_place]

                    temp_input = self.calculation(temp_input, False)
                    left_paran = self.determine_which_operation(the_input)['LPARAN'] \
                        [num_of_nested_lparan]
                    self.replace_list(the_input, str(temp_input),
                                [left_paran, right_paran_place])
                    break
        return the_input


    # calculates all factorials
    def factorial_calc(self, the_input):
        indexes = self.determine_which_operation(the_input)
        for i in self.determine_which_operation(the_input)['FACTORIAL']:
            num_to_factorial = int(the_input[i-1])
            current_product = 1
            for z in range(1, num_to_factorial+1):
                current_product *= z
            the_input[i-1] = current_product
            del the_input[i]
        return the_input


    # calculates all sine functions
    def sin_calc(self, the_input, change_input=True):
        if not change_input:
            the_input = float(the_input)*self.PI/180
            the_input = the_input - (the_input**3/(3*2)) + \
                (the_input**5/(5*4*3*2)) - (the_input**7/(7*6*5*4*3*2)) + \
                (the_input**9/(9*8*7*6*5*4*3*2)) - \
                (the_input**11/(11*10*9*8*7*6*5*4*3*2)) + \
                (the_input**13/(13*12*11*10*9*8*7*6*5*4*3*2)) - \
                (the_input**15/(15*14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
                (the_input**17/(17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
            the_input = round(the_input, 10)
            return the_input

        indexes = self.determine_which_operation(the_input)
        while indexes['SIN']:
            for i in indexes['SIN']:
                answer = float(the_input[i+1])*PI/180
                answer = answer - (answer**3/(3*2)) + (answer**5/(5*4*3*2)) - \
                    (answer**7/(7*6*5*4*3*2)) + (answer**9/(9*8*7*6*5*4*3*2)) \
                    - (answer**11/(11*10*9*8*7*6*5*4*3*2)) + \
                    (answer**13/(13*12*11*10*9*8*7*6*5*4*3*2)) - \
                    (answer**15/(15*14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
                    (answer**17/(17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
                answer = round(answer, 10)
                the_input[i+1] = answer
                del the_input[i]
                indexes = self.determine_which_operation(the_input)
        return the_input


    # calculates all cosine functions
    def cos_calc(self, the_input, change_input=True):
        if not change_input:
            answer = float(the_input)*PI/180
            answer = 1 - (answer**2/(2)) + (answer**4/(4*3*2)) - (
                answer**6/(6*5*4*3*2)) + (answer**8/(8*7*6*5*4*3*2)) - \
                (answer**10/(10*9*8*7*6*5*4*3*2)) + \
                (answer**12/(12*11*10*9*8*7*6*5*4*3*2)) - \
                (answer**14/(14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
                (answer**16/(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
            answer = round(answer, 10)
            return answer

        indexes = self.determine_which_operation(the_input)
        while indexes['COS']:
            for i in indexes['COS']:
                answer = float(the_input[i+1])*self.PI/180
                answer = 1 - (answer**2/(2)) + (answer**4/(4*3*2)) - \
                    (answer**6/(6*5*4*3*2)) + (answer**8/(8*7*6*5*4*3*2)) - \
                    (answer**10/(10*9*8*7*6*5*4*3*2)) + \
                    (answer**12/(12*11*10*9*8*7*6*5*4*3*2)) - \
                    (answer**14/(14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
                    (answer**16/(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
                answer = round(answer, 10)
                the_input[i+1] = answer
                del the_input[i]
                indexes = self.determine_which_operation(the_input)
        return the_input


    # calculates all tangent functions
    def tan_calc(self, the_input, change_input=True):
        if not change_input:
            answer = self.sin_calc(the_input, change_input=False) / \
                self.cos_calc(the_input, change_input=False)
            answer = round(answer, 10)
            return answer
        indexes = self.determine_which_operation(the_input)
        while indexes['TAN']:
            for i in indexes['TAN']:
                answer = self.sin_calc(float(the_input[i+1]), change_input=False) / \
                    self.cos_calc(float(the_input[i+1]), change_input=False)
                the_input[i+1] = answer
                del the_input[i]
                indexes = self.determine_which_operation(the_input)
        return the_input


    # calculates all logs (base 10 only)
    def log_calc(self, the_input):
        indexes = self.determine_which_operation(the_input)

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
                answer = find_log(float(the_input[i+1]))
                the_input[i+1] = answer
                del the_input[i]
                indexes = self.determine_which_operation(the_input)
        return the_input


    # calculates square roots
    def square_root_calc(self, the_input):
        indexes = self.determine_which_operation(the_input)
        while indexes['SQUARE_ROOT']:
            if indexes['RPARAN']:
                end_of_sqroot = [x for x in indexes['RPARAN']
                                if x > indexes['SQUARE_ROOT'][0]][0]
                temp_output = the_input[indexes['SQUARE_ROOT'][0]+1:end_of_sqroot]
                del the_input[indexes['SQUARE_ROOT'][0]:end_of_sqroot+1]
            else:
                temp_output = the_input[indexes['SQUARE_ROOT'][0]+1::]
                del the_input[indexes['SQUARE_ROOT'][0]::]
            temp_output = float(self.calculation(temp_output, False))**0.5
            the_input.insert(indexes['SQUARE_ROOT'][0], temp_output)
            indexes = self.determine_which_operation(the_input)
        return the_input


    # calculates all exponent operations
    def exponent_calc(self, the_input):
        while self.determine_which_operation(the_input)['EXPONENT']:
            the_input, indexes = \
                self.emda_calc_and_substitute(the_input, 'EXPONENT', -1, '^')
        return the_input


    def multiplication_calc(self, the_input):
        while self.determine_which_operation(the_input)['MULTIPLY']:
            the_input, indexes = \
                self.emda_calc_and_substitute(the_input, 'MULTIPLY', 0, '*')
        return the_input


    def division_calc(self, the_input):
        while self.determine_which_operation(the_input)['DIVIDE']:
            the_input, indexes = \
                self.emda_calc_and_substitute(the_input, 'DIVIDE', 0, '/')
        return the_input


    def addition_subtraction_calc(self, the_input):
        while self.determine_which_operation(the_input)['ADD']:
            the_input, indexes = self.emda_calc_and_substitute(the_input, 'ADD', 0, '+')
        return the_input


    # calls all functions in proper order
    def calculation(self, the_input, print_bool=True):
        the_input = self.stage('Input Correction Output: ',
                        clean_input, the_input, print_bool)
        the_input = self.stage('Absolute Value Output: ',
                        self.abs_val_calc, the_input, print_bool)
        the_input = self.stage('Paranthesis Output: ',
                        self.paran_calc, the_input, print_bool)
        the_input = self.stage('Factorial Output: ',
                        self.factorial_calc, the_input, print_bool)
        the_input = self.stage('Sine Output: ', self.sin_calc, the_input, print_bool)
        the_input = self.stage('Cosine Output: ', self.cos_calc, the_input, print_bool)
        the_input = self.stage('Tangent Output: ', self.tan_calc, the_input, print_bool)
        the_input = self.stage('Logarithm Output: ', self.log_calc, the_input, print_bool)
        the_input = self.stage('Square Root Output: ',
                        self.square_root_calc, the_input, print_bool)
        the_input = self.stage('Exponent Output: ',
                        self.exponent_calc, the_input, print_bool)
        the_input = self.stage('Multiplication Output: ',
                        self.multiplication_calc, the_input, print_bool)
        the_input = self.stage('Division Output: ',
                        self.division_calc, the_input, print_bool)
        the_input = self.stage('Addition/Subtraction Output: ',
                        self.addition_subtraction_calc, the_input, print_bool)

        if float(the_input[0]) % 1 == 0:
            the_input = int(float(the_input[0]))
        else:
            the_input = float(the_input[0])
        return the_input


# main function, thats called when it is the file opened.
def main():
        import time
        user_input = input('Please give me an expression to evaluate: ')
        while user_input != '':
            time_start = time.time()
            main_calculator = Calculator()
            the_output = main_calculator.calculation(user_input)
            print('\nthe final output as a decimal: ',
                  round(float(the_output), 10))
            print('The final output as a fraction: ',
                  fractions.Fraction(the_output).limit_denominator())

            time_end = time.time()

            print('It took ', round((time_end-time_start)*100000, 2),
                  'microseconds for the program to run!\n\n\n\n')
            user_input = input('Please give me an expression to evaluate: ')

if __name__ == '__main__':
    main()

# two paranthesis () causes an error, so in my new way of abs_val,
    # so would ||-2|+2|

# implement a universal "which one first" functoin so i can seperate m and d,
# and use it for all functions, and then abs val and parans
# seperate multiplication and division
