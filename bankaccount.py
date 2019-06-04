from account import Account
import shelve
import sys

print('Welcome to Leaf Village Bank!')
baShelf = shelve.open('bank_accounts')

print('Are you a (N)ew or (C)urrent customer? ')
customer = input().upper()

while customer != 'N' and customer != 'C':
    print('\nSorry, that is not a valid input. Please Try Again...')
    print('Are you a (N)ew or (C)urrent customer? ')
    customer = input().upper()

# If new customer
if customer == 'N':
    print('Welcome! Lets create an account for you!')

    print('Please enter your name:')
    name = input()
    name = name.capitalize()
    print(f'Welcome {name}! How much will you deposit today?')
    balance = int(input())

    if balance < 1:
        print('I am sorry but we need at least a $1 deposit to create your account')
        print('Will you deposit $1 today? (Y)es or (N)o')
        response = input().upper()

        while response != 'Y' and response != 'N':
            print('Sorry, that was an invalid input. Try again...')
            response = input().upper()

        if response == 'Y':
            balance = 1
            acc1 = Account(name, balance)
            baShelf[name] = balance
            print('Your account has been created!')
            print(acc1)
        elif response == 'N':
            print('Sorry to hear that. We hope to work with you in the future.')
            print('Have a good day!')
            sys.exit()
    else:
        acc1 = Account(name, balance)
        baShelf[name] = balance
        print('Your account has been created!')
        print(f'Thanks for coming in today {name}')
        print(acc1)
# If existing customer
elif customer == 'C':
    print('Please enter your name')
    name = input()
    name = name.capitalize()
    if name in baShelf:
        acc1 = Account(name, baShelf[name])
        print(f'Welcome back {name}!')
        print('What will you like to do today: (W)ithdraw or (D)eposit or see (B)alance')
        response = input().upper()

        while response != 'W' and response != 'D' and response != 'B':
            print('\nSorry, that was an invalid input. Try again...')
            print('What will you like to do today: (W)ithdraw or (D)eposit or see (B)alance')
            response = input().upper()

        if response == 'W':
            print('How much would you like to withdraw?')
            amount = int(input())
            valid_withdraw = acc1.withdraw(amount)
            if valid_withdraw:
                baShelf[name] = acc1.get_balance()
                print(acc1)
                print(f'Thanks for coming in today {name}!\nHave a great day!')
                sys.exit()
            else:
                print('Logging off...')
                sys.exit()
        elif response == 'D':
            print('How much would you like to deposit?')
            amount = int(input())
            if amount > 0:
                acc1.deposit(amount)
                baShelf[name] = acc1.get_balance()
                print(acc1)
                print(f'Thanks for coming in today {name}!\nHave a great day!')
                sys.exit()
            else:
                print('Sorry but that was invalid. Logging out for security purposes...')
                sys.exit()
        elif response == 'B':
            print(acc1)
            print(f'Thanks for stopping by {name}.\nHave a great day!')
            sys.exit()
    else:
        print('Sorry, we cannot find you in our system. Program will now shut down... Goodbye')
        sys.exit()

baShelf.close()
