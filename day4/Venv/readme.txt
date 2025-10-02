Création de l'envt virtuel:
	py -m venv .venv

Lancement de l'envt virtuel:
	 . .venv/Scripts/activate

	pip list
	
	pip install xxxxxxx
	
	pip uninstall xxxxxxx

Documentation des dépendances:
	pip freeze > requirements.txt

Récupération des dépendances:
	pip install -r requirements.txt

Sortie de l'envt virtuel:
	deactivate


/!\ ne pas livrer le .venv, l'ajouter au .gitignore
