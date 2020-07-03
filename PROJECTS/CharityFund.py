# class CharityFund:
#     def __init__(self, balance):
#         self.balance = balance
#     def save_fund(self, amount):
#         self.balance += amount
#     def spend_fund(self, amount):
#         self.balance -= amount
#     def invest(self, return_rate):
#         self.balance *= 1 + return_rate
#     def get_balance(self):
#         if self.balance < 0:
#             print(f'You got a deficit of {str(-self.balance)}')
#         return self.balance
#     def is_danger(self):
#         if self.balance < 50000:
#             print(f'Danger, You have {str(self.balance)} left')
#         return self.balance < 50000

# help_elderly = CharityFund(1000000)
# help_elderly.spend_fund(200000)
# print(help_elderly.get_balance())
# help_elderly.invest(-0.05)
# print(help_elderly.get_balance())
# help_elderly.save_fund(100000)
# print(help_elderly.get_balance())
# help_elderly.spend_fund(900000)
# print(help_elderly.get_balance())
# print(help_elderly.is_danger())


class CharityPage:
    def __init__(self, balance):
        self.balance = balance
    def save_fund(self, amount):
        self.balance += amount
    def spend_fund(self, amount):
        self.balance -= amount
    def invest(self, price):
        self.balance *= 1 + price
    def get_balance(self):
        if self.balance < 0:
            print(f'You are having a deficit of {str(-self.balance)}')
        return f'You are having {str(self.balance)}'
        if self.balance <= 20000:
            return f'Danger, you are having less than or equal to {str(self.balance)}'


help_needy = CharityPage(100000)
help_needy.save_fund(20)
print(help_needy.get_balance())