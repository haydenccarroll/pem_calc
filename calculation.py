import re
import fractions


DICT_OF_OPERATOR_NAMES = {'*': 'MULTIPLY',
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
PI = 3.1415926535897932384626433832795


# creates a 2d list of all occurances for each regex
def define_lists(the_input):
        the_input = "".join([str(x) for x in the_input])
        regex_list = []
        regexes = [r'[^\w\+\)\d\|]\+',
                   r'[\)\d\π][\(\&\π\@\#\`\_]',
                   r'[\)\π\!][\d\(\π]', r'[\d\)]-',
                   r'\+[\-]*\+', r' ',
                   r'^\+',
                   r'(\-[^1])|(\-$)',
                   r'\&\(', r'\*$',
                   r'(\d[A-Za-z])|([a-zA-Z]\d)', r'^\*']
        for regex in regexes:
            regex_list.append([x.start(0) for x in
                               re.finditer(regex, "".join([str(x) for x
                                           in the_input]))][::-1])
        return regex_list


def decimal_to_fraction(self, the_input):
        return fractions.Fraction(the_input).limit_denominator()


# replaces list by consecutive indexes
def replace_list(input_list, replacement_string, indexes_to_replace):
    if type(input_list) != list:
        input_list = list(input_list)
    del input_list[indexes_to_replace[0]:indexes_to_replace[1]+1]
    input_list.insert(indexes_to_replace[0], replacement_string)
    return input_list


def is_nested_list_empty(the_list):
        return all(map(is_nested_list_empty, the_list)) \
               if isinstance(the_list, list) else False


# redefines the output as a list and uses a regex to do this
def seperate_by_operators(the_input):
    the_input = re.split(r'([+*^\/()\|\&\!\@\#\`\_])',
                         "".join([str(x) for x in the_input]))
    for x in the_input:
        if x == '':
            del the_input[the_input.index(x)]
    return the_input


# determines the index of operators, and returns a list
def determine_which_operation(the_input):
    indexes_of_operators = {DICT_OF_OPERATOR_NAMES[symbol]:
                            [int(i) for i, x in enumerate(the_input)
                             if x == symbol] for symbol in r"*/+()^|&!@#`_"}
    return indexes_of_operators


# carries out operations, and then deletes values, and adds values.
def emda_calc_and_substitute(the_input, operator_index,
                             index_in_operator_index, operator):
    indexes = determine_which_operation(the_input)
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
    the_input = replace_list(the_input, temp_output, [left_index, right_index])
    indexes = determine_which_operation(the_input)
    return the_input, indexes


# input function, string, and returns or possibly displays results
def stage(message, function, the_input, print_bool):
        the_input = list(the_input)
        the_input = seperate_by_operators(the_input)
        the_input = function(the_input)
        if print_bool:
            print(message, "".join([str(x) for x in the_input]))
            return the_input
        return the_input


# corrects user input with regex
def regex_correction(the_input):
    # replaces keywords and symbols to other symbols for easy regex parsing
    the_input = "".join(the_input).replace('√', '&')
    the_input = the_input.replace('log', '@')
    the_input = the_input.replace('sin', '#')
    the_input = the_input.replace('cos', '`')
    the_input = the_input.replace('tan', '_')

    temp_define_list = define_lists(the_input)

    while not is_nested_list_empty(temp_define_list):
        the_input = list(the_input)
        re1, re2, re3, re4, re5, re6, re7, re8, re9, re10, re11, re12 = \
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re8]:
            the_input = replace_list(the_input, '+-1*', [i, i])
            the_input = list("".join([str(x) for x in the_input]))
            temp_define_list = define_lists(the_input)
        for i in temp_define_list[re6]:
            del the_input[i]
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re2]:
            the_input.insert(i+1, '*')
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re3]:
            the_input.insert(i+1, '*')
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re1]:
            del the_input[i+1]
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re5]:
            del the_input[i]
        for i in temp_define_list[re4]:
            the_input.insert(i+1, '+')
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re7]:
            del the_input[i]
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re9]:
            del the_input[i+1]
        for i in temp_define_list[re10]:
            del the_input[i]
        for i in temp_define_list[re11]:
            the_input.insert(i+1, '*')
        for i in temp_define_list[re12]:
            del the_input[i]
    the_input = list("".join(the_input).replace('π', str(PI)))
    return the_input


# calculates all absolute values

def add_parens_for_abs_val(the_input):
    characters_inserted = 0
    indexes = determine_which_operation(the_input)["ABS_VAL"]
    for i in range(len(indexes)):
        if i % 2 == 0:
            the_input.insert(indexes[i]+1+characters_inserted, '(')  # makes |(
        else:
            the_input.insert(indexes[i]+characters_inserted, ')')  # makes )|
        characters_inserted += 1
    return the_input


def abs_val_calc(the_input):
    if not determine_which_operation(the_input)['ABS_VAL']:
        return the_input
    the_input = add_parens_for_abs_val(the_input)
    print('194', the_input)
    the_input = paran_calc(the_input)
    print(the_input, 'in abs val calc')
    while determine_which_operation(the_input)['ABS_VAL']:
        first_abs = determine_which_operation(the_input)['ABS_VAL'][0]
        second_abs = determine_which_operation(the_input)['ABS_VAL'][1]
        inside = float("".join(the_input[first_abs+1:second_abs]))
        inside = (inside**2)**0.5
        the_input = replace_list(the_input, inside, [first_abs, second_abs])
    return the_input


# evaluates paranthesis, including nested ones
def paran_calc(the_input):
    temp_input = ''
    the_input = seperate_by_operators(the_input)
    while determine_which_operation(the_input)['LPARAN']:
        num_of_nested_lparan, num_of_nested_rparan = -1, -1
        for i in enumerate(the_input[determine_which_operation(the_input)
                                     ['LPARAN'][0]:]):
            if i[1] == '(':
                num_of_nested_lparan += 1
            elif i[1] == ')':
                num_of_nested_rparan += 1
            elif len(the_input)-1-i[0] == determine_which_operation(
                                            the_input)['LPARAN'][0]:
                while num_of_nested_lparan != num_of_nested_rparan:
                    the_input.append(')')
                    num_of_nested_rparan += 1

            if num_of_nested_rparan == num_of_nested_lparan:
                for z in determine_which_operation(the_input)['RPARAN']:
                    if z > determine_which_operation(the_input)['LPARAN'][
                                                        num_of_nested_lparan]:
                        right_paran_place = z
                        break

                temp_input = the_input[determine_which_operation(the_input)
                                       ['LPARAN'][num_of_nested_lparan]+1:
                                       right_paran_place]

                temp_input = calculation(temp_input, False)
                left_paran = determine_which_operation(the_input)['LPARAN'] \
                    [num_of_nested_lparan]
                replace_list(the_input, str(temp_input),
                             [left_paran, right_paran_place])
                break
    return the_input


# calculates all factorials
def factorial_calc(the_input):
    indexes = determine_which_operation(the_input)
    for i in determine_which_operation(the_input)['FACTORIAL']:
        num_to_factorial = int(the_input[i-1])
        current_product = 1
        for z in range(1, num_to_factorial+1):
            current_product *= z
        the_input[i-1] = current_product
        del the_input[i]
    return the_input


# calculates all sine functions
def sin_calc(the_input, change_input=True):
    if not change_input:
        the_input = float(the_input)*PI/180
        the_input = the_input - (the_input**3/(3*2)) + \
            (the_input**5/(5*4*3*2)) - (the_input**7/(7*6*5*4*3*2)) + \
            (the_input**9/(9*8*7*6*5*4*3*2)) - \
            (the_input**11/(11*10*9*8*7*6*5*4*3*2)) + \
            (the_input**13/(13*12*11*10*9*8*7*6*5*4*3*2)) - \
            (the_input**15/(15*14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
            (the_input**17/(17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
        the_input = round(the_input, 10)
        return the_input

    indexes = determine_which_operation(the_input)
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
            indexes = determine_which_operation(the_input)
    return the_input


# calculates all cosine functions
def cos_calc(the_input, change_input=True):
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

    indexes = determine_which_operation(the_input)
    while indexes['COS']:
        for i in indexes['COS']:
            answer = float(the_input[i+1])*PI/180
            answer = 1 - (answer**2/(2)) + (answer**4/(4*3*2)) - \
                (answer**6/(6*5*4*3*2)) + (answer**8/(8*7*6*5*4*3*2)) - \
                (answer**10/(10*9*8*7*6*5*4*3*2)) + \
                (answer**12/(12*11*10*9*8*7*6*5*4*3*2)) - \
                (answer**14/(14*13*12*11*10*9*8*7*6*5*4*3*2)) + \
                (answer**16/(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
            answer = round(answer, 10)
            the_input[i+1] = answer
            del the_input[i]
            indexes = determine_which_operation(the_input)
    return the_input


# calculates all tangent functions
def tan_calc(the_input, change_input=True):
    if not change_input:
        answer = sin_calc(the_input, change_input=False) / \
            cos_calc(the_input, change_input=False)
        answer = round(answer, 10)
        return answer
    indexes = determine_which_operation(the_input)
    while indexes['TAN']:
        for i in indexes['TAN']:
            answer = sin_calc(float(the_input[i+1]), change_input=False) / \
                cos_calc(float(the_input[i+1]), change_input=False)
            the_input[i+1] = answer
            del the_input[i]
            indexes = determine_which_operation(the_input)
    return the_input


# calculates all logs (base 10 only)
def log_calc(the_input):
    indexes = determine_which_operation(the_input)

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
            indexes = determine_which_operation(the_input)
    return the_input


# calculates square roots
def square_root_calc(the_input):
    indexes = determine_which_operation(the_input)
    while indexes['SQUARE_ROOT']:
        if indexes['RPARAN']:
            end_of_sqroot = [x for x in indexes['RPARAN']
                             if x > indexes['SQUARE_ROOT'][0]][0]
            temp_output = the_input[indexes['SQUARE_ROOT'][0]+1:end_of_sqroot]
            del the_input[indexes['SQUARE_ROOT'][0]:end_of_sqroot+1]
        else:
            temp_output = the_input[indexes['SQUARE_ROOT'][0]+1::]
            del the_input[indexes['SQUARE_ROOT'][0]::]
        temp_output = float(calculation(temp_output, False))**0.5
        the_input.insert(indexes['SQUARE_ROOT'][0], temp_output)
        indexes = determine_which_operation(the_input)
    return the_input


# calculates all exponent operations
def exponent_calc(the_input):
    while determine_which_operation(the_input)['EXPONENT']:
        the_input, indexes = \
            emda_calc_and_substitute(the_input, 'EXPONENT', -1, '^')
    return the_input


def multiplication_calc(the_input):
    while determine_which_operation(the_input)['MULTIPLY']:
        the_input, indexes = \
            emda_calc_and_substitute(the_input, 'MULTIPLY', 0, '*')
    return the_input


def division_calc(the_input):
    while determine_which_operation(the_input)['DIVIDE']:
        the_input, indexes = \
            emda_calc_and_substitute(the_input, 'DIVIDE', 0, '/')
    return the_input


def addition_subtraction_calc(the_input):
    while determine_which_operation(the_input)['ADD']:
        the_input, indexes = emda_calc_and_substitute(the_input, 'ADD', 0, '+')
    return the_input


# calls all functions in proper order
def calculation(the_input, print_bool=True):
    the_input = stage('Input Correction Output: ',
                      regex_correction, the_input, print_bool)
    the_input = stage('Absolute Value Output: ',
                      abs_val_calc, the_input, print_bool)
    the_input = stage('Paranthesis Output: ',
                      paran_calc, the_input, print_bool)
    the_input = stage('Factorial Output: ',
                      factorial_calc, the_input, print_bool)
    the_input = stage('Sine Output: ', sin_calc, the_input, print_bool)
    the_input = stage('Cosine Output: ', cos_calc, the_input, print_bool)
    the_input = stage('Tangent Output: ', tan_calc, the_input, print_bool)
    the_input = stage('Logarithm Output: ', log_calc, the_input, print_bool)
    the_input = stage('Square Root Output: ',
                      square_root_calc, the_input, print_bool)
    the_input = stage('Exponent Output: ',
                      exponent_calc, the_input, print_bool)
    the_input = stage('Multiplication Output: ',
                      multiplication_calc, the_input, print_bool)
    the_input = stage('Division Output: ',
                      division_calc, the_input, print_bool)
    the_input = stage('Addition/Subtraction Output: ',
                      addition_subtraction_calc, the_input, print_bool)

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

            the_output = calculation(user_input)
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
