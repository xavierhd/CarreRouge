import Forme as fichierForme


class Modele(object):
    def __init__( self, grandeurEspaceDeJeuX = 600, grandeurEspaceDeJeuY = 600 ):
        super(Modele, self).__init__()
        self.gEDJX = grandeurEspaceDeJeuX
        self.gEDJY = grandeurEspaceDeJeuY
        self.listeForme = None
        self.difficulte = 1

    def initialiserPartie( self ):
        self.listeForme = self.initForme()

    def mettreA_Jour( self, nouvellePositionJoueur ):
        for forme in self.listeForme:
            if(forme.tag.count( "joueur" )):
                if(nouvellePositionJoueur is not None):
                    print('('+str(nouvellePositionJoueur[0])+','+str(nouvellePositionJoueur[1])+')',end=' ')
                    forme.deplacer( nouvellePositionJoueur )
                continue
            else:
                forme.deplacer( self.listeForme )

    def initForme( self ):
        uneListe = []
        
        #ajout du joueur
        uneListe.append(fichierForme.Joueur(self.gEDJX/2-10, self.gEDJX/2-10, self.gEDJX/2+10, self.gEDJY/2+10, "red", ("mobile","gentil", "joueur")))
        
        #ajout des pieces adverses
        for i in range(self.difficulte):
            uneListe.append(fichierForme.Automatique(self.gEDJX/4, self.gEDJY/4, self.gEDJX/4+60, self.gEDJY/4+60, "blue", ("1","mobile","mechant")))
            uneListe.append(fichierForme.Automatique(self.gEDJX/4*3, self.gEDJY/4, self.gEDJX/4*3+80, self.gEDJY/4+120, "blue", ("2","mobile","mechant")))
            uneListe.append(fichierForme.Automatique(self.gEDJX/4, self.gEDJY/4*3, self.gEDJX/4+80, self.gEDJY/4*3+30, "blue", ("3","mobile","mechant")))
            uneListe.append(fichierForme.Automatique(self.gEDJX/4*3, self.gEDJY/4*3, self.gEDJX/4*3+70, self.gEDJY/4*3+70, "blue", ("4","mobile","mechant")))
            
        #Ajout des blocs centraux
        uneListe.append(fichierForme.Forme(self.gEDJX/2-90, self.gEDJX/2-100, self.gEDJX/2-30, self.gEDJY/2+10, "black", ("mechant","bord","centre")))
        
        #Ajout des bordures
        uneListe.append(fichierForme.Forme(-100, -100, 20, self.gEDJY, "black", ("mechant","bord","gauche")))
        uneListe.append(fichierForme.Forme(-100, -100, self.gEDJX, 20, "black", ("mechant","bord","haut")))
        uneListe.append(fichierForme.Forme(-100, self.gEDJY+100, self.gEDJX, self.gEDJY-20, "black", ("mechant","bord","bas")))
        uneListe.append(fichierForme.Forme(self.gEDJX+100, -100, self.gEDJX-20, self.gEDJY, "black", ("mechant","bord","droit")))

        return uneListe


    def getHighScore( self ):
        try:
            tampon = open("high.Score", 'r')#r == read
            highScore = tampon.readlines()
            tampon.close()
            return highScore
        except Exception as e:
            print(e)
            return "Il n'y a pas encore de highScores...\n\nA vous de jouer!!!"



    def setHighScore( self, name, temps ):
        try:   #tentative d'ouverture du fichier en mode append
            tampon = open("high.Score", 'a+')#a == append / + == create
            name = name.rstrip()
            aEcrire = str(name) + ' --> ' + str(temps*self.difficulte) + '\n'
            tampon.write(aEcrire)
            tampon.close()
        except Exception as e:
            print(e)
                

            
        
		