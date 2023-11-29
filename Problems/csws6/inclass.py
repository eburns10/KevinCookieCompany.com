class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def __str__(self):
        return(f"Hi! My name is {self.name} and I have {len(self.friends)} friend(s)")
    
    def addFriend(self, newFriend):
        self.friends.append(newFriend)




p = Person("jake")
p2 = Person("angela")

print("angela and jake have met")
p2.addFriend(p)



print(p)
print(p2)