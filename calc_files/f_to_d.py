def frac_to_dec(sys_args=True, input_param=None):
    import calc_files.calculation
    import sys
    if sys_args:
        try:
            user_input = sys.argv[1]
        except NameError:
            return "Error"
    else:
        user_input = input_param
    try:
        if '/' in user_input:
            calculator = calc_files.calculation.Calculator(user_input)
            calculator.calculation(print_bool=False)
            return calculator.input
        else:
            import fractions
            return str(fractions.Fraction(user_input).limit_denominator())
    except Exception as e:
        return e

if __name__ == "__main":
    frac_to_dec()