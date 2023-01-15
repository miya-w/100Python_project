
# Python CheatSheet

## Data Types
```
Integers	-2, -1, 0, 1, 2, 3, 4, 5
Floating-point numbers	-1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25
Strings	'a', 'aa', 'aaa', 'Hello!', '11 cats'
```
```python
price = 10
rating = 4.9
course_name = ‘Python for Beginners’
is_published = True

#In the above example,
#• price is an integer (a whole number without a decimal point)
# • rating is a float (a number with a decimal point)
#• course_name is a string (a sequence of characters)
#• is_published is a boolean. Boolean values can be True or False. 
```

## The str(), int(), and float() Functions
```python
int('11')
# 11
float('3.14')
# 3.14

birth_year = int(input(‘Birth year: ‘))
#The input() function always returns data as a string. So, we’re converting the
#result into an integer by calling the built-in int() function. 

```
## Math Operators
```
**	Exponent	2 ** 3 = 8
%	Modulus/Remainder	22 % 8 = 6
//	Integer division	22 // 8 = 2
/	Division	22 / 8 = 2.75
*	Multiplication	3 * 3 = 9
-	Subtraction	5 - 2 = 3
+	Addition	2 + 2 = 4
= -> equal
== -> check
```



## Augmented Assignment Operators
#+=
#/=
#-=
#*=

var += 1	var = var + 1
```python
score = 0
#User Score
score += 1
print(score)
# #output: 1
```
## If Statements 

```python
if is_hot: 
    print(“hot day”) 
elif is_cold: 
    print(“cold day”) 
else:  
    print(“beautiful day”) 
```

## While loops 
```python
i = 1
while i < 5:
 print(i)
 i += 1
```

## For loops
```python
for i in range(1, 5):
 print(i)
```
## store collections of data

4 built-in data types in Python used to store collections of data
- List
- Set
- Dictionary
- Tuple


## List [ ]
- Lists are used to store multiple items in a single variable.
- List itemsare **ordered, changeable, and allow duplicate values**. 
```python
mylist = ["apple", "banana", "cherry"]
 print(thislist) #output: ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print(x)  #output: apple banana cherry

```
## Set{ }
- Sets are used to store multiple items in a single variable.
- A set is a collection which is **unordered, unchangeable*, and unindexed**.
```python
thisset = {"apple", "banana", "cherry"}
print(thisset) ##output {'cherry', 'banana', 'apple'}
```

## Dictionaries { }
- We use dictionaries to store key/value pairs.
- A dictionary is a collection which is **ordered, changeable and do not allow duplicates**.
```python
#Dictionaries are used to store data values 
# in key:value pairs.
# {
#     key1 : value1,
#     key2 : value2,
#     key3 : value3
# }
```
### Example
```pthon
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2020
}
print(thisdict)
#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
print(thisdict["brand"])
#output: Ford
print(thisdict["model"])
#output:Mustang

```

### - Access the dictionary
1.  get()
2. The **keys() method** will return a list of all the keys in the dictionary.
 ```python
 print(thisdict.keys())
    #output: dict_keys(['brand', 'model', 'year'])
```
### Add the item
```python
thisdict["color"] = "white"
print(thisdict)
#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020, 'color': 'white'}
```
### Update the item
- The update() method will update the dictionary with the items from the given argument.
1. ->thisdict.update({"year": 2020})
2. ->
```python
thisdict["year"] = 2018
print(thisdict)
#output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018, 'color': 'white'}
```

### Removing Items
- The pop() method removes the item with the specified key name
```python
thisdict.pop("model")
print(thisdict)
#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict.popitem()
print(thisdict)
```

## forloop in dictionary
```python
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
``` 
## Random

```python
import random
Love_score = random.randint(1, 100)
print(f"Your Love score is {Love_score} ")

# print("Let's flip the coin!")
coin = random.randint(0,1)
if coin == 0:
    print( "It's head!")
else:
    print( "it's number!")
```


## Loop
 - What is Loop ? 
```python
for item in list_of_item:
        # *Do something to each item*
```

```python
# In For Loop, it's going to assign the variable name score to each of the items in list""
student_scores = [78, 65, 80, 91, 64, 89, 92]

hight_score = 0
for score in student_scores:
    if score > hight_score:
        hight_score = score
    print(student_scores)
    print(hight_score)
    
#output
#print(student_scores) #[78, 65, 80, 91, 64, 89, 92]
#print(hight_score) #92
```
## Function

```python
#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Jack Bauer")
```
- What is print(f"...")?
- print(f"...") -> format
[StackOverFlow - What is print(f"...")](https://stackoverflow.com/questions/57150426/what-is-printf)

## OOP
- **Object-oriented programming (OOP)** is a method of structuring a program by bundling related properties and behaviors into individual objects.
## Build your own class
- attribute
- method
The attributes are the things that the object **has**.
The methods are the things that the object **does**.

```python
def function()
     pass
```
## __init__

### Init function
- Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

when our object is being constructed.And this is also known in programming as initializing an object. When the object is being initialized,we can set variables or counters to they're starting values.

### The self Parameter
The self **parameter** is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
### pass 
if we actually really want to leave this function or this class empty, we can use a keyword which is pass.And all it does is it just passes. It says, I don't want to have a go right now. Just continue to the next line of code. And this gets rid of our errors

### Object Methods
- excute 
```python
user_1.follow(user_2)
```
### Example.
```python
#--- no_init_function---
class User:
    pass

user_1 = User()
user_1.id ="001"
user_1.username = "Mia"

user_2 = User()
user_2.id ="002"
user_2.username = "John"
```
### example using __init__
```python
#---Using __init__---
class User:
    def __init__(self,id,username):
        self.id = id
        self.username = username
        self.fallower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1
        
user_1 = User("001","Mia")
user_2 = User("002","John")
user_3 = User("003","Harry")
        
#call methodpo
user_1.follow(user_2)

#---OutPut---      
print(User) 
    # output: <class '__main__.User'>
print(user_1)
    #output: <__main__.User object at 0x107adc910>
print(user_1.id)
    #output: 001
print(user_2.username)
    #output: John
print(user_1.follower)
    #output: 0
print(user_1.following)
    #output: 1
print(user_2.follower)
    output: 1

```

---
Resources
- [medium - What is a Python Class and How Do You Use It?](https://towardsdatascience.com/enhance-your-python-project-code-with-classes-5a19d0e9f841)
- [Python Document - 9.Class](https://docs.python.org/3/tutorial/classes.html)
-[geeksforgeeks - python object ](https://www.geeksforgeeks.org/python-object/)
