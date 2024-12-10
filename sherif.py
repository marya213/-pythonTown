from cowboy import Cowboy

class Sherif(Cowboy):
    def __init__(self, nom):
        super().__init__(nom)
        self.brigands_coffres = 0

    def coffrer(self, brigand): 
        brigand.en_prison = True
        self.brigands_coffres += 1
        print(f"{self.quelEstTonNom()} - Au nom de la loi, je vous arrête !")

    def rechercher(self, brigand):
        print(f"{self.quelEstTonNom()} - OYEZ OYEZ BRAVE GENS !! {brigand.recompense} $ à qui arrêtera {brigand.quelEstTonNom()} mort ou vif !")

    def presentation(self):
        super().presentation()
        print(f"{self.quelEstTonNom()} - J’ai coffré {self.brigands_coffres} brigands.")

    def manger(self):
        print(f"{self.quelEstTonNom()} mange avec dignité.")
