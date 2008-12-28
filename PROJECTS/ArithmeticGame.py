# import random
# import time

# class ArithmeticGame:
#     def __init__(self, num_questions):
#         self.num_questions = num_questions
#     def generate_questions(self):
#         operand_1 = random.randint(1, 30)
#         operand_2 = random.randint(1, 30)
#         operator = random.choice(['+', '-', '*', '//'])
#         if operator == '+':
#             answer = operand_1 + operand_2
#         if operator == '-':
#             answer = operand_1 - operand_2
#         if operator == '*':
#             answer = operand_1 * operand_2
#         if operator == '//':
#             answer = operand_1 // operand_2
#         question = str(operand_1) + ' ' + operator + ' ' + str(operand_2)
#         return question, answer
#     def play_game(self):
#         num_correct = 0
#         start_time = time.time()
#         for i in range(self.num_questions):
#             print(f'Question {str(i+1)}:')
#             question, answer = self.generate_questions()
#             print(question)
#             user_answer = int(input('What is your answer?: '))
#             if user_answer == answer:
#                 num_correct = num_correct + 1
#                 print('You are correct')
#             else:
#                 print(f'You are wrong. The correct answer is {str(answer)}')
#         end_time = time.time()
#         print(f'You got {str(num_correct)} answers correct.')
#         print('You used {0:.3f} seconds.'.format(end_time - start_time))

# new_game = ArithmeticGame(20)
# new_game.play_game()

import random
import time

class ArithmeticGame:
    def __init__(self, num_questions):
        self.num_questions = num_questions
    def generate_questions(self):
        operand_1 = random.randint(1, 30)
        operand_2 = random.randint(1, 30)
        operator = random.choice(['+', '-', '*', '//'])
        if operator == '+':
            answer = operand_1 + operand_2
        elif operator == '-':
            answer = operand_1 - operand_2
        elif operator == '*':
            answer = operand_1 * operand_2
        elif operator == '//':
            answer = operand_1 // operand_2
        question = f'{operand_1} {operator} {operand_2}'
        return question, answer
    def play_game(self):
        num_correct = 0
        question, answer = self.generate_questions()
        for i in range(self.num_questions):
            print(f'Question {i+1}')
            print(question)
            user_answer = (input('What is your answer: '))
            if user_answer == answer:
                print('You are correct')
                num_correct += 1
            if user_answer != int:
                print(question)
                user_answer
      
new_game = ArithmeticGame(10)
new_game.play_game()
