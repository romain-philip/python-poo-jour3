class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
        adversaire.vie -= 1

class Jeu:
    def __init__(self):
        self.niveau = None
        self.joueur = None
        self.ennemi = None

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1-3) : "))

    def lancerJeu(self):
        if self.niveau == 1:
            vie = 10
        elif self.niveau == 2:
            vie = 7
        else:
            vie = 5

        self.joueur = Personnage("Joueur", vie)
        self.ennemi = Personnage("Ennemi", vie)

    def verifierSante(self, personnage):
        return personnage.vie > 0

    def verifierGagnant(self):
        if not self.verifierSante(self.joueur):
            print("L'ennemi a gagné !")
        elif not self.verifierSante(self.ennemi):
            print("Le joueur a gagné !")

    def jouerTour(self):
        self.joueur.attaquer(self.ennemi)
        if self.verifierSante(self.ennemi):
            self.ennemi.attaquer(self.joueur)

    def jouerPartie(self):
        self.choisirNiveau()
        self.lancerJeu()

        while self.verifierSante(self.joueur) and self.verifierSante(self.ennemi):
            self.jouerTour()

        self.verifierGagnant()



jeu = Jeu()
jeu.jouerPartie()
