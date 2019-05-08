ALPHABET, the_shift, the_input =  'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 11, input('Enter something here: ').upper(); print("".join([["".join([ALPHABET[i] for i in [(ALPHABET.find(i)+the_shift) if (ALPHABET.find(i)+the_shift) < 26 else (ALPHABET.find(i)+the_shift) - 26 for i in current_word]])+' ' for x in the_input.split(' ')][0] for current_word in the_input.split(' ')]))

