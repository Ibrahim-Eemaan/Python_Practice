def print_queue(*a_list, **a_dict):
    for person in a_list:
        for patient, info in a_dict.items():
            if person == patient:
                print(person + ':')
                for key, value in info.items():
                    print(key + ' = ' + str(value))
            return

queue_list = ['Nelson', 'tiffany', 'Michelle' 'Raymond', 'Polly']
patient_dict = {'Tiffany': {'age': 15, 'weight': 50},
                'Raymond': {'age': 23, 'weight': 65},
                'Sabrina': {'age': 20, 'weight': 57},
                'Michelle': {'age': 21, 'weight': 53}
                }

print('These waiting people are on the record.')
print_queue(*queue_list, **patient_dict)
