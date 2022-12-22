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


# - - - - - - - - - - - - - - -
# ---- Nest------
#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

print(travel_log)

def add_new_country(country_visted, times_visted, cities_visted):
    new_country = {}
    new_country["country"] = country_visted
    new_country["visits"] = times_visted
    new_country["cities"] = cities_visted
    travel_log.append(new_country)

add_new_country("Russia" , 2 , ["Moscow", "saint Peterburg"])

print(travel_log)

