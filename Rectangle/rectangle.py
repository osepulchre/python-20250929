class Rectangle:
    def __init__(self, longueur:int, largeur:int):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self) -> int:
        return 2 * (self.longueur + self.largeur)
    
    def surface(self) -> int:
        return self.largeur*self.longueur
    
class Pave(Rectangle):
    def __init__(self, longueur:int, largeur:int, hauteur:int):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur
    
    def perimetre(self) -> int:
        return 2 * super().perimetre() + 4 * self.hauteur

    def surface(self) -> int:
        return 2 * super().surface() + self.hauteur * super().perimetre()
    
    def volume(self) -> int:
        return super().surface() * self.hauteur
    

if __name__ == '__main__':
    pave = Pave(3, 4, 5)
    print(f"perimetre: {pave.perimetre()}, surface: {pave.surface()}, volume: {pave.volume()}")

