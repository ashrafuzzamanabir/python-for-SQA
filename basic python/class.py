import random

class Person:
    def __init__(self, firstname , lastname, health, status):
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status
        
    def introduce(self):
        "all people introduce themselves"
        print("hello, my name is {} {}".format(self.firstname,self.lastname))

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion==1:
            print("{} is happy today".format(self.firstname))
        elif emotion==2:
            print("{} is sad today".format(self.firstname))
        else:
            print("{} is mad today".format(self.firstname))
    
    def status_change(self):
        if self.health ==100:
            print("{} is totaly healthy".format(self.firstname))

        elif self.health >= 80:
            print("{} is a healthy".format(self.firstname))

        elif self.health >=60:
            print("{} is somewhat healthy".format(self.firstname))
        elif self.health >= 40:
            print("{} is not too healthy".format(self.firstname))

        else:
            print("{} is in awful condition".format(self.firstname))


abir = Person("Abir","Hossain", 100, status=True)
araf = Person("Araf","Hossain", 70, status=False)
emu = Person("Emu","Hossain", 30, status=False)

print("{} is my friend {}".format(abir.firstname, abir.status))

abir.introduce()
abir.emote()
abir.status_change()

araf.introduce()
araf.emote()
araf.status_change()

emu.introduce()
emu.emote()
emu.status_change()

class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def introduce(self):
        print("hello passent, my name is {} {}".format(self.firstname, self.lastname))

    def hurt(self,other):
        if self.weapon == "sword":
            other.health -= 10
        elif self.weapon == "gun":
            other.health -=20
        print("{} now has {} health".format(other.firstname, other.health))
    
    def insult(self,other):
        if other.health <= 50:
            print("{} is a weak {}".format(other.firstname, other.lastname))

    def steal(self,other):
        print("ha ha ha ,{} , i have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False
    

Alex = Enemy("sword", "Alex", "Hossain", 100, status=True)

print("///////////////////////////////////////////////////////")
Alex.introduce()
Alex.hurt(abir)
Alex.hurt(araf)
Alex.hurt(emu)
Alex.insult(abir)
Alex.insult(araf)
Alex.insult(emu)
Alex.steal(abir)
Alex.steal(araf)
Alex.steal(emu)


