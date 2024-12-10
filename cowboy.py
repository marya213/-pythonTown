from humain import Humain

class Cowboy(Humain):
    def __init__(self, nom, adjectif="vaillant"):
        super().__init__(nom, boisson_favorite="whisky")
        self.popularite = 0
        self.adjectif = adjectif

    def tirer_sur(self, brigand):
        print(f"Le {self.adjectif} {self.quelEstTonNom()} tire sur {brigand.quelEstTonNom()}. PAN !")
        self.parle("Prend ça, rascal !")

    def liberer(self, dame):
        print(f"{self.quelEstTonNom()} - Ne vous inquiétez pas, {dame.quelEstTonNom()}, vous êtes libre maintenant !")
        dame.se_faire_liberer()
        self.popularite += 1

    def presentation(self):
        super().presentation()
        print(f"{self.quelEstTonNom()} - On m’appelle {self.adjectif}, et j’ai une popularité de {self.popularite}.")

    def manger(self):
        print(f"{self.quelEstTonNom()} mange proprement.")
