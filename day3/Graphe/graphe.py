from short_path import short_path

class Noeud:
    def __init__(self, nom:str):
        self.arcs_sortants=[]
        self.nom=nom

    @property
    def out_edges(self):
        return self.arcs_sortants
    
    def ajouter_arc(self, arc):
        self.arcs_sortants.append(arc)
    
    def __repr__(self):
        return self.nom

class Arc:
    def __init__(self, origine: Noeud, cible: Noeud, moyen: str, prix: int, duree: int):
        self.noeud_origine=origine
        self.noeud_cible=cible
        self.moyen_de_transport=moyen
        self.prix = prix
        self.duree = duree
        origine.ajouter_arc(self)
    
    @property
    def head(self):
        return self.noeud_cible
    
    @property
    def tail(self):
        return self.noeud_origine
    
    def __repr__(self):
        return f"{self.noeud_origine} -> {self.noeud_cible} : {self.moyen_de_transport}, {self.prix} €, {self.duree} minutes"

lille = Noeud("Lille")
paris = Noeud("Paris")
strasbourg = Noeud("Strasbourg")
lyon = Noeud("Lyon")

print("")
print(Arc(lyon, paris, "train", 100, 120))
print(Arc(lyon, strasbourg, "train", 50, 160))
print(Arc(paris, lille, "train", 60, 60))
print(Arc(paris, lille, "bus", 10, 100))
print(Arc(strasbourg, lille, "bus", 20, 180))
print()

chemin_plus_rapide,duree_min=short_path(lyon, lille, lambda arc : arc.duree)
print(f"Trajet le plus rapide: {duree_min} minutes, {chemin_plus_rapide}")
chemin_moins_cher,prix_min=short_path(lyon, lille, lambda arc : arc.prix)
print(f"Trajet le moins cher: {prix_min} €, {chemin_moins_cher}")