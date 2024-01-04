class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte: {self.__numero_compte}, Nom: {self.__nom}, Prénom: {self.__prenom}, Solde: {self.__solde}")

    def afficherSolde(self):
        print(f"Solde: {self.__solde}")

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur: Solde insuffisant")
        else:
            self.__solde -= montant
            self.afficherSolde()

    def agios(self):
        if self.__solde < 0:
            self.__solde *= 1.05  

    def virement(self, compte, montant):
        if self.__solde - montant < 0 and not self.__decouvert:
            print("Erreur: Solde insuffisant pour effectuer le virement")
        else:
            self.__solde -= montant
            compte.versement(montant)
            print("Virement effectué avec succès")



compte1 = CompteBancaire("123456", "Dupont", "Jean", 1000, False)
compte2 = CompteBancaire("654321", "Durand", "Pierre", -500, True)


compte1.afficher()
compte1.afficherSolde()
compte1.versement(200)
compte1.retrait(1500)
compte1.agios()
compte1.virement(compte2, 500)

compte2.afficher()
compte2.afficherSolde()
compte2.versement(200)
compte2.retrait(1500)
compte2.agios()
compte2.virement(compte1, 500)
