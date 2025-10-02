import json, os

file_path="catalogue.json"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        catalogue = json.load(file)
else:
    catalogue = {
        "produits": [
            {"id": 1, "nom": "Stylo", "prix": 1.8},
            {"id": 2, "nom": "Cahier", "prix": 2.5},
            {"id": 3, "nom": "Sac",   "prix": 19.9}
        ]
    }
    with open("catalogue.json", "w", encoding="utf-8") as file:
        json.dump(catalogue, file, indent=2)

prix_total=0
for produit in catalogue["produits"]:
    prix_total += produit["prix"]

catalogue["total"]=prix_total

print(json.dumps(catalogue))

with open("catalogue_total.json", "w", encoding="utf-8") as file:
        json.dump(catalogue, file, indent=2)

