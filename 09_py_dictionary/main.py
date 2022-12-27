# --- Python Dictionaries ---
# Dictionaries are used to store data values in key:value pairs.
# {
#     key1 : value1,
#     key2 : value2,
#     key3 : value3
# }

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }

# print(thisdict)
# print out // {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
# print(thisdict["brand"])
# print out // Ford


##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.

# print(programming_dictionary["Function"])

#Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)
#Create an empty dictionary.
# empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#######################################
student_scores = {
  "Harry": 67,
  "Mary": 82,
  "Mia" : 90,
  "Hamilton":88,
  "David":91,
}

#for student in student_scores:
  # print(student_scores[student]) #output: 67 82 90 88 91
  # print(student) #output: Harry Mary Mia Hamilton David
  # print(student_scores["Mia"]) #output : 90

# 1. Create an empty dictionary student_grades.
student_grades = {}

# 2. Write your code below to add the grades to student_grades.
for student in student_scores:
 score = student_scores[student]
 if score > 90:
   student_grades[student] = "Outstanding"
 elif score > 80:
   student_grades[student] = "Execellent"
 elif score > 70:
   student_grades[student] = "acceptable"
 else: 
   student_grades[student] = "fail"
print(student_grades)
  
   





# - - - - - - - - - - - - - - -
# ---- Nest------
#Nesting 
# capitals = {
#   "France": "Paris",
#   "Germany": "Berlin",
#   }

#Nesting a List in a Dictionary

# travel_log = {
#   "France": ["Paris", "Lille", "Dijon"],
#   "Germany": ["Berlin", "Hamburg", "Stuttgart"],
# }

#Nesting Dictionary in a Dictionary

# travel_log = {
#   "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }

# #Nesting Dictionaries in Lists

# travel_log = [
# {
#   "country": "France", 
#   "cities_visited": ["Paris", "Lille", "Dijon"], 
#   "total_visits": 12,
# },
# {
#   "country": "Germany",
#   "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#   "total_visits": 5,
# },
# ]

# print(travel_log)

# def add_new_country(country_visted, times_visted, cities_visted):
#     new_country = {}
#     new_country["country"] = country_visted
#     new_country["visits"] = times_visted
#     new_country["cities"] = cities_visted
#     travel_log.append(new_country)

# add_new_country("Russia" , 2 , ["Moscow", "saint Peterburg"])

# print(travel_log)

