from volDirect import Vol_direct
class Vols:
    def __init__(self, vols:list[Vol_direct]):
        self.vols=vols
        self.vols_par_depart={}
        self.vols_par_arrivee={}
        for vol in vols:
            if not vol.depart in self.vols_par_depart:
                self.vols_par_depart[vol.depart] = []
            self.vols_par_depart[vol.depart].append(vol)
            if not vol.arrivee in self.vols_par_arrivee:
                self.vols_par_arrivee[vol.arrivee] = []
            self.vols_par_arrivee[vol.arrivee].append(vol)
    
    def liste_successeurs(self, depart:str):
        if depart in self.vols_par_depart:
            for vol in self.vols_par_depart[depart]:
                print(vol.arrivee)

    def appartient(self, ville:str):
        return ville in self.vols_par_arrivee or ville in self.vols_par_depart
    
    def affiche(self):
        for vol in self.vols:
            vol.affiche()

if __name__ == '__main__':
    vols=Vols([Vol_direct("Paris", "Marseille", "lundi", 9), Vol_direct("Paris", "Toulouse", "mardi", 15), Vol_direct("Bordeaux", "Paris", "jeudi", 7), Vol_direct("Lille", "Bordeaux", "mercredi", 20)])
    vols.liste_successeurs("Paris")

    print(vols.appartient("Marseille"))
    print(vols.appartient("Nantes"))
    print(vols.appartient("Paris"))

    vols.affiche()