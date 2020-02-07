def convert_to_frac(float_str):
    float_str = float_str.split('.')
    whole_number = int(float_str[0])
    numerator = int(float_str[1])
    denominator = 10**len(float_str[1])
    numerator += whole_number*denominator
    numerator, denominator = reduce_frac(numerator, denominator)
    return f"{numerator}/{denominator}"

def reduce_frac(num, denom):
    denom_factors = []
    for i in range(1, denom+1):
        if denom % i== 0:
            denom_factors.append(i)

    num_factors = []
    for i in range(1, num+1):
        if num % i == 0:
            num_factors.append(i)
    gcf = False
    for i in reversed(denom_factors):
        if i in num_factors:
            gcf = i
            break
    print(gcf, denom_factors, num_factors)
    if gcf:
        return num//gcf, denom//gcf
    return num, denom



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
            return convert_to_frac(user_input)
    except Exception as e:
        return e

if __name__ == "__main":
    frac_to_dec()