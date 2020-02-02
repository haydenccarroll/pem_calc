import re
class Cleaner:
    def __init__(self, inputObject=None):
        self.inputObject = inputObject
        self.list_of_regex = []
    
    def define_lists(self):
        self.inputObject.input = "".join([str(x) for x in self.inputObject.input])
        self.list_of_regex = []
        regexes = [r'[^\w\+\)\d\|]\+',
                   r'[\)\d\π][\(\&\π\@\#\`\_]',
                   r'[\)\π\!][\d\(\π]', r'[\d\)]-',
                   r'\+[\-]*\+', r' ',
                   r'^\+',
                   r'(\-[^1])|(\-$)',
                   r'\&\(', r'\*$',
                   r'(\d[A-Za-z])|([a-zA-Z]\d)', r'^\*']
        for regex in regexes:
            self.list_of_regex.append([x.start(0) for x in
                               re.finditer(regex, "".join([str(x) for x
                                           in self.inputObject.input]))][::-1])
