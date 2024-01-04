class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"{self.nom} ({self.position}, numéro {self.numero}) a marqué {self.buts} buts, a effectué {self.passes_decisives} passes décisives, a reçu {self.cartons_jaunes} cartons jaunes et {self.cartons_rouges} cartons rouges.")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom, buts, passes_decisives, cartons_jaunes, cartons_rouges):
        for joueur in self.joueurs:
            if joueur.nom == nom:
                joueur.buts += buts
                joueur.passes_decisives += passes_decisives
                joueur.cartons_jaunes += cartons_jaunes
                joueur.cartons_rouges += cartons_rouges



joueur1 = Joueur("Mbappé", 7, "Attaquant")
joueur2 = Joueur("Pogba", 6, "Milieu")
joueur3 = Joueur("upamecano", 4, "Défenseur")


equipe = Equipe("France")


equipe.ajouterJoueur(joueur1)
equipe.ajouterJoueur(joueur2)
equipe.ajouterJoueur(joueur3)


equipe.afficherStatistiquesJoueurs()


equipe.mettreAJourStatistiquesJoueur("Mbappé", 1, 0, 0, 0)


equipe.afficherStatistiquesJoueurs()
