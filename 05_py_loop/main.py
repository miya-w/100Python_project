# - - - - - - - - - - - - - -
# ----- What is Loop ? -----
# - - - - - - - - - - - - - -
 
    #for item in list_of_item:
        #Do something to each item

# = -> equal
# == -> check
# - - - - - - - - - - - - - 
# lus-Equals Operator +=
# Plus-Equal Operator
# - - - - - - - - - - - - -
# counter = 0
# counter += 10

# # This is equivalent to

# counter = 0
# counter = counter + 10
# print(counter)

# The operator will also perform string concatenation

# message = "Part 1 of message "
# message += "Part 2 of message"

#  - - - - - - - - - - - - - - - -
# ----------- Loop --------------
# - - - - - -- - - - - - - - - - - 

# fruits = ["apple", "pear", "orange", "pineapple"]
# for fruit in fruits:
#     print(fruit)
# print(fruits)

# print // print(fruit) : apple pear orange pineapple
# print // print(fruits) : ['apple', 'pear', 'orange', 'pineapple']

# In For Loop, it's going to assign the variable name fruit to each of the items starting
# from the first one apple in "fruits list"

# - - - - - - - - - - - - - - - - -
# ------the highest score --------

# student_scores = [78, 65, 80, 91, 64, 89, 92]

# hight_score = 0
# for score in student_scores:
#     # if score > hight_score:
#     #     hight_score = score
#     print(student_scores)

# - - - - - - - - - - - - - -  - - - - - 
#----------- Loop with Range ----------
#range() Function
#To loop through a set of code a specified number of times, we can use the range() function,
# - - - - - - - - - - -  - - - - - - - - 

#  for nuber in range(a, b)
#     print (number)

# for number in range(1, 100):
#   print(number)

# # print put // 1 ~ 99

# for number in range(1, 101):
#   print(number)
# # print put // 1 ~ 100

# for number in range(1, 11, 3):
#   print(number)

# # print out // 1 4 7 10

total = 0
for number in range (1, 101):
     total += number
        # total = total + number
print(total)

## print put // 5050

# for number in range(1, 16):
#     if number % 3 == 0 and number % 5 ==0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print ("buzz")
#     else:
#         print(number)

# - - - - - - - - - - - - - - - - - - -
# ---- Password Generator Project ----
# - - - - - - - - - - - - - - - - - - -  

# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level
# # password = ""

# # for char in range(1, nr_letters + 1):
# #   password += random.choice(letters)

# # for char in range(1, nr_symbols + 1):
# #   password += random.choice(symbols)

# # for char in range(1, nr_numbers + 1):
# #   password += random.choice(numbers)

# # print(password)

# #Hard Level
# password_list = []

# for char in range(1, nr_letters + 1):
#   password_list.append(random.choice(letters))

# for char in range(1, nr_symbols + 1):
#   password_list += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#   password_list += random.choice(numbers)

# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""
# for char in password_list:
#   password += char

# print(f"Your password is: {password}")
