#---------If_else----------

# height = int(input("what's your height in cm ? " ))

# if height > 120:
#     print("you can ride the rollercoaster")
# else:
#     print("Sorry, you can't ride the rollercaster")
    
#----- == odd & even------   
# number = int(input("Give me a number"))

# if number % 2 == 0:
#     print("This is a even number.")
# else:
#     print("This is an odd number.")
 
# ---------if/ elif/else --------  

# height = int(input("what's your height in cm ? " ))
# if height >= 120:
#     print("you can ride the rollercoaster")
#     age = int(input("what's your age? "))
#     if age <= 12:
#         print("ticket is $5 ")
#     elif age <= 18:
#         print("ticket is $7")
#     else:
#        print("ticket is $12 ")
        
# else:
#     print("Sorry, you can't ride the rollercaster")


# --------------------------------------
  
# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#   print("You can ride the rollercoaster!")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill = 5
#     print("Child tickets are $5.")
#   elif age <= 18:
#     bill = 7
#     print("Youth tickets are $7.")
#   else:
#     bill = 12
#     print("Adult tickets are $12.")
  
#   wants_photo = input("Do you want a photo taken? Y or N. ")
#   if wants_photo == "Y":
#     bill += 3
  
#   print(f"Your final bill is ${bill}")

# else:
#   print("Sorry, you have to grow taller before you can ride.")

    
# ---------and or ---------
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
