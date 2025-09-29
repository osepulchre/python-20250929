class Watertank:
    volume_total:float = 0

    def __init__(self, poids_a_vide:float, capacite_max:float, niveau_de_remplissage:float = 0):
        self.poids_a_vide = poids_a_vide
        self.capacite_max = capacite_max
        self.niveau_de_remplissage = niveau_de_remplissage
        Watertank.volume_total += niveau_de_remplissage

    @property
    def poids_total(self):
        return self.poids_a_vide + self.niveau_de_remplissage
    
    def remplir(self, volume):
        Watertank.volume_total -= self.niveau_de_remplissage
        self.niveau_de_remplissage += volume
        if self.niveau_de_remplissage > self.capacite_max:
            self.niveau_de_remplissage = self.capacite_max
        Watertank.volume_total += self.niveau_de_remplissage
        
    
    def vider(self, volume):
        Watertank.volume_total -= self.niveau_de_remplissage
        self.niveau_de_remplissage += volume
        if self.niveau_de_remplissage < 0:
            self.niveau_de_remplissage = 0
        Watertank.volume_total += self.niveau_de_remplissage

    def __str__(self):
        return f"Poids à vide : {self.poids_a_vide} kg, poids total : {self.poids_total} kg, niveau de remplissage : {self.niveau_de_remplissage} l/{self.capacite_max} l"

if __name__ == '__main__':
    watertank1 = Watertank(500, 2000, 1000)
    watertank2 = Watertank(400, 1500)
    watertank2.remplir(800)
    print(watertank1)
    print(watertank2)
    print(f"Volume total : {Watertank.volume_total} l")
