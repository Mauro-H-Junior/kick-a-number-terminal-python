import random
import time

def main_title():
    print('-'*80)
    print('                   ******* WELCOME TO THE LUCK APP *******')
    print('-'*80)
    input('                   PRESS "ENTER" TO GO TO THE APP.....')
    print('-'*60)

def verify_random_number():
    while True:

        number_user = int(input('CHOOSE A NUMBER from 1 to 100:'))

        if number_user == random_number:
            print('-'*80)
            print('****** CONGRATULATIONS, this is the correct number!! The App has been encerred ******')
            print('-'*80)
            return False

        elif number_user < random_number:
            print('-'*80)
            print('try a HIGHER number')
            print('-'*80)
            

        elif number_user > random_number:
            print('-'*80)
            print('try a LOWER number')
            print('-'*80)

def check_app_execution():

    yes_or_no = input(f'\nOPEN THE APP AGAIN?\nType "YES" or "NO":')
    print('-'*80)
    return yes_or_no.lower() == 'yes'

# ----------------------------------------------------------------------------

while True:
    main_title()

    random_number = random.randint(1,100)
    print(random_number) # Só para facilitar os testes
    print('GENERATING A NUMBER FROM 1 to 100. WAIT A MOMENT...')
    print('-'*80)
    time.sleep(2)

    verify_random_number()
    next = check_app_execution()
    if not next:
        print('Ending APP...')
        time.sleep(2)
        break
    


 


