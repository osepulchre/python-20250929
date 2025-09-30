class Gateau:
    """ classe gâteau """
    def __init__(self, nom_gateau: str, temps_cuisson: int, ingredients: list[str], etapes_recette: list[str], nom_createur: str):
        """ constructeur """
        self.nom_gateau = nom_gateau
        self.temps_cuisson = temps_cuisson
        self.ingredients = ingredients
        self.etapes_recette = etapes_recette
        self.nom_createur = nom_createur
    
    def affiche_ingredients(self):
        for ingredient in self.ingredients:
            print(f"{ingredient}")

mon_gateau = Gateau("gateau au chocolat", 10, ["farine", "beurre", "sucre", "chocolat", "oeufs"], ["verser", "mélanger", "cuire", "manger"], "moi")
mon_gateau2 = Gateau(nom_createur="pas moi", nom_gateau="gateau au chocolat", temps_cuisson=10, ingredients=["farine", "courgette", "sucre", "chocolat", "oeufs"], etapes_recette=["verser", "mélanger", "cuire", "manger"])

print(f"Ingrédients:")
mon_gateau.affiche_ingredients()

print(f"Etapes de la recette:")
for etape_recette in mon_gateau.etapes_recette:
    print(f"{etape_recette}")

print(f"Ingrédients:")
mon_gateau2.affiche_ingredients()

print(f"Etapes de la recette:")
for etape_recette in mon_gateau2.etapes_recette:
    print(f"{etape_recette}")

print(f"{Gateau.__doc__}")
print(f"{Gateau.__init__.__doc__}")
