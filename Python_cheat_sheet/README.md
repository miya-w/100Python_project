
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


## List 
- Lists are used to store multiple items in a single variable.
- List itemsare ordered, changeable, and allow duplicate values. 
```python
mylist = ["apple", "banana", "cherry"]
 print(thislist) #output: ['apple', 'banana', 'cherry']

thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print(x)  #output: apple banana cherry

```
## Set
- Sets are used to store multiple items in a single variable.
- A set is a collection which is unordered, unchangeable*, and unindexed.
```python
thisset = {"apple", "banana", "cherry"}
print(thisset) ##output {'cherry', 'banana', 'apple'}
```

## Dictionaries
- We use dictionaries to store key/value pairs.
- A dictionary is a collection which is ordered*, changeable    and do not allow duplicates.
```python
customer = {
 “name”: “John Smith”,
 “age”: 30,
 “is_verified”: True
}

# We can use strings or numbers to define keys. They should be unique. We can use
#any types for the values.
customer[“name”] # returns “John Smith”
customer[“type”] # throws an error
customer.get(“type”, “silver”) # returns “silver”
customer[“name”] = “new name”
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

car
```python
# attributes:
speed = 20
fuel = 30
# method
def move():
    speed = 60
def stop()
speed = 0
#calling the method
car.stop()
```