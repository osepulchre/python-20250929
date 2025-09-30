class Vol_direct:
    def __init__(self, depart: str, arrivee: str, jour: str, heure: int):
        self.depart = depart
        self.arrivee = arrivee
        self.jour = jour
        self.heure = heure
    
    def __str__(self):
        return f"Ce vol part de {self.depart} vers {self.arrivee} le {self.jour} à {self.heure} heure"
    
    def affiche(self):
        print(self)

if __name__ == '__main__':
    print(Vol_direct("Paris", "Marseille", "lundi", "9"))