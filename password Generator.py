import string
import random

def password_generator():
    flag = True

    while flag:
        nc = int(input("Number of characters: "))
        nu = int(input("Enter number of Upper case letters: "))
        nl = int(input("Enter the number of Lower case letters: "))
        nd = int(input("Enter number of digits: "))
        ns = int(input("Enter Number of Symbols: "))

        if nu + nl + nd + ns > nc:
            print("Number of characters do not match")
        else:
            flag = False

    ne = nc - (nu + nl + nd + ns)

    upper_char = random.sample(list(string.ascii_uppercase), nu)
    lower_char = random.sample(list(string.ascii_lowercase), nl)
    digit_char = random.sample(list(string.digits), nd)
    symbol_char = random.sample([i for i in list(string.punctuation) if i not in [",", '"', "'", ")", "(", "]", "[", "}", "{"]], ns)

    T = list(string.ascii_letters) + list(string.digits) + [i for i in list(string.punctuation) if i not in [",", '"', "'", ")", "(", "]", "[", "}", "{"]]
    extra_char = random.sample(T, ne)

    password_letters = upper_char + lower_char + digit_char + symbol_char + extra_char
    random.shuffle(password_letters)
    password = "".join(password_letters)

    return password

print(password_generator())
