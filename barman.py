from humain import Humain

class Barman(Humain):
    def __init__(self, nom, nom_bar=None):
        super().__init__(nom, boisson_favorite="vin")
        self.nom_bar = nom_bar if nom_bar else f"Chez {nom}"

    def presentation(self):
        super().presentation()
        print(f"{self.quelEstTonNom()} - Bienvenue au bar {self.nom_bar} !")

    def parle(self, texte):
        print(f"{self.quelEstTonNom()} - {texte} Coco.")

    def servir(self, client):
        print(f"{self.quelEstTonNom()} - Un verre de {client.quelleEstTaBoisson()} pour toi, {client.quelEstTonNom()} !")

    def manger(self):
        print(f"{self.quelEstTonNom()} mange en discutant.")
