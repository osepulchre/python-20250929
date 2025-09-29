from compteBancaire import CompteBancaire

compte = CompteBancaire(123456789, "Olivier", -437)
compte.afficher()

compte.versement(550)

compte.retrait(1000)

compte.agios()
