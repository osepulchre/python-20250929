class CompteBancaire:
    def __init__(self, numero_compte:int, nom:str, solde:int):
        self.numero_compte = numero_compte
        self.nom = nom
        self.solde = solde
    
    def versement(self, montant:int):
        self.solde += montant
        self.afficher()
        
    def retrait(self, montant:int):
        self.versement(-montant)
    
    def agios(self):
        if self.solde < 0:
            self.retrait(self.solde * 5 / 100)
        
    def afficher(self):
        print(f"{self.numero_compte} - {self.nom} : {self.solde}")

if __name__ == '__main__':
    compte = CompteBancaire(123456789, "Olivier", -437)
    compte.afficher()

    compte.versement(550)

    compte.retrait(1000)

    compte.agios()
