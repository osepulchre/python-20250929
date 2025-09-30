class Chien:
    # ceci est un commentaire, la ligne suivante est une docstring
    """ Représentation d'un chien """
    # constructeur. Méthode Dunder ou Magique : double underscore au début et à la fin du nom
    def __init__(self, nom, age, race):
        self.nom = nom
        self.age = age
        self.race = race
    
    # self est l'instance. Obligatoire dans la définition de la méthode. 
    def aboyer(self):
        print(f"Wouf Wouf {self.nom}")
        
    def __repr__(self):
        return f"{self.nom} est un {self.race} de {self.age} an(s)"
    
#    def __str__(self):
#        return f"x{self.nom}  est un {self.race} de {self.age} an(s)"
        
toutou = Chien("Miya", 9, "chihuahua")
toutou.aboyer()
print(f"{toutou}")
toutous = [toutou, Chien("Pythagore", 2, "beagle")]
print(f"{toutous}")
