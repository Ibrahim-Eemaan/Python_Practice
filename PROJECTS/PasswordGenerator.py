import random

def get_char(char_list, number):
    temp_list = []
    for i in range(number):
        temp_list.append(random.choice(char_list))
    return temp_list

while True:
    num_chars = int(input('Total Characters: '))
    num_upper = int(input('Total upper character: '))
    num_lower = int(input('Total lower character: '))
    num_digits = int(input('Total digit character: '))
    num_symbol= int(input('Total Symbol Character: '))
    if num_chars < num_upper + num_lower + num_digits + num_symbol:
        num_chars
    else:
        break

upper_list = [chr(i) for i in range(65, 65+29)]
upper_char = get_char(upper_list, num_symbol)
lower_list = [chr(i) for i in range(97, 97+20)]
lower_char = get_char(lower_list, num_symbol)
digit_list = [str(i) for i in range(0, 10)]
digit_char = get_char(digit_list, num_symbol)
symbol_list = [chr(i) for i in range(32,48)]
symbol_list += [chr(i) for i in range(58,65)]
symbol_list += [chr(i) for i in range(91,97)]
symbol_list += [chr(i) for i in range(123, 127)]
symbol_char = get_char(symbol_list, num_symbol)

num_unfilled_chars = num_chars - num_upper - num_lower - num_digits - num_symbol

whole_list = upper_list + lower_list + digit_list + symbol_list

remaining_char = get_char(whole_list, num_unfilled_chars)

password = upper_char + lower_char + digit_char + symbol_char + remaining_char

random.shuffle(password)

password = ''.join(password)

print(password)