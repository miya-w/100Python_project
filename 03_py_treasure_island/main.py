print('''
      
XXXXXXXXXXXXXXXXXXFEDERAL RESERVE NOTEXXXXXXXXXXXXXXXXXXX
XXX  XX       THE UNITED STATES OF AMERICA        XXX  XX
XXXX XX  -------       ------------               XXXX XX
XXXX XX              /   jJ===-\    \      C7675  XXXX XX
XXXXXX     OOO      /   jJ - -  L    \      ---    XXXXXX
XXXXX     OOOOO     |   JJ  |   X    |       __     XXXXX
XXX    3   OOO      |   JJ ---  X    |      OOOO    3 XXX
XXX                 |   J|\    /|    |     OOOOOO     XXX
XXX     C36799887   |   /  |  |  \   |      OOOO      XXX
XXX                 |  |          |  |       --       XXX
XXX      -------    \ /            \ /                XXX
X  XX                \ ____________ /               X  XX
XX XXX 3_________        --------  ___   _______ 3 XXX XX
XX XXX            ___   ONE DOLLAR  i              XXX XX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  
      ''')
print("welcome to treasure island!")
print("you are going to rob a bank with your friend Michael")
choice1 = input('you\'re at crossroad, and you saw a police car next to you, do you drive "straight" or "turn away"? ').lower()

if choice1 == "straight":
    print('you didn\'t attract police\'s attention, and you got the bank!')
    choice2 = input('you got the bank, choose to "wear" mask or "Not wear" mask?').lower()
    if choice2 == "wear":
        print("you came to the bank and controlled the staffs in bank")
        choice3 = input( 'You are going to take the money and Michael still want more, choose "Stop" him or "Let"him ask the more money?').lower()
        if choice3 == "stop":
            print("You ran away in time, and you got a huge of money!")
        else:
            print("Game Over! The police had came and you were caught")            
    else:
        print("You was reconized by someone who know you, you were caught!")
else:
    print("your suspecious behaviour attract police, and you are stoped by them, IT IS GAME OVER! ")