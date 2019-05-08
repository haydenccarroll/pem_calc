'''
import re
def convert_to_ymxb_form(inp):
    inp = re.split(r'([\+\=])', inp)
   
    def redefine_indexes(inp):
        indexes_of_y = []
        indexes_of_x = []
        indexes_of_operators = []
        index_of_equal = None
        for i in enumerate(inp):
            if (i[1]).find('y') != -1:
                print(i[0], i[1], 'finding y')
                indexes_of_y.append(i[0])
            if i[1].find('=') != -1:
                index_of_equal = i[0]
            if i[1].find('x') != -1:
                indexes_of_x.append(i[0])
            if i[1].find('+') != -1:
                indexes_of_operators.append(i[0])
        return indexes_of_y, indexes_of_x, index_of_equal, indexes_of_operators      
    
    indexes_of_y, indexes_of_x, index_of_equal, indexes_of_operators = redefine_indexes(inp)
    for i in indexes_of_y:
        print(i, index_of_equal, indexes_of_y)
        if i > index_of_equal:
            print('is tjos ever ran? also here is index_of_equal and i', index_of_equal, i, inp)
            inp.append('-%s+'%inp[i])
            inp.insert(0, '-%s+'%inp[i])
            inp = re.split(r'([\+\=])', "".join(inp))
            indexes_of_y, indexes_of_x, index_of_equal, indexes_of_operators = redefine_indexes(inp)
    for i in [x for x  in range(0,len(inp)) if ((x not in indexes_of_y) and (x not in indexes_of_operators))]:
        print(inp)
        print(i, index_of_equal, indexes_of_y, indexes_of_operators, 'this is at ln 31', i)
        if i < index_of_equal:
            print('is tjos ever ran? also here is index_of_equal and i', index_of_equal, i, inp)
            inp.append('+-%s+'%inp[i])
            inp.insert(0, '+-%s+'%inp[i])
            inp = re.split(r'([\+\=])', "".join(inp))
            indexes_of_y, indexes_of_x, index_of_equal, indexes_of_operators = redefine_indexes(inp)
    print(inp)
convert_to_ymxb_form('3x=3y+2')

'''