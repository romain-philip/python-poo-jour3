class Ville:
    def __init__(self, nom, population):
        self.__nom = nom
        self.__population = population

    def get_population(self):
        return self.__population

    def ajouter_population(self):
        self.__population += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_population()



paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)


print(f"Population de Paris : {paris.get_population()}")
print(f"Population de Marseille : {marseille.get_population()}")


john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)


print(f"Population de Paris après l'arrivée de nouvelles personnes : {paris.get_population()}")
print(f"Population de Marseille après l'arrivée de nouvelles personnes : {marseille.get_population()}")
