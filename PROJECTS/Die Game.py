import random

start_place = 0
end_place = 40
user_place = 0
computer_place = 0
user_win = False
computer_win = False
quit_game = False

#Starting The Logical Part
while not user_win or not computer_win:
    user_input = input("Enter 't' to toss and 'q' to quit: ")
    if user_input == 'q':
        quit_game = True
        break
    if user_input == 't':
        user_move = random.randint(1,6)
        user_place += user_move
    print("You move " + str(user_move) + " Steps.")
    if user_place > end_place:
        overshoot = user_place - end_place
        user_place = end_place - overshoot
    print("You are now at " + str(user_place) + "Position.")
    if user_place == end_place:
        user_win = True
        break

    computer_move = random.randint(1,6)
    computer_place += computer_move
    print("Computer move for " + str(computer_move) + " steps.")
    if computer_place > end_place:
        overshoot = computer_place - end_place
        computer_place = end_place - overshoot
    print("Computer is now at the " + str(computer_place) + " Position.")
    if computer_place == end_place:
        computer_win = True
        break
if quit_game:
    print("YOu have " + str(user_place - end_place) + " steps to go")
if user_win:
    print("Congrats! You win")
if computer_win:
    print("Computer wins!")