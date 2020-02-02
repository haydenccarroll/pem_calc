import re
PI = 3.1415926535897932384626433832795028841971
def define_lists(the_input):
        the_input = "".join([str(x) for x in the_input])
        regex_list = []
        regexes = [r'[^\w\+\)\d\|]\+',
                   r'[\)\d\π][\(\&\π\@\#\`\_]',
                   r'[\)\π\!][\d\(\π]', r'[\d\)]-',
                   r'\+[\-]*\+', r' ',
                   r'^\+',
                   r'(\-[^1])|(\-$)',
                   r'\&\(', r'\*$',
                   r'(\d[A-Za-z])|([a-zA-Z]\d)', r'^\*']
        for regex in regexes:
            regex_list.append([x.start(0) for x in
                               re.finditer(regex, "".join([str(x) for x
                                           in the_input]))][::-1])
        return regex_list


def is_nested_list_empty(the_list):
        return all(map(is_nested_list_empty, the_list)) \
               if isinstance(the_list, list) else False


# replaces list by consecutive indexes
def replace_list(input_list, replacement_string, indexes_to_replace):
    if type(input_list) != list:
        input_list = list(input_list)
    del input_list[indexes_to_replace[0]:indexes_to_replace[1]+1]
    input_list.insert(indexes_to_replace[0], replacement_string)
    return input_list


def clean_input(the_input):
    # replaces keywords and symbols to other symbols for easy regex parsing
    the_input = "".join(the_input).replace('√', '&')
    the_input = the_input.replace('log', '@')
    the_input = the_input.replace('sin', '#')
    the_input = the_input.replace('cos', '`')
    the_input = the_input.replace('tan', '_')

    temp_define_list = define_lists(the_input)

    while not is_nested_list_empty(temp_define_list):
        the_input = list(the_input)
        re1, re2, re3, re4, re5, re6, re7, re8, re9, re10, re11, re12 = \
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re8]:
            the_input = replace_list(the_input, '+-1*', [i, i])
            the_input = list("".join([str(x) for x in the_input]))
            temp_define_list = define_lists(the_input)
        for i in temp_define_list[re6]:
            del the_input[i]
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re2]:
            the_input.insert(i+1, '*')
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re3]:
            the_input.insert(i+1, '*')
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re1]:
            del the_input[i+1]
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re5]:
            del the_input[i]
        for i in temp_define_list[re4]:
            the_input.insert(i+1, '+')
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re7]:
            del the_input[i]
        temp_define_list = define_lists(the_input)
        for i in temp_define_list[re9]:
            del the_input[i+1]
        for i in temp_define_list[re10]:
            del the_input[i]
        for i in temp_define_list[re11]:
            the_input.insert(i+1, '*')
        for i in temp_define_list[re12]:
            del the_input[i]
    the_input = list("".join(the_input).replace('π', str(PI)))
    return the_input
