
MINI = 5

def main():
    """Function"""
    password=password_check(MINI)
    print_asterisks(password)



def password_check(mini):
    password = input("Enter password of at least {} characters: ".format(mini))

    while len(password) < mini:
        password = input("Enter password of at least {} characters: ".format(mini))
    return password

def print_asterisks(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))

main()







