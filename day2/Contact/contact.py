from address import Address
from person import Person

class Contact(Address, Person):
    def __init__(self, street: str, city: str, name: str, email: str):
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)

    def show(self):
        Person.show(self)
        Address.show(self)
    
if __name__ == '__main__':
    Contact("rond-point du Pont de Sèvres", "Boulogne-Billancourt", "Sepulchre Olivier", "olivier@sepulch.re").show()
