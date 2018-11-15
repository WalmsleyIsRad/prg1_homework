class Dog:
    def __init__(self,initalname,age=0):
        self.name = initalname
        self.age = age

    def speak(self):
        print(self.name + " Rrruuffffffff!")

    def change_name(self,newname):
        self.name = newname

    def calculate_dog_years(self):
        return self.age * 7

    def walk(self,xdiff,ydiff):
        self.x += xdiff
        self.y += ydiff

    def fetch(self,ballx,bally):
        
        self.walk(ballx,bally)

    def celebrate_birthday(self):
        self.age +=1
        print("Happy birthday " + self.name)

fido = Dog("Fido",3)
fido.speak()
fido.celebrate_birthday()
fido.change_name("Remmy")
fido.speak()

rex = Dog("Rex",0)
rex.speak()
rex.celebrate_birthday()

thor = Dog("Thor",11)
thor.speak
thor.celebrate_birthday()