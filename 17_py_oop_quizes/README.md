## Object-oriented programming (OOP)
Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects.
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