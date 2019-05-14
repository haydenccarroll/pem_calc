import re
import calculation
import time

class VariableSolver:
    def __init__(self, input_string):
        regex_correction_for_input = calculation.Evaluator(input_string)
        self.input_str   = ''.join(regex_correction_for_input.regex_correction(input_string))
        
    def split_input_str_into_list(self, input_string):  #is never used
        return re.split(r'(\+)', ''.join(input_string))

    def simplify_variable_term_exponents_into_multiplication(self, input_string): #doesnt work i dont think. It does for each term it should do for str
        while True: # executes until there is an error
            try:
                the_search = re.search(r'([a-zA-Z]?)(\^)(\d+)', input_string)
                the_result = the_search.group(1)*int(the_search.group(3))
                input_string = input_string.replace(the_search.group(0), the_result)
            except AttributeError:
                break
        return input_string  
    
    def variable_term_into_exponents(self, term): #make it work with a string not an individual term
        term = self.simplify_variable_term_exponents_into_multiplication(term) # converts everything to multiplication form first, because a specific formaat is needed for vars_into_exponents to wrok

        dict_of_var_indexes = dict()
    
        for i in enumerate(term): # creates dict
            if i[1].isalpha():
                dict_of_var_indexes[i[1]] = dict_of_var_indexes.get(i[1], [])
                dict_of_var_indexes[i[1]].append(i[0])
    
        for key in dict_of_var_indexes.keys(): # creates exponents
            power = len(dict_of_var_indexes[key])
            exponent = '%s^(%s)'%(key, power)
            term = term.replace(key, '', power-1)
            term = term.replace(key, exponent)
        return term
    
    
        
    def regex_correction_for_terms(self, input_string):
        input_regex_correction = calculation.Evaluator(input_string)
        input_string = ''.join(input_regex_correction.regex_correction(input_string))

        input_list = re.split(r'(\+)', input_string)
        new_input = []
        
        for term in input_list:
            new_input += self.simplify_variable_term_exponents_into_multiplication(term)
            
        input_string = ''.join(new_input)
        return input_string
        
    def get_rid_of_useless_multi(self, input_string):
        input_list = re.split(r'(\+)', input_string)
        i = 0
        terms = [x  for x in input_list if len(x) >= 1]
        for term in terms:    #  gets rid of unnecessary multiplication and adds 1s
            term = term.replace('**', '*')
            if term[0] == '*':
                term = term[1:]
            if term[-1] == '*':
                term = term[:-1]
            if term[0].isalpha():
                term = '1*'+term
            input_list[i] = term
            i += 1
            
        input_string = ''.join(input_list)
        return input_string

    def create_dict_of_vars_to_indexes(self, input_string, *no_duplicates):
        input_list = re.split(r'(\+)', input_string)
        dict_of_indexes_of_vars = dict()
        
        for i in enumerate(input_list):       
            var_name = []    
            inner_index = []             
            for y,z in enumerate(i[1]):                          
                if z.isalpha():
                    var_name.append(z)
                    inner_index.append(y)
                
            var_name = ''.join(sorted(var_name)) # creates the variable name, by getting all of the letters in a row, and ordering them alphabetically. it really isnt a variable name, it is just a list of consecutive vars. useful for addition tho
            if ''.join(var_name).isalpha(): # if there is a variable name
                dict_of_indexes_of_vars[var_name] = dict_of_indexes_of_vars.get(var_name, []) # if there is a value it equals itself, if there inst one it creates an empty list to append to                                  
                dict_of_indexes_of_vars[var_name].append([i[0], inner_index]) # appends to the list, with the term index, as well as the index in said term. 
        
        if no_duplicates:
            list_to_del = []
            for k,v in dict_of_indexes_of_vars.items():
                if len(v) <= 1:
                    list_to_del.append(k)
        
            for i in list_to_del:
                dict_of_indexes_of_vars.pop(i)
            return dict_of_indexes_of_vars
        return dict_of_indexes_of_vars


    def parsing(self, input_string):
        # Put the for below in a while

        run_loop, times_ran = True, 0
        while run_loop:
            dict_of_indexes_of_vars = self.create_dict_of_vars_to_indexes(input_string)
            
            for key, val in self.create_dict_of_vars_to_indexes(input_string, True).items():
                temp_input = re.split(r'(\+)', input_string)
                temp_input_calc_obj = calculation.Evaluator(temp_input)
            
                temp_input_left_num = re.sub(r'[a-zA-Z]+', '1', temp_input[val[0][0]])
                #temp_inpt_left_num = "".join(gets_rid_of_useless_multiplication(temp_inpt_left_num))
                temp_input_left_num = float(temp_input_calc_obj.calculation(temp_input_left_num, False))
            
                temp_input_right_num = re.sub(r'[a-zA-Z]+', '1', temp_input[val[1][0]])
                #temp_inpt_right_num = "".join(gets_rid_of_useless_multiplication(temp_inpt_right_num))
                temp_input_right_num = float(temp_input_calc_obj.calculation(temp_input_right_num, False))
                
                result = temp_input_left_num + temp_input_right_num
                del temp_input[val[1][0]]
                temp_input.append('+%s*%s'%(result, key))
                del temp_input[val[0][0]]
                input_string = ''.join(temp_input)
                    
            
            for key, val in self.create_dict_of_vars_to_indexes(input_string).items(): #simplifies terms even if they don't need to be combined. only runs once
                if len(val) <= 1:
                    run_loop = False
                
                if times_ran == 0 and len(val) == 1:
                    temp_input = re.split(r'(\+)', input_string)
                    temp_input_calc_obj = calculation.Evaluator(temp_input)
                    temp_input_left_num = re.sub(r'[a-zA-Z]+', '1', temp_input[val[0][0]])
                    #temp_inpt_left_num = "".join(gets_rid_of_useless_multiplication(temp_inpt_left_num))
                    result = float(temp_input_calc_obj.calculation(temp_input_left_num, False))
                    
                    temp_input.append('+%s*%s'%(result, key))
                    del temp_input[val[0][0]]
                    input_string = ''.join(temp_input)
            
            dict_of_indexes_of_vars = self.create_dict_of_vars_to_indexes(input_string) 
            
            while input_string.find('++') != -1: #gets rid of useless plus signs
                input_string = input_string.replace('++', '+')              
    
            times_ran += 1
            
        input_list = re.split(r'(\+)', input_string)
        list_to_calculate = []
        for term in input_list:
            if (not [x for x in term if (x.isalpha() or x == '+' or term == '')]) and term: # if there is a non var term, 
                list_to_calculate.append(term) # append
        try:
            if list_to_calculate[-1] == '+':
                del list_to_calculate[-1]
        except IndexError:
            list_to_calculate = ''
        for i in range(len(list_to_calculate))[::-1]:
                list_to_calculate.insert(i, '+')
        list_to_calculate = ''.join(list_to_calculate)
    
        non_var_terms_calc = calculation.Evaluator(list_to_calculate)
        try:
            the_non_var_value = non_var_terms_calc.calculation(list_to_calculate, False)
        except IndexError:
            the_non_var_value = ''

        indexes_of_non_vars = [x[0] for x in enumerate(input_list) if not [i for i in x[1] if i.isalpha() or x[1] == '+']]
    
        for i in indexes_of_non_vars[::-1]:
            del input_list[i]
        
        input_list.append('+%s'%the_non_var_value) 
        input_string = ''.join(input_list)
        return input_string


def main():
    var =  VariableSolver('-3c-4cx+2xxx')
    var.input_str = var.simplify_variable_term_exponents_into_multiplication(var.input_str)
    var.input_str = var.regex_correction_for_terms(var.input_str)
    var.input_str = var.get_rid_of_useless_multi(var.input_str)
    var.input_str = var.parsing(var.input_str)
    print(var.input_str)
    
if __name__ == '__main__': main()

'''
    simplify_variable_term_exponents_into_multiplication doesnt work completely. i believe it does each individual term, but it should accept whole string
    
    AS FAR AS INPUT GOES IN THE FUTURE:
        EXPONENTS NEED TO BE IN PARANTHESIS, SO IT DOES NOT SPLIT ON PLUSSES


    I BELIEVE IT IS MOSTLY FUNCTOINAL
    
    2/x simplifies to 2x this is not correct obviously

    simplifying variable terms into exponents does NOT work as of 3:53 5/2/19

    try (3+2)y
        it splits on pluses, but it really should only split if there are NO UNresolved parans
    
'''
