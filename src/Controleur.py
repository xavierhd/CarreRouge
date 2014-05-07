import Modele as fichierModele
import Vue as fichierVue

class Controleur(object):
    def __init__(self):
        super(Controleur, self).__init__()
        self.compteurDeLoop = 0
        self.isRunning = 0
        self.modele = None
        self.vue = fichierVue.Vue( self )
        self.vue.menu()
        self.vue.root.mainloop()

    def pause(self):
        if(self.isRunning):
            self.isRunning = 0
        else:
            self.isRunning = 1

    def menu(self, eventCode):
        if(eventCode == 1): #click bouton jouer
            self.modele = fichierModele.Modele()
            self.vue.mettreA_Jour( self.modele.listeForme )
            self.gameLoop()
        elif(eventCode == 2): #click bouton option
            pass
        elif(eventCode == 3): #click bouton high score
            self.afficherHighScore()
        elif(eventCode == 4): #click bouton quitter
            self.vue.root.destroy()

    def gameLoop(self):
        if(self.modele.listeForme[0].isNotDead(self.modele.listeForme)):
            self.compteurDeLoop += 1
            print("loop --> "+ str(self.compteurDeLoop))
            if self.isRunning:
                print("selfisrunning")
                self.modele.mettreA_Jour( self.vue.getPositionCarre() )
                self.vue.mettreA_Jour( self.modele.listeForme )
            self.vue.root.after(30,self.gameLoop)
        else:
            self.modele = None
            self.vue.premierClick = 1 
            self.vue.menu()

    def afficherHighScore(self):
        self.vue.menuHighScore(self.modele.getHighScore())

    def setHighScore(self,unNom):
        self.modele.setHighScore(unNom, self.temps)

            
if __name__ == '__main__':
    c=Controleur()