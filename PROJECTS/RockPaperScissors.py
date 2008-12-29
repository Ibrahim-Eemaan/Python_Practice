import random

wins = 0
draws = 0
losses = 0
is_ended = False
prompt =  "Choose one, Rock ('r'), Paper ('p'), Scissors('s') or 'q' to quit: "
while True:
    user_choice = input(prompt)
    while user_choice not in (['r', 's', 'p', 'q']):
        user_choice = input(prompt)
    if user_choice == 'q':
        break
    else:
        computer_choice = random.choice(['r', 's', 'p', 'q'])
        if computer_choice == 'r':
            move = 'Rock'
        elif computer_choice == 's':
            move = 'Scissors'
        else:
            move = 'Paper'
        print("Computer take a " + move)
        if computer_choice == user_choice:
            print('You Draw')
            draws += 1
        if (computer_choice == 'r' and user_choice == 'p' ) or (computer_choice == 'p' and user_choice == 's') or (computer_choice == 's' and user_choice == 'r'):
            print('YOu win')
            wins += 1
        else:
            print('You lose')
            losses += 1
print('You have ' + str(wins) + ' wins, ' + str(draws) + ' draws, ' + str(losses) + ' losses.')