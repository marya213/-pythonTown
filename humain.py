from abc import ABC, abstractmethod

class Humain(ABC):
    def __init__(self, nom, boisson_favorite="eau"):
        self.__nom = nom
        self.__boisson_favorite = boisson_favorite

    def parle(self, texte):
        print(f"{self.__nom} - {texte}")

    def presentation(self):
        print(f"{self.__nom} - Bonjour, je suis {self.__nom}, et j’aime le {self.__boisson_favorite}.")

    def boire(self):
        print(f"{self.__nom} - Ah ! un bon verre de {self.__boisson_favorite} ! GLOUPS !")

    def quelEstTonNom(self):
        return self.__nom

    def quelleEstTaBoisson(self):
        return self.__boisson_favorite

    @abstractmethod
    def manger(self):
        pass
