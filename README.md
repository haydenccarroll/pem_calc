# PFEiMDAS_calculator
This is a fully-functional calculator created in Python 3 with tkinter. it has no modules, besides tkinter and re. All mathematical operations is done in calculation.py, while the "input cleaner" tasks are completed in calc_input_cleaner.py. Below is a list and description of all the functions in the Calculation class.

__init__(self, user_input)
    This function is the builtin __init__, and takes in user input. Besides this, it creates some object variables that are used in other functions. The following variables are self.input, (which is the list of characters that gets calculated on), self.message_functs, (a 2d list with function names and output message strings that is used for self.calculation()), self.PI (a constant that gets used particularly in trig functions), and a dictionary of operators that correlate to their symbol such as "MULTIPLY": "*".
    
replace_list(self, replacement, indexes_to_replace)
    A function that takes in a replacement such as 2.0 to replace certain indexes in the list, self.input. For example, if replacement is 2.0, indexes_to_replace is [0,2], and self.input is ['1', '+', '1'], then self.input would be changed to [2.0]. This is used in the calculation functions, to replace the input with the output. 
    
seperate_by_operators(self)
    A function that takes self.input, and seperates it by the different operators including +,^,|, and many others. For example, if self.input is ['1, '1', '+', '1', '1'], then self.input gets mutated to ['11', '+', '11']
    
 determine_which_operation(self)
    A function that returns a dictionary of operator names to a list of occurances of that operator. Example: {'MULTIPLY': [1], "DIVISION": [3, 5], "ADDITION": []}
