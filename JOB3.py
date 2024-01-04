class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut

    def get_statut(self):
        return self.__statut

    def set_statut(self, statut):
        self.__statut = statut

    def __str__(self):
        return f"{self.__titre} ({self.__statut}): {self.__description}"


class ListeDeTaches:
    def __init__(self):
        self.__taches = []

    def ajouterTache(self, tache):
        self.__taches.append(tache)

    def supprimerTache(self, tache):
        self.__taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.set_statut("terminer")

    def afficherListe(self):
        for tache in self.__taches:
            print(tache)

    def filterListe(self, statut):
        return [tache for tache in self.__taches if tache.get_statut() == statut]



tache1 = Tache("Faire les courses", "Acheter du fromage et du pain")
tache2 = Tache("Rendre le livre", "Rendre le livre à la bibliothèque")
tache3 = Tache("Préparer le dîner", "Préparer des lasagnes pour le dîner")


liste = ListeDeTaches()
liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)


liste.afficherListe()


liste.marquerCommeFinie(tache1)


print("Tâches à faire :")
for tache in liste.filterListe("à faire"):
    print(tache)


liste.supprimerTache(tache2)


liste.afficherListe()
