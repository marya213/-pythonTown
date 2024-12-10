from humain import Humain

class Dame(Humain):
    def __init__(self, nom, robe="rouge"):
        super().__init__(nom, boisson_favorite="lait")
        self.robe = robe
        self.libre = True

    def se_faire_enlever(self):
        self.libre = False
        print(f"{self.quelEstTonNom()} - Au secours !")

    def se_faire_liberer(self):
        self.libre = True
        print(f"{self.quelEstTonNom()} - Merci, mon héros !")

    def changer_de_robe(self, nouvelle_couleur):
        self.robe = nouvelle_couleur
        print(f"{self.quelEstTonNom()} - Regardez ma nouvelle robe {self.robe} !")

    def presentation(self):
        super().presentation()
        print(f"{self.quelEstTonNom()} - Ma robe est de couleur {self.robe}.")

    def manger(self):
        print(f"{self.quelEstTonNom()} mange délicatement.")
