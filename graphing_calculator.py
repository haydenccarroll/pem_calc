'''

set up a server

either password to enter or whitelist, preferably passwword

have an open, create, save, run file button
    when open is clicked, 
        launch file explorer of SERVER files
    when create is clicked,
        launch file explorer of SERVER files (create a file)
        
    when save is clicked, 
        save current file
    
    when run is clicked,
        have server go to that file and run iter
        ? how would output be displayed?
        



'''
import re
def parser(inpt):
    list_inpt = re.split(r'([\+\=])', inpt)
    if ''.join(list_inpt).find('=') != -1:
        equal_index = list_inpt.index('=')
        list_inpt.insert(equal_index+1, '0+')
        list_inpt.insert(equal_index, '+0')
        print(list_inpt)
    
        left_side_list = list_inpt[:equal_index]
        list_to_move_over = left_side_list
        list_to_move_over.insert(0, '-1*(')
        list_to_move_over.append(')')
        
        list_inpt = list_inpt + list_to_move_over
        
        del list_inpt[:equal_index]
        
        print(list_inpt)
        indexes_of_ys = []
        for i in list_inpt:
            if i.find('y') != -1:
                indexes_of_ys.append(list_inpt.index(i))
                
        print(indexes_of_ys)
        
        vals_of_ys = [list_inpt[x] for x in indexes_of_ys]
        print(vals_of_ys)
        vals_of_ys.append(')')
        vals_of_ys.insert(0, '-1*(')
        
        
        for x in indexes_of_ys[::-1]:
            del list_inpt[x]
        
        
        equal_index = list_inpt.index('=')
        
        list_inpt = vals_of_ys + list_inpt
        
        list_inpt_stuff = [list_inpt.index(x) for x in list_inpt][::-1]

        for i in list_inpt_stuff:
            list_inpt.insert(i, '+')
    print(list_inpt)
# needs to add +0 to both sides
parser('3x-3=2y+-1*4y')



    +0 = 2y+-1*4y-(3x-3)
    
    
    -(2y, 4y)

    
    move only if there is no * or / operator in y "term"


    ADD TERM BEFORE like +3


# mainly works, but not completely. how can i ensure the y's symbols are carried with it?

add Error for errors, doing now. 
if you press second the stuff dissapears
1/x should not append 1/, but insert 1/ in the first index
add arc functions
add e
add ln
add commas (just get rid of them in calculation)
add curly braces as parans but they cant go like this {3+3)

from tkinter import *
import calculation
class Window(Frame):
    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.is_second = False

    def create_widgets(self):
        self.master.title(" PFEMDAS Calculator")
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=1)
        self.master.columnconfigure(4, weight=1)
        self.master.columnconfigure(5, weight=1)

        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.rowconfigure(2, weight=1)
        self.master.rowconfigure(3, weight=1)
        self.master.rowconfigure(4, weight=1)
        self.master.rowconfigure(5, weight=1)

        if self.is_second:
            seven = Button(self.master, text = '  A   ', bg = 'gray',fg='white', command=lambda: self.button_command('Z'))
            eight = Button(self.master, text = '  B   ', bg = 'gray',fg='white', command=lambda: self.button_command('Y'))
            nine = Button(self.master, text = '  C   ', bg = 'gray',fg='white', command=lambda: self.button_command('X'))
            four = Button(self.master, text='  D   ', bg = 'gray',fg='white', command=lambda: self.button_command('V'))
            five = Button(self.master, text='  E   ', bg = 'gray',fg='white', command=lambda: self.button_command('U'))
            six = Button(self.master, text='  F   ', bg = 'gray',fg='white', command=lambda: self.button_command('T'))
            one = Button(self.master, text='  G   ', bg = 'gray',fg='white', command=lambda: self.button_command('S'))
            two = Button(self.master, text='  H   ', bg = 'gray',fg='white', command=lambda: self.button_command('R'))
            three = Button(self.master, text='  Q   ', bg = 'gray',fg='white', command=lambda: self.button_command('Q'))
            zero = Button(self.master, text='  |   ', bg = 'gray',fg='white', command=lambda: self.button_command('|'))
            decimal = Button(self.master, text='  ,   ', bg = 'gray',fg='white', command=lambda: self.button_command(','))
            equal = Button(self.master, text='  =   ', bg = 'gray',fg='white', command=lambda: self.refresh_input_box())
            add = Button(self.master, text='  +   ', bg = 'gray',fg='white', command=lambda: self.button_command('+'))
            minus = Button(self.master, text='  -   ', bg = 'gray',fg='white', command=lambda: self.button_command('-'))
            multiplication = Button(self.master, text='  *   ', bg = 'gray',fg='white', command=lambda: self.button_command('*'))
            division = Button(self.master, text='  /   ', bg = 'gray',fg='white', command=lambda: self.button_command('/'))
            left_paran = Button(self.master, text='  {   ', bg = 'gray',fg='white', command=lambda: self.button_command('{'))
            right_paran = Button(self.master, text='  }   ', bg = 'gray',fg='white', command=lambda: self.button_command('}'))
            exponent = Button(self.master, text='  ^   ', bg = 'gray',fg='white', command=lambda: self.button_command('^'))
            sqroot = Button(self.master, text="  \u221A   ", bg = 'gray',fg='white', command=lambda: self.button_command('\u221A('))
            pi = Button(self.master, text='  e  ', bg = 'gray',fg='white', command=lambda: self.button_command('e'))
            factorial = Button(self.master, text='  1/x  ', bg = 'gray',fg='white', command=lambda: self.button_command('1/'))
            sin = Button(self.master, text=' arcsin  ', bg = 'gray',fg='white', command=lambda: self.button_command('arcsin('))
            cos = Button(self.master, text=' arccos  ', bg = 'gray',fg='white', command=lambda: self.button_command('arccos('))
            tan = Button(self.master, text=' arctan  ', bg = 'gray',fg='white', command=lambda: self.button_command('arctan('))
            clear_all = Button(self.master, text='  CE  ', bg = 'gray',fg='white', command=lambda: self.clear_input_box())
            delete = Button(self.master, text=' Del  ', bg = 'gray',fg='white', command=lambda: self.delete_input_box())
            log = Button(self.master, text=' ln   ', bg = 'gray',fg='white', command=lambda: self.button_command('ln('))
            graph = Button(self.master, text=' 2nd  ', bg = 'gray',fg='white', command=lambda: self.inverse_second_var())
            d_to_f = Button(self.master, text='F->D ', bg = 'gray',fg='white', command=lambda: self.refresh_input_box())
        else:
            
            seven = Button(self.master, text = '  7   ', command=lambda: self.button_command('7'))
            eight = Button(self.master, text = '  8   ', command=lambda: self.button_command('8'))
            nine = Button(self.master, text = '  9   ', command=lambda: self.button_command('9'))
            four = Button(self.master, text='  4   ', command=lambda: self.button_command('4'))
            five = Button(self.master, text='  5   ', command=lambda: self.button_command('5'))
            six = Button(self.master, text='  6   ', command=lambda: self.button_command('6'))
            one = Button(self.master, text='  1   ', command=lambda: self.button_command('1'))
            two = Button(self.master, text='  2   ', command=lambda: self.button_command('2'))
            three = Button(self.master, text='  3   ', command=lambda: self.button_command('3'))
            zero = Button(self.master, text='  0   ', command=lambda: self.button_command('0'))
            decimal = Button(self.master, text='  .   ', command=lambda: self.button_command('.'))
            equal = Button(self.master, text='  =   ', command=lambda: self.refresh_input_box())
            add = Button(self.master, text='  +   ', command=lambda: self.button_command('+'))
            minus = Button(self.master, text='  -   ', command=lambda: self.button_command('-'))
            multiplication = Button(self.master, text='  *   ', command=lambda: self.button_command('*'))
            division = Button(self.master, text='  /   ', command=lambda: self.button_command('/'))
            left_paran = Button(self.master, text='  (   ', command=lambda: self.button_command('('))
            right_paran = Button(self.master, text='  )   ', command=lambda: self.button_command(')'))
            exponent = Button(self.master, text='  ^   ', command=lambda: self.button_command('^'))
            sqroot = Button(self.master, text="  \u221A   ", command=lambda: self.button_command('\u221A('))
            pi = Button(self.master, text='  \u03C0  ', command=lambda: self.button_command('\u03C0'))
            factorial = Button(self.master, text='  n!  ', command=lambda: self.button_command('!'))
            sin = Button(self.master, text=' sin  ', command=lambda: self.button_command('sin('))
            cos = Button(self.master, text=' cos  ', command=lambda: self.button_command('cos('))
            tan = Button(self.master, text=' tan  ', command=lambda: self.button_command('tan('))
            clear_all = Button(self.master, text='  CE  ', command=lambda: self.clear_input_box())
            delete = Button(self.master, text=' Del  ', command=lambda: self.delete_input_box())
            log = Button(self.master, text=' log   ', command=lambda: self.button_command('log('))
            graph = Button(self.master, text=' 2nd  ', command=lambda: self.inverse_second_var())
            d_to_f = Button(self.master, text='D->F ', command=lambda: self.d_to_f())
        
        self.input_box = Entry(self.master, font=("Calibri 15"))
        self.input_box.grid(row = 0, column = 0, sticky = 'nesw', columnspan=6)
        seven.grid(row=1, column=0, sticky='nesw')
        eight.grid(row=1, column=1, sticky='nesw')
        nine.grid(row=1, column=2, sticky='nesw')
        four.grid(row=2, column=0, sticky='nesw')
        five.grid(row=2, column=1, sticky='nesw')
        six.grid(row=2, column=2, sticky='nesw')
        one.grid(row=3, column=0, sticky='nesw')
        two.grid(row=3, column=1, sticky='nesw')
        three.grid(row=3, column=2, sticky='nesw')
        zero.grid(row=4, column=0, sticky='nesw')
        decimal.grid(row=4, column=1, sticky='nesw')
        equal.grid(row=4, column=2, sticky='nesw')
        add.grid(row=1, column=3,sticky='nesw')
        minus.grid(row=2, column=3, sticky='nesw')
        multiplication.grid(row=3, column=3, sticky='nesw')
        division.grid(row=4, column=3, sticky='nesw')
        left_paran.grid(row=5, column=0, sticky='nesw')
        right_paran.grid(row=5, column=1, sticky='nesw')
        exponent.grid(row=5, column=2, sticky='nesw')
        sqroot.grid(row=5, column=3, sticky='nesw')
        pi.grid(row=1, column=4, sticky='nesw')
        factorial.grid(row=2, column=4, sticky='nesw')
        sin.grid(row=3, column=4, sticky='nesw')
        cos.grid(row=4, column=4, sticky='nesw')
        tan.grid(row=5, column=4, sticky='nesw')
        clear_all.grid(row=1, column=5, sticky='nesw')
        delete.grid(row=2, column=5, sticky='nesw')
        log.grid(row=3, column=5, sticky='nesw')
        graph.grid(row=4, column=5, sticky='nesw')
        d_to_f.grid(row=5, column=5, sticky='nesw')

    def inverse_second_var(self):
        self.is_second = not self.is_second
        self.create_widgets()

    def refresh_input_box(self):
        result = calculation.Evaluator(self.input_box.get())
        try:
            the_result = result.calculation(self.input_box.get(), False)
        except:
            the_result = 'Error'
        if self.is_second == True:
            self.inverse_second_var()
        self.input_box.delete(0, 'end')
        self.input_box.insert(0, the_result)

    def button_command(self, str_to_append):
        self.input_box.insert('end', str_to_append)
    def clear_input_box(self):
        self.input_box.delete(0, 'end')

    def delete_input_box(self):
        self.input_box.delete(len(self.input_box.get())-1,'end')

    def d_to_f(self):
        result = calculation.Evaluator(self.input_box.get())
        try:
            the_result = result.decimal_to_fraction(self.input_box.get())
        except:
            the_result = 'Error'
        self.input_box.delete(0, 'end')
        self.input_box.insert(0, the_result)
root = Tk()
app = Window(master=root)
app.master.minsize(350,400)
app.master.maxsize(350,400)
app.create_widgets()
app.mainloop()









import re
import fractions
class Evaluator(): # the evaluator class
    def __init__(self, inpt): # initializes some important variables
        self.inpt = list(inpt)
        self.inpt = self.regex_correction(self.inpt)
        self.MULTIPLY_INDEX, self.DIVISION_INDEX,  self.ADDITION_INDEX, self.LPARAN_INDEX, self.RPARAN_INDEX, self.EXPONENT_INDEX, self.ABS_VAL_INDEX, self.SQUARE_ROOT, self.FACTORIAL, self.LOG, self.SIN, self.COS, self.TAN = 0, 1, 2, 3, 4, 5 ,6, 7, 8, 9, 10, 11, 12
    
    def find_sin(self, inp):
        inp = inp*3.1415926535897932384626433832795/180
        inp = inp - (inp**3/(3*2)) + (inp**5/(5*4*3*2)) - (inp**7/(7*6*5*4*3*2)) + (inp**9/(9*8*7*6*5*4*3*2)) - (inp**11/(11*10*9*8*7*6*5*4*3*2)) + (inp**13/(13*12*11*10*9*8*7*6*5*4*3*2)) - (inp**15/(15*14*13*12*11*10*9*8*7*6*5*4*3*2)) + (inp**17/(17*16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
        inp = round(inp, 10)
        return inp

    def find_cos(self, inp):
        inp = inp*3.1415926535897932384626433832795/180
        inp = 1 - (inp**2/(2)) + (inp**4/(4*3*2)) - (inp**6/(6*5*4*3*2)) + (inp**8/(8*7*6*5*4*3*2))  - (inp**10/(10*9*8*7*6*5*4*3*2)) + (inp**12/(12*11*10*9*8*7*6*5*4*3*2)) - (inp**14/(14*13*12*11*10*9*8*7*6*5*4*3*2)) + (inp**16/(16*15*14*13*12*11*10*9*8*7*6*5*4*3*2))
        inp = round(inp, 10)
        return inp

    def find_tan(self, inp):
        inp = find_sin(inp)/find_cos(inp)
        inp = round(inp, 10)
        return inp

    def order_of_operation_function(self, inp, operator_index, index_in_operator_index, operator): # carries out operations, and then deletes values, and adds values. S
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
        
    def determine_which_operation(self, inpt): # determines the index of certain operations, and returns a list. this is called multiple times throughout the various functions
        indexes_of_operators = [[], [], [], [], [], [], [], [], [], [], [], [], []]
        def get_indexes(inp, symbol): return [int(i) for i, x in enumerate(inp) if x == symbol]
        
        indexes_of_operators = [get_indexes(inpt, symbol) for symbol in r"*/+()^|&!@#`_"]
        return indexes_of_operators
    
    def redefine_output(self, inp): # redefines the output as a list and uses a regex to do this
        inp = re.split(r'([+*^\/()\|\&\!\@\#\`\_])', "".join([str(x) for x in inp]))
        for x in inp:
            if x == '': del inp[inp.index(x)]
        return inp
        
    def regex_correction(self, inp): # corrects the regex, due to user input
        inp = "".join(inp).replace('√', '&')
        inp = inp.replace('log', '@')
        inp = inp.replace('sin', '#')
        inp = inp.replace('cos', '`')
        inp = inp.replace('tan', '_')
        inp = list(inp)
        def define_lists(inp): # defines the list for error correction in regex
            def re_list_generator(regex, inp): # function for creating regex lists
                return [x.start(0) for x in re.finditer(regex, "".join([str(x) for x in inp]))]
            inp = "".join([str(x) for x in inp])
            re_1_list = re_list_generator(r'[^\+\)\d\|]\+', inp) #if the user has an unecessary addition in situations such as (+2) *+ -+. i need to get rid of the second index of the match, which would be the plus. 
            re_2_list = re_list_generator(r'[\)\d\π][\(\&\π\@\#\`\_]', inp) # if the user is multiplying paran before like 3(. i need to make it insert * after the first index of the match. 
            re_3_list = re_list_generator(r'[\)\π\!][\d\(\π]', inp)  #if the user is multiplying paran like )3 i need to make it insert * after the first index of the match
            re_4_list = re_list_generator(r'[\d\)]-', inp) # if there is are some minuses in a row.  I need to delete both of these if so. 
            re_5_list = re_list_generator(r'\+[\-]*\+', inp) # if there are consecutive pluses, intermixed with minuses. this is true for ++ -+-+, or -++. I should delete the pluses.
            re_6_list = re_list_generator(r' ', inp) # if there is a space. I need to delete all spaces. This should go first. 
            re_7_list = re_list_generator(r'^\+', inp) # if there is a plus at the beginning, it should delete the plus
            re_8_list = re_list_generator(r'(\-[^1])|(\-$)', inp) # if there is a minus, convert to +-1*
            re_9_list = re_list_generator(r'\&\(', inp) # if there is a l paran right after a sqroot
            inp = list(inp)
            return (re_1_list[::-1], re_2_list[::-1], re_3_list[::-1], re_4_list[::-1], re_5_list[::-1], re_6_list[::-1], re_7_list[::-1], re_8_list[::-1], re_9_list[::-1])
        temp_define_list = define_lists(inp)  
        while temp_define_list != ([], [], [], [], [], [], [], [], []):
            re1, re2, re3, re4, re5, re6, re7, re8, re9 = 0, 1, 2, 3, 4, 5, 6, 7, 8            
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
            inp = list("".join(inp).replace('π', '3.1415926535897932384626433832795'))

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
        while indexes[self.LOG]:
           for i in indexes[self.LOG]:
               answer = find_log(float(inp[i+1]))
               inp[i+1] = answer
               del inp[i]
               indexes = self.determine_which_operation(inp)
        return inp

    def sin_calc(self, inp):
        indexes = self.determine_which_operation(inp)
        while indexes[self.SIN]:
           for i in indexes[self.SIN]:
               answer = self.find_sin(float(inp[i+1]))
               inp[i+1] = answer
               del inp[i]
               indexes = self.determine_which_operation(inp)
        return inp

    def cos_calc(self, inp):
        indexes = self.determine_which_operation(inp)
        while indexes[self.COS]:
           for i in indexes[self.COS]:
               answer = self.find_cos(float(inp[i+1]))
               inp[i+1] = answer
               del inp[i]
               indexes = self.determine_which_operation(inp)
        return inp

    def tan_calc(self, inp):
        indexes = self.determine_which_operation(inp)
        while indexes[self.TAN]:
           for i in indexes[self.TAN]:
               answer = self.find_tan(float(inp[i+1]))
               inp[i+1] = answer
               del inp[i]
               indexes = self.determine_which_operation(inp)
        return inp


    def square_root_calc(self, inp):
        indexes = self.determine_which_operation(inp)
        while indexes[self.SQUARE_ROOT]:
            if indexes[self.RPARAN_INDEX]: 
                end_of_sqroot = [x for x in indexes[self.RPARAN_INDEX] if x > indexes[self.SQUARE_ROOT][0]][0]
                temp_output = inp[indexes[self.SQUARE_ROOT][0]+1:end_of_sqroot]
                del inp[indexes[self.SQUARE_ROOT][0]:end_of_sqroot+1]
            else: 
                temp_output = inp[indexes[self.SQUARE_ROOT][0]+1::]
                del inp[indexes[self.SQUARE_ROOT][0]::]
            temp_output = float(self.calculation(temp_output, False))**0.5
            inp.insert(indexes[self.SQUARE_ROOT][0], temp_output)
            indexes = self.determine_which_operation(inp)
        return inp

    def factorial_calc(self, inp):
        indexes = self.determine_which_operation(inp)
        for i in self.determine_which_operation(inp)[self.FACTORIAL]:
            num_to_factorial = int(inp[i-1])
            current_product = 1
            for z in range(1,num_to_factorial+1):
                current_product *= z
            inp[i-1] = current_product
            del inp[i]
        return inp

    def abs_val_calc(self, inp): # calculates all absolute values
        while self.determine_which_operation(inp)[self.ABS_VAL_INDEX]:
            z = 0
            absolute_value_checker = self.determine_which_operation(inp)[self.ABS_VAL_INDEX]
            for i in self.determine_which_operation(inp)[self.ABS_VAL_INDEX]:
                z += 1
                if z % 2 != 0:
                    first_index = i
                    if inp[i+1] == '+':
                        del inp[i+1]
                        absolute_value_checker = self.determine_which_operation(inp)[self.ABS_VAL_INDEX]
                        break
                    if inp[first_index-1] in [0,1,2,3,4,5,6,7,8,9,')','0','1','2','3','4','5','6','7','8','9'] and first_index != 0:
                        inp.insert(first_index, '*')
                        absolute_value_checker = self.determine_which_operation(inp)[self.ABS_VAL_INDEX]
                        break
                elif z % 2 == 0:
                    second_index = i
                    temp_inp = inp[first_index+1:second_index]
                    new_temp_inp = (float(self.calculation(temp_inp, False))**2)**0.5
                    if second_index+1 == len(inp):
                        pass
                    elif inp[second_index+1] in [0,1,2,3,4,5,6,7,8,9,')','0','1','2','3','4','5','6','7','8','9']:
                        inp.insert(second_index+1, '*')
                        absolute_value_checker = self.determine_which_operation(inp)[self.ABS_VAL_INDEX]
                        break
                    del inp[first_index:second_index+1]
                    inp.insert(first_index, new_temp_inp)
                    break
        return inp
      
    def paran_calc(self, inp): # calculates all stuff in the parans. If there are parans in a paran, it calls itself, via calling the calculation method
        temp_input = ''
        inp = self.redefine_output(inp)
        while self.determine_which_operation(inp)[self.LPARAN_INDEX]:
            num_of_nested_lparan, num_of_nested_rparan = -1,-1
            for i in enumerate(inp[self.determine_which_operation(inp)[self.LPARAN_INDEX][0]:]):
                if i[1] == '(': num_of_nested_lparan += 1
                elif i[1] == ')': num_of_nested_rparan += 1
                elif len(inp)-1-i[0] == self.determine_which_operation(inp)[self.LPARAN_INDEX][0]: #make this in a loop so it doesnt just do one paranthesis and can do sin(tan(34
                    while num_of_nested_lparan != num_of_nested_rparan:
                        inp.append(')')
                        num_of_nested_rparan += 1
                if num_of_nested_rparan == num_of_nested_lparan:
                    for z in self.determine_which_operation(inp)[self.RPARAN_INDEX]:
                        if z > self.determine_which_operation(inp)[self.LPARAN_INDEX][num_of_nested_lparan]:
                            right_paran_place = z
                            break
                        
                    temp_input = inp[self.determine_which_operation(inp)[self.LPARAN_INDEX][num_of_nested_lparan]+1:right_paran_place]
                    temp_input = self.calculation(temp_input, False)
                    del_list = [x for x in range(self.determine_which_operation(inp)[self.LPARAN_INDEX][num_of_nested_lparan], right_paran_place+1)]
                    del_list.reverse()
                    pos_to_insert = self.determine_which_operation(inp)[self.LPARAN_INDEX][num_of_nested_lparan]
                    for i in del_list: del inp[i]
                    inp.insert(pos_to_insert, str(temp_input))
                    break
        return inp

    def exponent_calc(self, inp): # calculates all exponent operations, including sqroot (&)
        while self.determine_which_operation(inp)[self.EXPONENT_INDEX]: inp, indexes = self.order_of_operation_function(inp, self.EXPONENT_INDEX, -1, '^')
        return inp
    
    def multiplication_division_calc(self, inp):  # calculates multiplication and division, in whatever order pops up first
        indexes = self.determine_which_operation(inp)
        while self.determine_which_operation(inp)[self.MULTIPLY_INDEX] or self.determine_which_operation(inp)[self.DIVISION_INDEX]:
            if indexes[self.MULTIPLY_INDEX]:
                if indexes[self.DIVISION_INDEX]:
                    if indexes[self.MULTIPLY_INDEX][0] < indexes[self.DIVISION_INDEX][0]: inp, indexes = self.order_of_operation_function(inp, self.MULTIPLY_INDEX, 0, '*')
                    else: inp, indexes = self.order_of_operation_function(inp, self.DIVISION_INDEX, 0, '/')
                else: inp, indexes = self.order_of_operation_function(inp, self.MULTIPLY_INDEX, 0, '*')
            elif indexes[self.DIVISION_INDEX]: inp, indexes = self.order_of_operation_function(inp, self.DIVISION_INDEX, 0, '/')
        return inp

    def addition_subtraction_calc(self, inp):
        while self.determine_which_operation(inp)[self.ADDITION_INDEX]: inp, indexes = self.order_of_operation_function(inp, self.ADDITION_INDEX, 0, '+')
        return inp

    def calculation(self, inp, print_bool): # the basic calculation function, which calls the functions necessary to calculation in the correct order
        inp = list(inp)
        inp = self.regex_correction(inp)
        def stage(message, function, inp, print_bool): 
            inp = self.redefine_output(inp)
            inp = function(inp)
            if print_bool == True:
                print(message, "".join([str(x) for x in inp]))
                return inp
            else:
                return inp
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
            the_output =  math_expression_one.calculation(math_expression_one.inpt, True)
            print('\nthe final output as a decimal: ', round(float(the_output), 10))
            print('The final output as a fraction: ', fractions.Fraction(the_output).limit_denominator())
            time_end = time.time()
            print('It took ', round((time_end-time_start)*100000, 2), 'microseconds for the program to run!\n\n\n\n')
            user_input = input('Please give me an expression to evaluate: ')
if __name__ == '__main__': main()


#GRAPH IS NESTED LIST, Y THEN X
# Because of line spaces, stuff is messed up

import math 
import re
class Graph:
    def __init__(self, inpt):
        self.inpt = inpt
        self.x_coord = None
        self.y_coord = None
        self.input_is_valid = False
    def initialize_stuff(self):
        if self.input_is_valid:
            self.max_x_y = max(abs(self.x_coord), abs(self.y_coord))
            self.power_of_ten = (10**len(str(self.max_x_y)))
            self.size_of_graph = math.ceil(((self.max_x_y/self.power_of_ten)+(0.5*(self.max_x_y/self.power_of_ten)))*self.power_of_ten)*2
            if self.size_of_graph % 2 == 0:
                self.size_of_graph += 1
                
            self.size_of_quadrant = (self.size_of_graph-1)//2
            
            #print(self.size_of_graph, 'size_of_graph', self.size_of_quadrant, 'size_of_quadrant')
            self.the_graph = []

    def parsing_input(self):
        inpt = self.inpt
        num_lparan, num_rparan = 0,0
        paranthesis_balanced = False
        while True:
            if inpt.find('(') != -1:
                num_lparan += 1
                inpt = inpt.replace('(', '')
            elif inpt.find(')') != -1:
                num_rparan += 1
                inpt = inpt.replace(')', '')
            else:
                if (num_lparan == num_rparan) and num_lparan != 0:
                    paranthesis_balanced = True
                break
        if paranthesis_balanced == True:
            if inpt.find(',') != -1:
                inpt = inpt.split(',')
                self.x_coord = int(inpt[0])
                self.y_coord = int(inpt[1])
                self.input_is_valid = True
            
    def create_graph(self):
        self.the_graph = [' '*self.size_of_graph]*self.size_of_graph #creates the graph, using ' '
        new_graph =[]
        for y in self.the_graph: # iters over each y coord of graph. 
            y = list(y)
            y[self.size_of_quadrant] = '>' 
            y = "".join(y)
            new_graph.append(y)
        new_graph[self.size_of_quadrant] = new_graph[self.size_of_quadrant].replace(' ', '>')
        self.the_graph = new_graph
    def adding_point(self):
        list_of_current_y = list(self.the_graph[self.y_coord])
        print(self.y_coord)
        list_of_current_y[self.x_coord+self.size_of_quadrant] = 'X'
        self.the_graph[-self.y_coord-self.size_of_quadrant-1] = "".join(list_of_current_y)
    def printing_graph(self):
        for i in range(self.size_of_graph):
            print(self.the_graph[i])
my_graph = Graph(input('Please enter coords in (x,y) form: '))
my_graph.parsing_input()
my_graph.initialize_stuff()
my_graph.create_graph()
my_graph.adding_point()
my_graph.printing_graph()

Notes:
    - cannot do floats
    - cannot do lines
    - cannot parse an input and find y=mx+but
    - cant do quadratic form
    - is messed up because of line spaces
    - maybe the mutability of lists is messing me up

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