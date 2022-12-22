# print('hello')

# if 5 > 2:
#  print("Five is greater than two!") 
# if 5 > 2:
#         print("Five is greater than two!") 
        
#------BNI caculator in Python-------
# height = input('enter your height in m: ')
# weight = input('enter your weight in kg: ')


# Weight_for_print = int(weight)

# print(weight)
# print('your wight is '+ str(Weight_for_print))

# bmi = int(weight)/ float(height) ** 2
# bmi_as_init = int(bmi) 
# print(bmi_as_init)
# print('your bmi is '+str(bmi_as_init))
#-------------------------------------
# print(either only string or number ) 
# print('your wight is '+ str(Weight_for_print)) -> //print : your wight is 50
# print('your wight is '+ Weight_for_print) -> Error
#-------------------------------------
# print(5/2)

#+=
#/=
#-=
#*=

# score = 0

#User Score

# score += 1
# print(score)
#---------------

#format() method -> (python 2.0 Out of date)f-string
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price)) 


#----Life calculator-----

# your_age = input('How old are you?')

# year_remaining = 83 - your_age
# days_remaining = year_remaining * 365
# weeks_remaining = year_remaining * 52
# message = "you still get {} days to live. "
# message_week = "you still get {} weeks to live. "

# print(message.format(days_remaining)) 
# print(message_week.format(weeks_remaining)) 

#--------Tip Caculator---------

bill = float(input('How much is the bill?'))
tip = int(input('how much is the tip? 10%, 12%, 15%?'))
people = int(input('how many people?'))
# bill_f = float((bill + bill * (tip/100))/people)

print(bill)
print(tip)
print(type(tip))
print(tip / 100)
print(type(tip / 100))
print(float(tip/100))

tip_percent = float(tip/100)
tip_f = float(bill * tip_percent)
bill_total = bill + tip_f


print(tip_percent)
print(tip_f)
print(bill_total)

print(3 / 2) 
print(float(3) / 2)
print((1.0 * 3) / 2) 











