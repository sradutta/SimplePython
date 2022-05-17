import operator

class Pets():
    def __init__(self,name,owner_name,pet_type,pet_age):
        self._name = name
        self.owner_name = owner_name
        self.pet_type = pet_type
        self.pet_age = pet_age

    name = property(operator.attrgetter("_name"))


Alpaca = Pets('Scruffy', 'Fred Jones', 'Alpaca', 8)
Alpaca.pet_age += 1
print(Alpaca.pet_age)

#check if Scruffy can be set to Timmy:
Alpaca.name = 'Timmy'
#No, we can't as we get the attribute error "can't set attribute name


