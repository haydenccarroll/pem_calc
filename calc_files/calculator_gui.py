from tkinter import *
import calculation
import fractions

the_calculator = calculation.Calculator("")

class Window(Frame):
    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.is_second = False

    def create_widgets(self, *refresh_input):
        if refresh_input == (False,):
            pass
        else:
            refresh_input = True
        self.master.title("PFEiMDAS Calculator")
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
            seven = Button(self.master, text='  A   ', bg='gray', fg='white',
                           command=lambda: self.button_command('Z'))
            eight = Button(self.master, text='  B   ', bg='gray', fg='white',
                           command=lambda: self.button_command('Y'))
            nine = Button(self.master, text='  C   ', bg='gray', fg='white',
                          command=lambda: self.button_command('X'))
            four = Button(self.master, text='  D   ', bg='gray', fg='white',
                          command=lambda: self.button_command('V'))
            five = Button(self.master, text='  E   ', bg='gray', fg='white',
                          command=lambda: self.button_command('U'))
            six = Button(self.master, text='  F   ', bg='gray', fg='white',
                         command=lambda: self.button_command('T'))
            one = Button(self.master, text='  G   ', bg='gray', fg='white',
                         command=lambda: self.button_command('S'))
            two = Button(self.master, text='  H   ', bg='gray', fg='white',
                         command=lambda: self.button_command('R'))
            three = Button(self.master, text='  Q   ', bg='gray', fg='white',
                           command=lambda: self.button_command('Q'))
            zero = Button(self.master, text='  |   ', bg='gray', fg='white',
                          command=lambda: self.button_command('|'))
            decimal = Button(self.master, text='  ,   ', bg='gray', fg='white',
                             command=lambda: self.button_command(','))
            equal = Button(self.master, text='  =   ', bg='gray', fg='white',
                           command=lambda: self.refresh_input_box())
            add = Button(self.master, text='  +   ', bg='gray', fg='white',
                         command=lambda: self.button_command('+'))
            minus = Button(self.master, text='  -   ', bg='gray', fg='white',
                           command=lambda: self.button_command('-'))
            multiplication = Button(self.master, text='  *   ', bg='gray',
                                    fg='white', command=lambda:
                                    self.button_command('*'))
            division = Button(self.master, text='  /   ', bg='gray',
                              fg='white', command=lambda:
                              self.button_command('/'))
            left_paran = Button(self.master, text='  {   ', bg='gray',
                                fg='white', command=lambda:
                                self.button_command('{'))
            right_paran = Button(self.master, text='  }   ', bg='gray',
                                 fg='white', command=lambda:
                                 self.button_command('}'))
            exponent = Button(self.master, text='  ^   ', bg='gray',
                              fg='white', command=lambda:
                              self.button_command('^'))
            sqroot = Button(self.master, text="  \u221A   ", bg='gray',
                            fg='white', command=lambda:
                            self.button_command('\u221A('))
            pi = Button(self.master, text='  e  ', bg='gray', fg='white',
                        command=lambda: self.button_command('e'))
            factorial = Button(self.master, text='  1/x  ', bg='gray',
                               fg='white', command=lambda:
                               self.button_command('1/', 0))
            sin = Button(self.master, text=' arcsin  ', bg='gray', fg='white',
                         command=lambda: self.button_command('arcsin('))
            cos = Button(self.master, text=' arccos  ', bg='gray', fg='white',
                         command=lambda: self.button_command('arccos('))
            tan = Button(self.master, text=' arctan  ', bg='gray', fg='white',
                         command=lambda: self.button_command('arctan('))
            clear_all = Button(self.master, text='  CE  ', bg='gray',
                               fg='white', command=lambda:
                               self.clear_input_box())
            delete = Button(self.master, text=' Del  ', bg='gray', fg='white',
                            command=lambda: self.delete_input_box())
            log = Button(self.master, text=' ln   ', bg='gray', fg='white',
                         command=lambda: self.button_command('ln('))
            graph = Button(self.master, text=' 2nd  ', bg='gray', fg='white',
                           command=lambda: self.inverse_second_var())
        else:

            seven = Button(self.master, text='  7   ', command=lambda:
                           self.button_command('7'))
            eight = Button(self.master, text='  8   ', command=lambda:
                           self.button_command('8'))
            nine = Button(self.master, text='  9   ', command=lambda:
                          self.button_command('9'))
            four = Button(self.master, text='  4   ', command=lambda:
                          self.button_command('4'))
            five = Button(self.master, text='  5   ', command=lambda:
                          self.button_command('5'))
            six = Button(self.master, text='  6   ', command=lambda:
                         self.button_command('6'))
            one = Button(self.master, text='  1   ', command=lambda:
                         self.button_command('1'))
            two = Button(self.master, text='  2   ', command=lambda:
                         self.button_command('2'))
            three = Button(self.master, text='  3   ', command=lambda:
                           self.button_command('3'))
            zero = Button(self.master, text='  0   ', command=lambda:
                          self.button_command('0'))
            decimal = Button(self.master, text='  .   ', command=lambda:
                             self.button_command('.'))
            equal = Button(self.master, text='  =   ', command=lambda:
                           self.refresh_input_box())
            add = Button(self.master, text='  +   ', command=lambda:
                         self.button_command('+'))
            minus = Button(self.master, text='  -   ', command=lambda:
                           self.button_command('-'))
            multiplication = Button(self.master, text='  *   ', command=lambda:
                                    self.button_command('*'))
            division = Button(self.master, text='  /   ', command=lambda:
                              self.button_command('/'))
            left_paran = Button(self.master, text='  (   ', command=lambda:
                                self.button_command('('))
            right_paran = Button(self.master, text='  )   ', command=lambda:
                                 self.button_command(')'))
            exponent = Button(self.master, text='  ^   ', command=lambda:
                              self.button_command('^'))
            sqroot = Button(self.master, text="  \u221A   ", command=lambda:
                            self.button_command('\u221A('))
            pi = Button(self.master, text='  \u03C0  ', command=lambda:
                        self.button_command('\u03C0'))
            factorial = Button(self.master, text='  n!  ', command=lambda:
                               self.button_command('!'))
            sin = Button(self.master, text=' sin  ', command=lambda:
                         self.button_command('sin('))
            cos = Button(self.master, text=' cos  ', command=lambda:
                         self.button_command('cos('))
            tan = Button(self.master, text=' tan  ', command=lambda:
                         self.button_command('tan('))
            clear_all = Button(self.master, text='  CE  ', command=lambda:
                               self.clear_input_box())
            delete = Button(self.master, text=' Del  ', command=lambda:
                            self.delete_input_box())
            log = Button(self.master, text=' log   ', command=lambda:
                         self.button_command('log('))
            graph = Button(self.master, text=' 2nd  ', command=lambda:
                           self.inverse_second_var())
            d_to_f = Button(self.master, text='D<->F ', command=lambda:
                            self.d_to_f())
        if refresh_input != (False,):
            self.input_box = Entry(self.master, font=("Calibri 15"))
        self.input_box.grid(row=0, column=0, sticky='nesw', columnspan=6)
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
        add.grid(row=1, column=3, sticky='nesw')
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
        self.create_widgets(False)

    def refresh_input_box(self):
        result = calculation.Calculator(self.input_box.get())
        result.calculation(print_bool=False)
        the_result = result.input
        if self.is_second:
            self.inverse_second_var()
        self.input_box.delete(0, 'end')
        self.input_box.insert(0, the_result)

    def button_command(self, str_to_append, *pos):
        if pos:
            self.input_box.insert(pos, str_to_append)
        else:
            self.input_box.insert('end', str_to_append)

    def clear_input_box(self):
        self.input_box.delete(0, 'end')

    def delete_input_box(self):
        self.input_box.delete(len(self.input_box.get())-1, 'end')

    def d_to_f(self):

        try:
            if '/' in self.input_box.get():
                decimal_calc = calculation.Calculator(self.input_box.get())
                decimal_calc.calculation(print_bool=False)
                the_result = decimal_calc.input
            else:
                the_result = fractions.Fraction(self.input_box.get()).limit_denominator()
        except Exception as e:
            print(e)
            the_result = 'Error'
        self.input_box.delete(0, 'end')
        self.input_box.insert(0, the_result)
root = Tk()
app = Window(master=root)
app.master.minsize(350, 400)
app.master.maxsize(350, 400)
app.create_widgets()
app.mainloop()
