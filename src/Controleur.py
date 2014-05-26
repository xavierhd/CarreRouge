import Modele as fichierModele
import Vue as fichierVue

class Controleur(object):
    def __init__( self ):
        super(Controleur, self).__init__()
        self.compteurDeLoop = 0
        self.isRunning = 0
        self.modele = None
        self.vue = fichierVue.Vue( self )
        self.modele = fichierModele.Modele()
        self.vue.menu()
        self.vue.root.mainloop()

    def pause( self ):
        if(self.isRunning):
            self.isRunning = 0
        else:
            self.isRunning = 1

    def menu( self, eventCode ):
        if(eventCode == 1): #click bouton jouer
            self.modele.initialiserPartie()
            self.vue.mettreA_Jour( self.modele.listeForme )
            self.gameLoop()
        elif(eventCode == 2): #click bouton option
            self.vue.menuOption()
        elif(eventCode == 3): #click bouton high score
            self.vue.menuHighScore( self.modele.getHighScore() )
        elif(eventCode == 4): #click bouton quitter
            self.vue.root.destroy()

    def gameLoop( self ):
        if(self.modele.listeForme[0].isNotDead( self.modele.listeForme) ):
            if self.isRunning:
                self.compteurDeLoop += 1
                print("loop --> "+ str(self.compteurDeLoop),end=' ')
                self.modele.mettreA_Jour( self.vue.getPositionCarre() )
                self.vue.mettreA_Jour( self.modele.listeForme )
                print('')
            self.vue.root.after(30,self.gameLoop)
        else:
            print("vous etes mort!!! tantantan!!!")
            self.vue.entrerScore()
            self.vue.premierClick = 1 
            self.pause()

    def setHighScore( self, nom ):
        self.modele.setHighScore( nom, self.compteurDeLoop )
        self.vue.menu()

    def setDifficulte( self,  difficulte ):
        self.modele.difficulte = difficulte

            
if __name__ == '__main__':
    c=Controleur()
