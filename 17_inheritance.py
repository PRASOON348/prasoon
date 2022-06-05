############INHERITANCE##########

class student:
    def work(self):
        print("He can write")
        print("He can read")
        print("He can play")

class sunny(student):
    def special_talent(self):
        print("He can dance")

class prasoon(student):
    def skills(self):
        print("He is a programmer!")

        
ps = prasoon()
ps.work()
ps.skills()