from humain import Humain
from brigand import Brigand
from cowboy import Cowboy
from dame import Dame
from barman import Barman
from sherif import Sherif

# Création des personnages 
dame = Dame("Evelyne", robe="bleue")
brigand = Brigand("Bob", look="dangereux")
cowboy = Cowboy("John", adjectif="brave")
barman = Barman("Joe")
sherif = Sherif("Wyatt")

# Scénario 
dame.presentation()
dame.changer_de_robe("verte")
brigand.kidnapper(dame)
cowboy.liberer(dame)
sherif.coffrer(brigand)
sherif.rechercher(brigand)
barman.servir(cowboy)

# Les personnages mangent 
dame.manger()
brigand.manger()
cowboy.manger()
barman.manger()
sherif.manger()
