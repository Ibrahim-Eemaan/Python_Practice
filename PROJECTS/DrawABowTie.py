l = input("How long should it be?: ")
l = int(l)
for i in range(l):
    string = '*' * (i + 1)
    string += ' ' * (2 * (l - i - 1))
    string += '*' * (i + 1)
    print(string)
for i in range(l - 1):
    string = '*' * (l - i - 1)
    string += ' ' * (2 * (i + 1))
    string += '*' * (l - i - 1)
    print(string)