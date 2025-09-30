class Personne:
    def __init__(self, nom:str, prenom:str, tel:str, email:str):
        self.nom=nom
        self.prenom=prenom
        self.tel=tel
        self.email=email

    def __str__(self):
        return f"nom: {self.nom}, prénom: {self.prenom}, numéro de téléphone: {self.tel}, email: {self.email}"
    
class Travailleur(Personne):
    def __init__(self, nom: str, prenom: str, tel: str, email:str, entreprise: str, adresse_entreprise: str, tel_pro: str):
        super().__init__(nom, prenom, tel, email)
        self.entreprise = entreprise
        self.adresse_entreprise = adresse_entreprise
        self.tel_pro = tel_pro

    def __str__(self):
        return f"{super().__str__()}, entreprise: {self.entreprise}, adresse: {self.adresse_entreprise}, téléphone professionnel: {self.tel_pro}"
    
class Scientifique(Travailleur):
    def __init__(self, nom: str, prenom: str, tel: str, email:str, entreprise: str, adresse_entreprise: str, tel_pro: str, disciplines: list[str], types: list[str]):
        super().__init__(nom, prenom, tel, email, entreprise, adresse_entreprise, tel_pro)
        self.disciplines = disciplines
        self.types = types

    def __str__(self):
        return f"{super().__str__()}, disciplines: {"".join(discipline + "/" for discipline in self.disciplines)}, types: {"".join(type+"/" for type in self.types)}"
    
print(Scientifique("Lovelace", "Ada", "098765432", "ada@lovelace.org", "Babbage corp.", "London", "023456789", ["algorithmique", "mathématiques appliquées"], ["théorique", "informatique"]))
