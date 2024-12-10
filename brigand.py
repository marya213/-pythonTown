from humain import Humain

class Brigand(Humain):
    def __init__(self, nom, look="méchant", dames_enlevees=0, recompense=100, en_prison=False):
        super().__init__(nom, boisson_favorite="tord-boyaux")
        self.look = look
        self.dames_enlevees = dames_enlevees
        self.recompense = recompense
        self.en_prison = en_prison

    def kidnapper(self, dame):
        print(f"{self.quelEstTonNom()} - Ah ah ! {dame.quelEstTonNom()}, tu es mienne désormais !")
        dame.se_faire_enlever()

    def se_faire_emprisonner(self, cowboy):
        self.en_prison = True
        print(f"{self.quelEstTonNom()} - Damned, je suis fait ! {cowboy.quelEstTonNom()}, tu m’as eu !")

    def presentation(self):
        super().presentation()
        print(f"{self.quelEstTonNom()} - J’ai l’air {self.look} et j’ai déjà kidnappé {self.dames_enlevees} dames !")
        print(f"{self.quelEstTonNom()} - Ma tête est mise à prix {self.recompense} $ !")

    def manger(self):
        print(f"{self.quelEstTonNom()} mange salement.")
