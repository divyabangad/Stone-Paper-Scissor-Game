import random


def play(score):
    print('\n===============================================================================')
    print('Menu Options:')
    print('\t1. Stone')
    print('\t2. Paper')
    print('\t3. Scissor')

    user=input('Enter Your Choice:\n')
    comp=random.randint(1,3)

    if(comp == 1):
        print('Computer\'s Choice is Stone')
        if(user == '1'):
            print('Your Choice is Stone')
            print('\t-----------------')
            print('\tOops! It is a TIE')
            print('\t-----------------')
        elif(user == '2'):
            print('Your Choice is Paper')
            print('\t---------------')
            print('\tHurray! You WIN')
            print('\t---------------')
            score[0]=score[0]+1
        elif(user == '3'):
            print('Your Choice is Scissor')
            print('\t---------------')
            print('\tSorry, You LOST')
            print('\t---------------')
            score[1]=score[1]+1

    elif(comp == 2):
        print('Computer\'s Choice is Paper')
        if(user == '1'):
            print('Your Choice is Stone')
            print('\t---------------')
            print('\tSorry, You LOST')
            print('\t---------------')
            score[1]=score[1]+1
        elif (user == '2'):
            print('Your Choice is Paper')
            print('\t-----------------')
            print('\tOops! It is a TIE')
            print('\t-----------------')
        elif(user == '3'):
            print('Your Choice is Scissor')
            print('\t---------------')
            print('\tHurray! You WIN')
            print('\t---------------')
            score[0]=score[0]+1

    elif(comp == 3):
        print('Computer\'s Choice is Scissor')
        if(user == '1'):
            print('Your Choice is Stone')
            print('\t---------------')
            print('\tHurray! You WIN')
            print('\t---------------')
            score[0] = score[0] + 1
        elif (user == '2'):
            print('Your Choice is Paper')
            print('\t---------------')
            print('\tSorry, You LOST')
            print('\t---------------')
            score[1] = score[1] + 1
        elif(user == '3'):
            print('Your Choice is Scissor')
            print('\t-----------------')
            print('\tOops! It is a TIE')
            print('\t-----------------')

score=[0,0]
print('\nHello Mate, Let\'s play Stone, Paper And Scissor')

choice=input('\nDo you want to play?\n\tYes or No\n')
while(choice.upper()=='YES'):
    play(score)
    print('Your Score = ',score[0],' Computer\'s Score = ',score[1])
    choice=input('\nDo you want to play?\n\tYes or No\n')

print('Thank You! Bye.')