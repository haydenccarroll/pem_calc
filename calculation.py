'at line 66 figure out why re.split has random "" no space characters, and why the code below it is necessary. '
'shorten regex correction, as it is messsy'
'use more useful method names. instead of redefine_output have split_inp_into_list or soemthing'
'change emda_calc_and_substitute to a better name like multi_divi_add_calc or something'
'stop using inp, start using something more descriptive. inpt is still bad as well'
'clean up abs val as much as possible'
'also paran_calc'
'stop using if condition: statement and start putting statement on new line for readability'
'dont return "Undefined" return None False or something similar'
'for whatever reason i cant convert to an int  if its a str and a float. check 322 for confirmation'
'use more white space'


'for order of operatoin function do what i did with the trig functs and make optional keywords'
import re
import fractions
class Evaluator(): # the evaluator class
    def __init__(self, user_input): # initializes some important variables

        self.user_input = list(user_input)
        self.DICT_OF_OPERATOR_NAMES = { '*': 'MULTIPLY',
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
        self.PI = 3.1415926535897932384626433832795


    def regex_correction(self, inp): # corrects the regex, due to user input

        inp = "".join(inp).replace('√', '&')
        inp = inp.replace('log', '@')
        inp = inp.replace('sin', '#')
        inp = inp.replace('cos', '`')
        inp = inp.replace('tan', '_')
        inp = re.sub(r'(\^)([^(+]+)', '^(\g<2>)', inp)
        
        def define_lists(inp): # defines the list for error correction in regex

            def re_list_generator(regexes, inp): # function for creating regex lists
                new_regex_list = []
                for regex in regexes:
                    new_regex_list.append([x.start(0) for x in re.finditer(regex, "".join([str(x) for x in inp]))][::-1])
                return new_regex_list
                
            inp = "".join([str(x) for x in inp])
            re_1_list = re_list_generator([r'[^\w\+\)\d\|]\+', 
                                           r'[\)\d\π][\(\&\π\@\#\`\_]', 
                                           r'[\)\π\!][\d\(\π]', r'[\d\)]-', 
                                           r'\+[\-]*\+', r' ',
                                          r'^\+', 
                                          r'(\-[^1])|(\-$)', 
                                          r'\&\(', r'\*$', r'(\d[A-Za-z])|([a-zA-Z]\d)'
                                          , r'^\*'], inp) #if the user has an unecessary addition in situations such as (+2) *+ -+. i need to get rid of the second index of the match, which would be the plus. 
            return re_1_list
        temp_define_list = define_lists(inp)  
        
        def is_nested_list_empty(the_list):
            return all(map(is_nested_list_empty, the_list)) if isinstance(the_list, list) else False
            
        while not is_nested_list_empty(temp_define_list):
            inp = list(inp)
            re1, re2, re3, re4, re5, re6, re7, re8, re9, re10, re11, re12 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
            temp_define_list = define_lists(inp)  
            for i in temp_define_list[re8]:
                del inp[i]
                inp.insert(i, '+-1*')
                inp = list("".join([str(x) for x in inp]))
                temp_define_list = define_lists(inp)
            for i in temp_define_list[re6]: del inp[i]
            temp_define_list = define_lists(inp)   
            for i in temp_define_list[re2]: inp.insert(i+1, '*')
            temp_define_list = define_lists(inp)   
            for i in temp_define_list[re3]: inp.insert(i+1, '*')
            temp_define_list = define_lists(inp)   
            for i in temp_define_list[re1]: del inp[i+1]
            temp_define_list = define_lists(inp)  
            for i in temp_define_list[re5]: del inp[i]
            for i in temp_define_list[re4]: inp.insert(i+1, '+')
            temp_define_list = define_lists(inp)  
            for i in temp_define_list[re7]: del inp[i]
            temp_define_list = define_lists(inp)  
            for i in temp_define_list[re9]: del inp[i+1]
            for i in temp_define_list[re10]: del inp[i]
            for i in temp_define_list[re11]: inp.insert(i+1, '*')
            for i in temp_define_list[re12]: del inp[i]
        inp = list("".join(inp).replace('π', str(self.PI)))
        return inp

    def seperate_by_operators(self, inp): # redefines the output as a list and uses a regex to do this
        inp = re.split(r'([+*^\/()\|\&\!\@\#\`\_])', "".join([str(x) for x in inp]))
        for x in inp:
            if x == '': del inp[inp.index(x)]
        return inp

    def determine_which_operation(self, inpt): # determines the index of certain operations, and returns a list. this is called multiple times throughout the various functions
        def get_indexes(inp, symbol): 
            return [int(i) for i, x in enumerate(inp) if x == symbol]
        
        indexes_of_operators = {self.DICT_OF_OPERATOR_NAMES[symbol]: get_indexes(inpt, symbol) for symbol in r"*/+()^|&!@#`_"}
        return indexes_of_operators

    def abs_val_calc(self, inp): # calculates all absolute values
        while self.determine_which_operation(inp)['ABS_VAL']:
            z = 0
            absolute_value_checker = self.determine_which_operation(inp)['ABS_VAL']
            for i in self.determine_which_operation(inp)['ABS_VAL']:
                z += 1
                if z % 2 != 0:
                    first_index = i
                    if inp[i+1] == '+':
                        del inp[i+1]
                        absolute_value_checker = self.determine_which_operation(inp)['ABS_VAL']
                        break
                    if inp[first_index-1] in [0,1,2,3,4,5,6,7,8,9,')','0','1','2','3','4','5','6','7','8','9'] and first_index != 0:
                        inp.insert(first_index, '*')
                        absolute_value_checker = self.determine_which_operation(inp)['ABS_VAL']
                        break
                elif z % 2 == 0:
                    second_index = i
                    temp_inp = inp[first_index+1:second_index]
                    new_temp_inp = (float(self.calculation(temp_inp, False))**2)**0.5
                    if second_index+1 == len(inp):
                        pass
                    elif inp[second_index+1] in [0,1,2,3,4,5,6,7,8,9,')','0','1','2','3','4','5','6','7','8','9']:
                        inp.insert(second_index+1, '*')
                        absolute_value_checker = self.determine_which_operation(inp)['ABS_VAL']
                        break
                    del inp[first_index:second_index+1]
                    inp.insert(first_index, new_temp_inp)
                    break
        return inp

    def paran_calc(self, inp): # calculates all stuff in the parans. If there are parans in a paran, it calls itself, via calling the calculation method
        temp_input = ''
        inp = self.seperate_by_operators(inp)
        while self.determine_which_operation(inp)['LPARAN']:
            num_of_nested_lparan, num_of_nested_rparan = -1,-1
            for i in enumerate(inp[self.determine_which_operation(inp)['LPARAN'][0]:]):
                if i[1] == '(': num_of_nested_lparan += 1
                elif i[1] == ')': num_of_nested_rparan += 1
                elif len(inp)-1-i[0] == self.determine_which_operation(inp)['LPARAN'][0]: #make this in a loop so it doesnt just do one paranthesis and can do sin(tan(34
                    while num_of_nested_lparan != num_of_nested_rparan:
                        inp.append(')')
                        num_of_nested_rparan += 1
                if num_of_nested_rparan == num_of_nested_lparan:
                    for z in self.determine_which_operation(inp)['RPARAN']:
                        if z > self.determine_which_operation(inp)['LPARAN'][num_of_nested_lparan]:
                            right_paran_place = z
                            break
                        
                    temp_input = inp[self.determine_which_operation(inp)['LPARAN'][num_of_nested_lparan]+1:right_paran_place]
                    temp_input = self.calculation(temp_input, False)
                    del_list = [x for x in range(self.determine_which_operation(inp)['LPARAN'][num_of_nested_lparan], right_paran_place+1)]
                    del_list.reverse()
                    pos_to_insert = self.determine_which_operation(inp)['LPARAN'][num_of_nested_lparan]
                    for i in del_list: del inp[i]
                    inp.insert(pos_to_insert, str(temp_input))
                    break
        return inp

    def factorial_calc(self, inp):
        indexes = self.determine_which_operation(inp)
        for i in self.determine_which_operation(inp)['FACTORIAL']:
            num_to_factorial = int(inp[i-1])
            current_product = 1
            for z in range(1,num_to_factorial+1):
                current_product *= z
            inp[i-1] = current_product
            del inp[i]
        return inp

    def sin_calc(self, inp, change_input=True):
        
        if not change_input:
            inp = float(inp)*self.PI/180
            inp = inp - (inp**3/(3*2)) + (inp**5/(5*4*3*2)) - (inp**7/(7*6*5*4*3*2)) + (inp**9/(9*8*7*6*5*4*3*2)) - (inp**11/(11*10*9*8*7*6*5*4*3*2)) + (inp**13/(13*12*11*10*9*8*7*6*5*4*3*2)) - (inp**15/(15*14*13*12*11*10*9*8*7*6*5*4*3*2)) + (inp**17/(17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
            inp = round(inp, 10)
            return inp
        
        indexes = self.determine_which_operation(inp)
        while indexes['SIN']:
           for i in indexes['SIN']:
               answer = float(inp[i+1])*self.PI/180
               answer = answer - (answer**3/(3*2)) + (answer**5/(5*4*3*2)) - (answer**7/(7*6*5*4*3*2)) + (answer**9/(9*8*7*6*5*4*3*2)) - (answer**11/(11*10*9*8*7*6*5*4*3*2)) + (answer**13/(13*12*11*10*9*8*7*6*5*4*3*2)) - (answer**15/(15*14*13*12*11*10*9*8*7*6*5*4*3*2)) + (answer**17/(17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
               answer = round(answer, 10)
               inp[i+1] = answer
               del inp[i]
               indexes = self.determine_which_operation(inp)
        
        return inp

    def cos_calc(self, inp, change_input=True):
       
        if  not change_input:
            answer = float(inp)*self.PI/180
            answer = 1 - (answer**2/(2)) + (answer**4/(4*3*2)) - (answer**6/(6*5*4*3*2)) + (answer**8/(8*7*6*5*4*3*2))  - (answer**10/(10*9*8*7*6*5*4*3*2)) + (answer**12/(12*11*10*9*8*7*6*5*4*3*2)) - (answer**14/(14*13*12*11*10*9*8*7*6*5*4*3*2)) + (answer**16/(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
            answer = round(answer, 10)
            return answer
         
        indexes = self.determine_which_operation(inp)
        while indexes['COS']:
           for i in indexes['COS']:
               answer = float(inp[i+1])*self.PI/180
               answer = 1 - (answer**2/(2)) + (answer**4/(4*3*2)) - (answer**6/(6*5*4*3*2)) + (answer**8/(8*7*6*5*4*3*2))  - (answer**10/(10*9*8*7*6*5*4*3*2)) + (answer**12/(12*11*10*9*8*7*6*5*4*3*2)) - (answer**14/(14*13*12*11*10*9*8*7*6*5*4*3*2)) + (answer**16/(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
               answer = round(answer, 10)
               inp[i+1] = answer
               del inp[i]
               indexes = self.determine_which_operation(inp)

         
        return inp

    def tan_calc(self, inp, change_input=True):

        if not change_input:
            answer = self.sin_calc(inp, change_input=False)/self.cos_calc(inp, change_input=False)
            answer = round(answer, 10)
            return answer

        indexes = self.determine_which_operation(inp)
        while indexes['TAN']:
           for i in indexes['TAN']:
               answer = self.sin_calc(float(inp[i+1]), change_input=False)/self.cos_calc(float(inp[i+1]), change_input=False)
               inp[i+1] = answer
               del inp[i]
               indexes = self.determine_which_operation(inp)
        
        return inp 

    def log_calc(self, inp):
        indexes = self.determine_which_operation(inp)
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
                    if gone_higher == True:
                        guess_log += 0.25/z
                    else: 
                        guess_log += 1
                z+=1.5
            return 'Undefined'
        while indexes['LOG']:
           for i in indexes['LOG']:
               answer = find_log(float(inp[i+1]))
               inp[i+1] = answer
               del inp[i]
               indexes = self.determine_which_operation(inp)
        return inp

    def square_root_calc(self, inp):
        indexes = self.determine_which_operation(inp)
        while indexes['SQUARE_ROOT']:
            if indexes['RPARAN']: 
                end_of_sqroot = [x for x in indexes['RPARAN'] if x > indexes['SQUARE_ROOT'][0]][0]
                temp_output = inp[indexes['SQUARE_ROOT'][0]+1:end_of_sqroot]
                del inp[indexes['SQUARE_ROOT'][0]:end_of_sqroot+1]
            else: 
                temp_output = inp[indexes['SQUARE_ROOT'][0]+1::]
                del inp[indexes['SQUARE_ROOT'][0]::]
            temp_output = float(self.calculation(temp_output, False))**0.5
            inp.insert(indexes['SQUARE_ROOT'][0], temp_output)
            indexes = self.determine_which_operation(inp)
        return inp

    def exponent_calc(self, inp): # calculates all exponent operations, including sqroot (&)
        while self.determine_which_operation(inp)['EXPONENT']: 
            inp, indexes = self.emda_calc_and_substitute(inp, 'EXPONENT', -1, '^')
        return inp

    def multiplication_division_calc(self, inp):  # calculates multiplication and division, in whatever order pops up first
        indexes = self.determine_which_operation(inp)
        while self.determine_which_operation(inp)['MULTIPLY'] or self.determine_which_operation(inp)['DIVIDE']:
            if indexes['MULTIPLY']:
                if indexes['DIVIDE']:
                    if indexes['MULTIPLY'][0] < indexes['DIVIDE'][0]: inp, indexes = self.emda_calc_and_substitute(inp, 'MULTIPLY', 0, '*')
                    else: inp, indexes = self.emda_calc_and_substitute(inp, 'DIVIDE', 0, '/')
                else: inp, indexes = self.emda_calc_and_substitute(inp, 'MULTIPLY', 0, '*')
            elif indexes['DIVIDE']: inp, indexes = self.emda_calc_and_substitute(inp, 'DIVIDE', 0, '/')
        return inp

    def addition_subtraction_calc(self, inp):
        while self.determine_which_operation(inp)['ADD']: inp, indexes = self.emda_calc_and_substitute(inp, 'ADD', 0, '+')
        return inp


    def emda_calc_and_substitute(self, inp, operator_index, index_in_operator_index, operator): # carries out operations, and then deletes values, and adds values. S
        
        indexes = self.determine_which_operation(inp)
        if operator == '^': 
            temp_output = float(inp[indexes[operator_index][index_in_operator_index]-1])**float(inp[indexes[operator_index][index_in_operator_index]+1])
        elif operator == '*': 
            temp_output = float(inp[indexes[operator_index][index_in_operator_index]-1])*float(inp[indexes[operator_index][index_in_operator_index]+1])
        elif operator == '/': 
            temp_output = float(inp[indexes[operator_index][index_in_operator_index]-1])/float(inp[indexes[operator_index][index_in_operator_index]+1])
        elif operator == '+':
            temp_output = float(inp[indexes[operator_index][index_in_operator_index]-1])+float(inp[indexes[operator_index][index_in_operator_index]+1])

            
    
        del inp[indexes[operator_index][index_in_operator_index]+1]
        del inp[indexes[operator_index][index_in_operator_index]]
        del inp[indexes[operator_index][index_in_operator_index]-1]
        inp.insert(indexes[operator_index][index_in_operator_index]-1, temp_output)
        indexes = self.determine_which_operation(inp)
        return inp, indexes
        
    def emda_calc_revised(self, inp, operator, operator_index):
        indexes = self.determine_which_operation(inp)
        try: 
            left_num = float(inp[operator_index-1])
            right_num = float(inp[operator_index+1])
        except ValueError:
            # either left num or right num is a variable (cant convert str to float)
            pass
        if operator == '^': 
            temp_output = float(inp[operator_index-1])**float(inp[operator_index+1])
        elif operator == '*': 
            temp_output = float(inp[operator_index-1])**float(inp[operator_index+1])
        elif operator == '/': 
            temp_output = float(inp[operator_index-1])**float(inp[operator_index+1])
        elif operator == '+':
            temp_output = float(inp[operator_index-1])**float(inp[operator_index+1])


        del inp[operator_index+1]
        del inp[operator_index]
        del inp[operator_index-1]
        inp.insert(operator_index-1, temp_output)
        indexes = self.determine_which_operation(inp)
        return inp, indexes
        return inp, indexes
    
    

    

    def calculation(self, inp, print_bool): # the basic calculation function, which calls the functions necessary to calculation in the correct order

        def stage(message, function, inp, print_bool): 

            inp = list(inp)
            inp = self.seperate_by_operators(inp)
            inp = function(inp)

            if print_bool == True:
                print(message, "".join([str(x) for x in inp]))
                return inp
            return inp
        
        inp = self.regex_correction(inp)

        inp = stage('Absolute Value Output: ', self.abs_val_calc, inp, print_bool)
        inp = stage('Paranthesis Output: ', self.paran_calc, inp, print_bool)
        inp = stage('Factorial Output: ', self.factorial_calc, inp, print_bool)
        inp = stage('Sin Output: ', self.sin_calc, inp, print_bool)
        inp = stage('Cos Output: ', self.cos_calc, inp, print_bool)
        inp = stage('Tan Output: ', self.tan_calc, inp, print_bool)
        inp = stage('Log Output: ', self.log_calc, inp, print_bool)
        inp = stage('Square Root Output: ', self.square_root_calc, inp, print_bool)
        inp = stage('Exponent Output: ', self.exponent_calc, inp, print_bool)
        inp = stage('Multiplication/Division Output: ', self.multiplication_division_calc, inp, print_bool)
        inp = stage('Addition/Subtraction Output: ', self.addition_subtraction_calc, inp, print_bool)
        
        if float(inp[0]) % 1 == 0:
            inp = int(float(inp[0]))
        else:
            inp = float(inp[0])
        return inp

    def decimal_to_fraction(self, inp):
        return fractions.Fraction(inp).limit_denominator()

def main(): # main function, thats called when it is the main file. 

        import time
        user_input = input('Please give me an expression to evaluate: ')

        while user_input != '':
            math_expression_one = Evaluator(user_input)  
            time_start = time.time()

            the_output =  math_expression_one.calculation(math_expression_one.user_input, True)
            print('\nthe final output as a decimal: ', round(float(the_output), 10))
            print('The final output as a fraction: ', fractions.Fraction(the_output).limit_denominator())

            time_end = time.time()

            print('It took ', round((time_end-time_start)*100000, 2), 'microseconds for the program to run!\n\n\n\n')
            user_input = input('Please give me an expression to evaluate: ')
if __name__ == '__main__': main()

'''

when you add variable support, IMPLICIT multiplication needs to be in parenthesis. for example,

3n -->  (3*n)

such that
3n! --> (3*n)! 
    instead of  3*(n!)

but please note that 
'
3*n! --> 3*n! and should NOT get translated to (3*n)!

just entering pi doesnt work

'''
