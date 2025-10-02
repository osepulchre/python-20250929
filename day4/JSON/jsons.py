import json, os

file_path="catalogue.json"

catalogue = {
        "produits": [
            {"id": 1, "nom": "Stylo", "prix": 1.8},
            {"id": 2, "nom": "Cahier", "prix": 2.5},
            {"id": 3, "nom": "Sac",   "prix": 19.9}
        ]
    }

with open("catalogue.json", "w", encoding="utf-8") as file:
    json.dump(catalogue, file, indent=2)

with open(file_path, "r") as file:
    catalogue2 = json.load(file)

prix_total = sum(produit["prix"] for produit in catalogue["produits"])

catalogue2["total"]=prix_total

print(json.dumps(catalogue2))

with open("catalogue_total.json", "w", encoding="utf-8") as file:
    json.dump(catalogue2, file, indent=2)

