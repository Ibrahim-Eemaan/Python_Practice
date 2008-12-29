import random

#play_game = 'y'

#while(play_game == 'y'):
   # answer = random.randint(1,100)
   # try_number = input('Guess a number between 1 and 100')
   # try_number = int(try_number)
   # counter = 1

#    while try_number != answer:
 #       if try_number > answer:
#            print('Your number is too large.')
  #      if try_number < answer:
#            print('Your number is too small.')
    #    try_number = int(input('Guess a number between 1 and 100'))
     #    counter = counter + 1
    #print('You got it! YOu tried ' + str(counter)) + ' times.'
#    play_game = input('Continue?: ')



#MY PROJECTS

guess_number = 'y'



while(guess_number == 'y'):
    answer = random.randint(1,100)
    guess = int(input('Input your guess: '))
    counter = 1

    if guess == answer:
       print(f'Bravo, you get it. You tried  {counter} times')
        
    
    while guess != answer:
        counter = +1
        if guess > answer:
            print('too large')
        if guess < answer:
            print(f'too small + {answer}')
        guess = int(input('Input your guess: '))