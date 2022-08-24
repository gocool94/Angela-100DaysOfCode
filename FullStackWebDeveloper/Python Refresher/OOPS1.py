class student:
    def __init__(self,name):
        self.name = name
        self.age = 26

    def average(self):
        print(self.age)
        print(self.name)

    def __str__(self):
        return "the users are getting aggregated"



s1 = student('gokul')
s1.average()

print(s1)