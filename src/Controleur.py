import Modele as fichierModele
import Vue as fichierVue

class Controleur(object):
    def __init__(self):
        super(Controleur, self).__init__()
        self.isRunning = 0
        self.modele = None
        self.vue = fichierVue.Vue(self )
        self.vue.root.mainloop()

    def pause(self):
        if(self.isRunning):
            self.isRunning = 0
        else:
            self.isRunning = 1

    def menu(self, eventCode):
        if(eventCode == 1):#click bouton jouer
            self.modele = fichierModele.Modele()
            self.vue.initPartie( self.modele.listeForme )
            self.gameLoop()
        if(eventCode == 2):#click bouton option
            pass
        if(eventCode == 3):#click bouton high score
            self.afficherHighScore()
        if(eventCode == 4):#click bouton quitter
            self.vue.root.destroy()

    def gameLoop(self):
        if self.isRunning:
            self.modele.mettreA_Jour( self.vue.getPositionCarre() )
            self.vue.mettreA_Jour( self.modele.listeForme )
            self.vue.root.after(30,self.gameLoop)

    def afficherHighScore(self):
        self.vue.menuHighScore(self.modele.getHighScore())

    def setHighScore(self,unNom):
        self.modele.setHighScore(unNom)

            
if __name__ == '__main__':
    c=Controleur()