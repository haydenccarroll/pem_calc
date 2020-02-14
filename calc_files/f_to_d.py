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
    return num//gcf, denom//gcf



def frac_to_dec(input_param=None):
    import calculation
    import sys

    try:
        input_param = sys.argv[1]
        user_input = input_param
    except IndexError:
        if not input_param:
            return input_param, "Error"
        user_input = str(input_param)

    if '/' in user_input:
        user_input = str(user_input)
        calculator = calculation.Calculator(user_input)
        calculator.calculation(print_bool=False)
        return input_param, calculator.input
    else:
        user_input = str(float(user_input))
        return input_param, convert_to_frac(user_input) 

if __name__ == "__main__":
    user_input, output = frac_to_dec()
    with open("../log/previous_calculations.txt", 'ab') as file:
        string = f'{user_input}, {output}\n'
        string = string.encode("utf8")
        file.write(string)