import re
import calculation

inpt = input('Please enter a valid expression: ')


def simplify_variable_term_exponents_into_multiplication(input_string): # this simplifies the variables with exponents to a standard, multiplication form. 
    input_string = "".join(input_string)
    while True: # executes until there is an error
        try:
            the_search = re.search(r'([a-zA-Z]?)(\^)(\d+)', input_string)
            the_result = the_search.group(1)*int(the_search.group(3))
            input_string = input_string.replace(the_search.group(0), the_result)
        except AttributeError:
            break
    return input_string       


def variable_term_into_exponents(term): # this adds exponents onto the variables in terms
    term = simplify_variable_term_exponents_into_multiplication(term) # converts everything to multiplication form first, because a specific formaat is needed for vars_into_exponents to wrok

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


def mini_regex_correction(inpt):
    inpt_regex_correction = calculation.Evaluator(inpt)
    inpt = "".join(inpt_regex_correction.regex_correction(inpt))

    inpt = re.split(r'(\+)', inpt)
    new_inpt = []
    for term in inpt:
        new_inpt += simplify_variable_term_exponents_into_multiplication(term)
    inpt = new_inpt
    return inpt

inpt = mini_regex_correction(inpt)

def gets_rid_of_useless_multiplication(inpt):
    inpt = re.split(r'(\+)', "".join(inpt))
    i = 0
    terms = [x  for x in inpt if len(x) >= 1]
    for term in terms:    #  gets rid of unnecessary multiplication and adds 1s
        term = term.replace('**', '*')
        if term[0] == '*':
            term = term[1:]
        if term[-1] == '*':
            term = term[:-1]
        if term[0].isalpha():
            term = '1*'+term
        inpt[i] = term
        i += 1
    return inpt
inpt = gets_rid_of_useless_multiplication(inpt)

def define_dictionary(inpt):
    inpt = re.split(r'(\+)', "".join(inpt))
    dict_of_indexes_of_vars = {}
    for i in enumerate(inpt):       
        var_name = []    
        inner_index = []             
        for y,z in enumerate(i[1]):                          
            if z.isalpha():
                var_name.append(z)
                inner_index.append(y)
                
        
        var_name = "".join(sorted(var_name)) # creates the variable name, by getting all of the letters in a row, and ordering them alphabetically. it really isnt a variable name, it is just a list of consecutive vars. useful for addition tho
        if "".join(var_name).isalpha(): # if there is a variable name
            dict_of_indexes_of_vars[var_name] = dict_of_indexes_of_vars.get(var_name, []) # if there is a value it equals itself, if there inst one it creates an empty list to append to                                  
            dict_of_indexes_of_vars[var_name].append([i[0], inner_index]) # appends to the list, with the term index, as well as the index in said term. 
    return dict_of_indexes_of_vars

def actual_parsing(inpt):
    inpt = re.split(r'(\+)', "".join(inpt)) # splits into terms
    # Put the for below in a while
    
    '''
        Simplifies two like terms
            - this is not a good method of doing it, because the loop is not correct after one loop. presumably the indexes are messed up because stuff was inserted amnd moved around
    
    
    
        get rid of the while loop
            just use that one for loop
            
        need to make stuff in a for loop until like 129 or something
    '''
    run_loop = True
    times_ran = 0
    while run_loop:
        run_loop = False
        for k, v in define_dictionary(inpt).items():
            if len(v) > 1:
                run_loop = True
        dict_of_indexes_of_vars = define_dictionary(inpt)
        for key, val in dict_of_indexes_of_vars.items():
            if len(val) > 1:
                temp_inpt = inpt
                temp_inpt_calc_obj = calculation.Evaluator(temp_inpt)
                
                print('this is BEFORE the temp_inpt_left_num and temp inpt val 00', temp_inpt[val[0][0]])

                
                temp_inpt_left_num = re.sub(r'[a-zA-Z]+', '1', temp_inpt[val[0][0]])
                #temp_inpt_left_num = "".join(gets_rid_of_useless_multiplication(temp_inpt_left_num))
                print('this is the temp_inpt_left_num and temp inpt val 00', temp_inpt_left_num, temp_inpt[val[0][0]])
                temp_inpt_left_num = float(temp_inpt_calc_obj.calculation(temp_inpt_left_num, False))
            
                temp_inpt_right_num = re.sub(r'[a-zA-Z]+', '1', temp_inpt[val[1][0]])
                #temp_inpt_right_num = "".join(gets_rid_of_useless_multiplication(temp_inpt_right_num))
                temp_inpt_right_num = float(temp_inpt_calc_obj.calculation(temp_inpt_right_num, False))
                
                result = temp_inpt_left_num + temp_inpt_right_num
                index_of_right_variable = val[1]
                del temp_inpt[val[1][0]]

                result = '%s*%s'%(result, key)
                temp_inpt.append('+%s'%result)
                del temp_inpt[val[0][0]]
                inpt = temp_inpt
                

            elif times_ran == 0 and len(val) == 1:
                temp_inpt = inpt
                temp_inpt_calc_obj = calculation.Evaluator(temp_inpt)
                
                temp_inpt_left_num = re.sub(r'[a-zA-Z]+', '1', temp_inpt[val[0][0]])
                #temp_inpt_left_num = "".join(gets_rid_of_useless_multiplication(temp_inpt_left_num))
                
                
                print(temp_inpt_left_num, 'temp inpt left num and temp_inpt at 143', temp_inpt)
                    
                result = float(temp_inpt_calc_obj.calculation(temp_inpt_left_num, False))
                result = '%s*%s'%(result, key)
                temp_inpt.append('+%s'%result)
                del temp_inpt[val[0][0]]
                inpt = temp_inpt
                
                
            dict_of_indexes_of_vars = define_dictionary(inpt)  
        while "".join(inpt).find('++') != -1:
            inpt = "".join(inpt).replace('++', '+')              
        
        inpt = re.split(r'(\+)', "".join(inpt))
        

        times_ran += 1
    print('this is inpt at 157', inpt)
    list_to_calculate = []
    for term in inpt:
        print(term, 'term at 155', 'and input', inpt)
        if (not [x for x in term if (x.isalpha() or x == '+' or term == '')]) and term: # if there is a non var term, 
            list_to_calculate.append(term) # append
    try:
        if list_to_calculate[-1] == '+':
            del list_to_calculate[-1]
        print('list to calculate, ', list_to_calculate)
    except IndexError:
        list_to_calculate = ''
    for i in range(len(list_to_calculate))[::-1]:
            list_to_calculate.insert(i, '+')
    list_to_calculate = "".join(list_to_calculate)
    
    non_var_terms_calc = calculation.Evaluator(list_to_calculate)
    try:
        the_non_var_value = non_var_terms_calc.calculation(list_to_calculate, False)
    except IndexError:
        the_non_var_value = ''
    print(inpt, 'inpt then type(inpt)', type(inpt), 'the non var value', the_non_var_value)
    
    indexes_of_non_vars = [x[0] for x in enumerate(inpt) if not [i for i in x[1] if i.isalpha() or x[1] == '+']]
    
    for i in indexes_of_non_vars[::-1]:
        del inpt[i]
        
    inpt.append('+%s'%the_non_var_value) 
    inpt = "".join(inpt)
    return inpt
inpt = actual_parsing(inpt)
# just pass it to regex correction
#inpt = variable_term_into_exponents(inpt)
#inpt = gets_rid_of_useless_multiplication(inpt)

print('\n\n%s'%inpt)






'''


    try 3x+3c-2x+3c

    2/x simplifies to 2x this is not correct obviously

    simplifying variable terms into exponents does NOT work as of 3:53 5/2/19

    try (3+2)y
        it splits on pluses, but it really should only split if there are NO UNresolved parans
    
'''
