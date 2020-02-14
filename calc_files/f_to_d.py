def convert_to_frac(float_str):
    float_str = float_str.split('.')

    float_str[1] = (float_str[1][:7]) if len(float_str[1]) > 7 else float_str[1]
    whole_number = int(float_str[0])
    numerator = int(float_str[1])
    denominator = 10**len(float_str[1])
    numerator += whole_number*denominator
    numerator, denominator = reduce_frac(numerator, denominator)
    return f"{numerator}/{denominator}"

def reduce_frac(num, denom):
    num_factors = []
    for i in reversed(range(2, num//2+1)):
        if num % i== 0:
            num_factors.append(i)
    num_factors.append(num)

    for i in reversed(num_factors):
        if denom % i == 0:
            gcf = i
            break
    else:
        gcf = 1
    print(num_factors)
    return num//gcf, denom//gcf



def frac_to_dec(sys_args=True, input_param=None):
    import calculation
    import sys
    if sys_args:
        try:
            user_input = str(sys.argv[1])
        except NameError:
            return "Error"
    else:
        user_input = str(float(input_param))

    if '/' in user_input:
        calculator = calculation.Calculator(user_input)
        calculator.calculation(print_bool=False)
        return calculator.input
    else:
        return convert_to_frac(str(user_input)) 

if __name__ == "__main":
    frac_to_dec()
