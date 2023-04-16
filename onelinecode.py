input_string = str(input('string: '))
print(' '.join(sorted([input_string[i] if (ord(input_string[i]) - 97) % 2 == 0 else input_string[i].upper() for i in range(len(input_string)) ],reverse=True)))