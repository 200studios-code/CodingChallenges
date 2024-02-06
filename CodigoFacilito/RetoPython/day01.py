
# # # # # # # # # # # # # # # # # # # #
# RetoPython Dia 1 - Codigo Facilito  #
# # # # # # # # # # # # # # # # # # # #

# https://gist.github.com/200studios-code/0cb2d96e35faf374670738fdb257c03d

import os

def clear():
    try:
        os.system('cls')
    except:
        pass

class User:
    def __init__(self, name, last_name, phone, email):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        return self.email == other.email

    def greeting(self):
        return f'\n * * * Hola {self.name} {self.last_name}, en breve recibiras un correo a {self.email} * * *\n'

class OPSTATUS:
    OK = 0
    ERROR = 1

    def message_from_status(status):
        if status == OPSTATUS.OK:
            return '\n,/ ,/ ,/ User registered successfully ,/ ,/ ,/\n'
        else:
            return '\n - - - User already registered - - -\n'

class DB:
    def __init__(self):
        self.db = set()

    def register(self, user):
        if user in self.db:
            return OPSTATUS.ERROR
        self.db.add(user)
        return OPSTATUS.OK

def should_exit(opt):
    return opt == None or opt == 'X' or opt == 'x'

def make_user(name, last_name, phone, email):
    return User(name, last_name, phone, email)

def welcome_msg():
    return '\n- - - - - - -\nPress any key to register a new user\nPress X|x to exit:\n'


if __name__ == '__main__':
    clear()
    myDB = DB()

    # Start registration loop
    opt = input(welcome_msg())
    while not should_exit(opt):
        # Get info from user
        name = input('Name(s):')
        last_name = input('Last name(s):')
        phone = input('Phone number:')
        email = input('Email:')

        # Create user and register in DB
        user = make_user(name, last_name, phone, email)
        status = myDB.register(user)

        # Show registration message + greet if successful
        print(OPSTATUS.message_from_status(status))
        if status == OPSTATUS.OK:
            print(user.greeting())

        # Option to loop back
        opt = input(welcome_msg())