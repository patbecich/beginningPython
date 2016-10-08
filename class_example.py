

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.daysLived = 0

    def calculateDaysLived(self):
        self.daysLived = 365*int(self.age)

    def describePerson(self):
        print("Name is ",self.name,", age is ",self.age,", and lived ", self.daysLived, " days")

    def addYears(self,years):
        self.age = self.age + years
        self.calculateDaysLived()




pat = Person("Pat", 22)

peter = Person("Peter", 24)

print pat
print peter

pat.calculateDaysLived()
pat.describePerson()
