from contact import Contact
class Notebook:
    def __init__(self, dictionnaire:dict[str, Contact]={}):
        self.dictionnaire = dictionnaire


    def add(self, name, email, street, city):
        self.dictionnaire[name] = Contact(street, city, name, email)

    def show(self):
        for key in self.dictionnaire.keys():
            self.dictionnaire[key].show()

if __name__ == '__main__':
    notebook = Notebook()
    notebook.show()
    notebook.add("Sepulchre Olivier", "olivier@sepulch.re", "rond-point du Pont de Sèvres", "Boulogne-Billancourt")
    notebook.add("Alaoui Mohammed", "mohammed@alao.ui", "rond-point du Pont de Sèvres", "Boulogne-Billancourt")
    notebook.show()
