import random
play_game = 'y'
start = 1
end = 100
direction = 'N'
smallest = start
largest = end

while play_game == 'y':
    smallest = start
    largest = end
    print('Guess a number between 1 and 100: ')
    try_number = random.randint(start, end)
    print(try_number)
    counter = 0
    direction = 'N'
    while direction != 'C':
        direction = input('Too small (S), Too long (L), Correct(C)')
        if direction == 'S':
            if try_number > smallest:
                smallest = try_number + 1
            try_number = random.randint(smallest,largest)
            print(try_number)
        if direction == 'L':
            if try_number < largest:
                largest = try_number - 1
            try_number = random.randint(smallest, largest)
            print(try_number)
    print('I got it')
    play_game = input("continue?: ")
        