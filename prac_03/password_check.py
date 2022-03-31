
MINI = 5

def main():
    """Function"""
    password = input("Enter password of at least {} characters: ".format(MINI))
    while len(password) < MINI:
        password = input("Enter password of at least {} characters: ".format(MINI))
    print('*' * len(password))
main()