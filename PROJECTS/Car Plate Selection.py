car_plates = ['xx123', 'we2134', 'us6578', 'it1424', 'qs2321', 'po1289']
odd_days = ['MO', 'WE', 'FR']
even_days = ['TU', 'TH', 'SA']
pass_list = []
today = input('Enter todays day (SU to SA): ')
for plate in car_plates:
    last_digit = int((plate[-1]))
    if today in odd_days and last_digit % 2 != 0:
        pass_list.append(plate)
    elif today in even_days and last_digit % 2 == 0:
        pass_list.append(plate)
    elif today == 'SU':
        pass_list.append(plate)
print(pass_list)
    