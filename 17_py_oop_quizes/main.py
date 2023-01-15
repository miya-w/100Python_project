
#Build your own class
# - attribute
# - method


class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1
        
user_1 = User("001","Mia")
user_2 = User("002","John")

#call methodpo
user_1.follow(user_2)
        
print(User) 
    # output: <class '__main__.User'>
print(user_1)
    #output: <__main__.User object at 0x107adc910>
print(user_1.id)
    #output: 001
print(user_2.username)
    #output: John

print(User.follow)
    #<function User.follow at 0x1071b8ae0>

print(user_1.follower)
    #output: 0
print(user_1.following)
    #output: 1
print(user_2.follower)
    #output: 1