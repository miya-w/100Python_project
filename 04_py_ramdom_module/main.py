# ---------Random in Python -----------

import random

# Love_score = random.randint(1, 100)
# print(f"Your Love score is {Love_score} ")

# print("Let's flip the coin!")
# coin = random.randint(0,1)
# if coin == 0:
#      print( 
#            "It's head!"
#             '''
                    

#            _,--*dSS|""I$$$SSccc,_
#          <$$$b |$$$l  j$$$$$$$$$$$$$Sbp
#           ?$$$b|$$$$  d$$$$$$$$$$$$$$P
#            ?$$$$$$$$; $$$$$$$$$$$$$$P
#             ?$$$$$$$| $$$$$$$$$$$$$P
#              )$$$$$$$_$SSSSS$$$$$$(
#              Y"'               """P
#              (                    )
#      _.,cccccd%S$$$$$$$$$$$$$$$SScccc,._
#    ($$$$$$$$$$SSSSSSSSSSSSSSS$$$$$$$$$$$$$$$)
#      `"""""Y"'      ____        `"$$$$$$$P"'
#            8P    ,o88o  `\        )
#          ,-'  \o888888)   )  .^^^^^^\
#       .-'   ..  \ """'    )_ \   _   )
#      (___.--.;   "---...-'~  /  / )  )
#       )      __..._      __/'  / )) /
#      (`.__.-)_)_)_))  {~'     .\_/_/
#     .'   `-.) ) ) ))   `.__.-'   \
#    /        `~----'        _/'    \.
#  .'                 _...../        )`-----...____
# ( ,          _.-~~~'       ......-'
#  `\______,.-~     Allen Mullen


              

#            ''')
# else:
#     print(
#         "it's number!"
#         '''
                     
# ,adPPYba,  
# I8[    ""  
#  `"Y8ba,   
# aa    ]8I  
# `"YbbdP"'  
                 
        
#         '''
#     )
    
# ----------Banker Game -----------

# The split() method splits a string into a list.
# split(",") -> tell python so seprate items with comma " , ".
# len() -> count the number of items in the list. 
# person_who_will_pay = names[random_choice]


# print('''
#         __                _ 
#  / _|              | |
# | |_ ___   ___   __| |
# |  _/ _ \ / _ \ / _` |
# | || (_) | (_) | (_| |
# |_| \___/ \___/ \__,_|
      
#       ''')

# names_string = input("Give me everyone's name, seprated by a comma.")

# names = names_string.split(",")

# print(len(names))
# print(names)
# num_items = len(names)


# random_choice = random.randint(0, num_items - 1 )

# person_who_will_pay = names[random_choice]
# # in the "names list" pick one item randomly. 

# print(random_choice)
# print(person_who_will_pay +" will pay the bill." )

#-------------------------------------------

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38 we are trying to prevent a crash by detecting
#any numbers great than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
#Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end






