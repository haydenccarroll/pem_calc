# pem_calc
This is a fully-functional calculator created in Python 3 with tkinter. it has no modules, besides tkinter and re. All mathematical operations is done in calculation.py, while the "input cleaner" tasks are completed in calc_input_cleaner.py. Below is a list and description of all the functions in the Calculation class.

init(self, user_input)
    This function is the builtin init, and takes in user input. Besides this, it creates some object variables that are used in other functions. The following variables are self.input, (which is the list of characters that gets calculated on), self.message_functs, (a 2d list with function names and output message strings that is used for self.calculation()), self.PI (a constant that gets used particularly in trig functions), and a dictionary of operators that correlate to their symbol such as "MULTIPLY": "*".
    
replace_with_value(self, replacement, indexes_to_replace)
    A function that takes in a replacement such as 2.0 to replace certain indexes in the list, self.input. For example, if replacement is 2.0, indexes_to_replace is [0,2], and self.input is ['1', '+', '1'], then self.input would be changed to [2.0]. This is used in the calculation functions, to replace the input with output. 
    
seperate_by_operators(self)
    A function that takes self.input, and seperates it by the different operators including +,^,|, and many others. For example, if self.input is ['1, '1', '+', '1', '1'], then self.input gets mutated to ['11', '+', '11']
    
 refresh operator_indexes(self)
    A function that updates self.operator_indexes, a dictionary of operator names to a list of occurances of that operator. Example: {'MULTIPLY': [1], "DIVISION": [3, 5], "ADDITION": []...} if self.input is '2*3/5/10'
    
emda_calc_and_substitute(self, operator_index, index_in_operator_index, operator)
    A function that performs operations on binary operators, such as /, *, +, and ^. It takes in the name of the operator to use in the self.operator_indexes dictionary, and the index in the list of operators from that dictionary, as well as the operator symbol. 
    

def stage(self, message, function, print_bool, arg=None)
    A function that takes a message, a function to perform operations on self.input, a boolean of whether or not the results will be printed, and potential arguments to said functions. This function prints the message, does the function on self.input, and prints the output if the print_bool is True, and does the operations without printing anything if print_bool is False.
    
