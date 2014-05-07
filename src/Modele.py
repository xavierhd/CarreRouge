import Forme as fichierForme


class Modele(object):
    def __init__( self, grandeurEspaceDeJeuX = 600, grandeurEspaceDeJeuY = 600 ):
        super(Modele, self).__init__()
        self.gEDJX = grandeurEspaceDeJeuX
        self.gEDJY = grandeurEspaceDeJeuY
        self.listeForme = self.initForme()
        self.nbForme = 4

    def mettreA_Jour( self, x, y ):
        for forme in self.listeForme:
            if(forme.tag.count("mechant") and forme.tag.count("mobile")):
                forme.deplacer(self.listeForme)

    def initForme( self ):
        uneListe = []
        #ajout du joueur
        uneListe.append(fichierForme.Manuel(self.gEDJX/2-10, self.gEDJX/2-10, self.gEDJX/2+10, self.gEDJY+10, "blue", ["mobile","gentil"]))
        #ajout des pieces adverses
        uneListe.append(fichierForme.Automatique(self.gEDJX/4, self.gEDJY/4, self.gEDJX/4+30, self.gEDJY/4+30, "red", ["mobile","mechant"]))
        uneListe.append(fichierForme.Automatique(self.gEDJX/4*3, self.gEDJY/4, self.gEDJX/4*3+20, self.gEDJY/4+50, "red", ["mobile","mechant"]))
        uneListe.append(fichierForme.Automatique(self.gEDJX/4, self.gEDJY/4*3, self.gEDJX/4+60, self.gEDJY/4*3+20, "red", ["mobile","mechant"]))
        uneListe.append(fichierForme.Automatique(self.gEDJX/4*3, self.gEDJY/4*3, self.gEDJX/4*3+30, self.gEDJY/4*3+50, "red", ["mobile","mechant"]))
        #Ajout des bordures
        uneListe.append(fichierForme.Manuel(0, 0, 20, self.gEDJY, "black", ["mechant","bord","haut"]))
        uneListe.append(fichierForme.Manuel(0, 0, self.gEDJX, 20, "black", ["mechant","bord","gauche"]))
        uneListe.append(fichierForme.Manuel(0, self.gEDJY, self.gEDJX, self.gEDJY-20, "black", ["mechant","bord","bas"]))
        uneListe.append(fichierForme.Manuel(self.gEDJX, 0, self.gEDJX-20, self.gEDJY, "black", ["mechant","bord","droit"]))

        return uneListe


    def getHighScore( self ):
        try:
            tampon = open("high.Score", 'r')#r == read
            highScore = tampon.readlines()
            tampon.close()
            return highScore
        except Exception as e:
            print(e)
            print("Il y a de forte chance que votre fichier n'existe tout simplement pas encore. Allez jouer quelques parties et enregistrez votre score pour remédier à la situation!")
            return None



    def setHighScore( self, name ):
        tampon = None
        try:   #tentative d'ouverture du fichier en mode append
            tampon = open("high.Score", 'a+')#a == append / + == create
            name = name.rstrip()
            aEcrire = name + '-->' + str(self.points) + '\n'
            try:
                tampon.write(aEcrire)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        finally:
            if(tampon):
                tampon.close()

            
        
		