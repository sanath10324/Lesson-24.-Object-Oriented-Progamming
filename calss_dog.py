class Golden_retriver:
    species = "Dog"
    def __init__(self, name, age):
        self.name = name
        self.age = age

Rocky = Golden_retriver("Rocky", 12)
Bond = Golden_retriver("Bond", 16)

print("Rocky is a {}".format(Rocky.species))
print("Bond is also a {}".format(Bond.species))

print("{} is {} years old!".format(Rocky.name, Rocky.age))
print("{} is {} years old!".format(Bond.name, Bond.age))
