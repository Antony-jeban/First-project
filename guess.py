import random
guesses = 0
random_num = random.randint(1,20)
name = input('what is your name :')
choice = input('hello,shall we play a guessing game?')
if choice in ['y','yes','yup','ok']:
    num = input('guess a number between 1-20:')
    while guesses < 6:
        num = int(num)
        guesses = guesses + 1
        if num < random_num:
            num = input('TOO LOW..guess again:')
        elif num > random_num:
            num = input('TOO HIGH..guess again:')
        elif num == random_num:
            print('Well Done',name,'You done this within ',guesses,'guesses!',';)')
            break
else:
    print('Thank you1!!',name)
if num != random_num:
    print('Sorry',name,' the number is ',random_num,';(')
