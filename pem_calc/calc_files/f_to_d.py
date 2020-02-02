import calculation
import sys
try:
    user_input = sys.argv[1]
    if '/' in user_input:
        calculator = calculation.Calculator(user_input)
        calculator.calculation(print_bool=False)
        print(calculator.input)
    else:
        import fractions
        print(fractions.Fraction(user_input).limit_denominator())
except:
    print("Error")