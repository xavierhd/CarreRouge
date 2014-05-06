import Forme as fichierForme


class Modele(object):
    def __init__( self, grandeurEspaceDeJeuX, grandeurEspaceDeJeuY ):
        super(Modele, self).__init__()
        self.listeForme = self.initForme()
        self.toi = fichierForme.PieceDuJoueur(x1, y1, x2, y2, couleur, tag)
        self.grandeurEspaceDeJeuX = grandeurEspaceDeJeuX
        self.grandeurEspaceDeJeuY = grandeurEspaceDeJeuY
        self.nbForme = 4

    def mettreA_Jour( self, x, y ):
        for forme in self.listeForme:
            if(forme.tag.count("mechant") and forme.tag.count("mobile"))
                forme.deplacer(self.listeForme)

    def initForme( self ):
        uneListe = []
        #ajout du joueur
        uneListe.append(fichierForme.PieceDuJoueur(self.grandeurEspaceDeJeuX/2-10, self.grandeurEspaceDeJeuX/2-10, self.grandeurEspaceDeJeuX/2+10, self.grandeurEspaceDeJeuY+10, "blue", ["mobile","gentil"]))
        #ajout des pieces adverses
        uneListe.append(fichierForme.Ennemi(self.grandeurEspaceDeJeuX/4, self.grandeurEspaceDeJeuY/4, self.grandeurEspaceDeJeuX/4+30, self.grandeurEspaceDeJeuY/4+30, "red", ["mobile","mechant"]))
        uneListe.append(fichierForme.Ennemi(self.grandeurEspaceDeJeuX/4*3, self.grandeurEspaceDeJeuY/4, self.grandeurEspaceDeJeuX/4*3+20, self.grandeurEspaceDeJeuY/4+50, "red", ["mobile","mechant"]))
        uneListe.append(fichierForme.Ennemi(self.grandeurEspaceDeJeuX/4, self.grandeurEspaceDeJeuY/4*3, self.grandeurEspaceDeJeuX/4+60, self.grandeurEspaceDeJeuY/4*3+20, "red", ["mobile","mechant"]))
        uneListe.append(fichierForme.Ennemi(self.grandeurEspaceDeJeuX/4*3, self.self.grandeurEspaceDeJeuY/4*3, self.grandeurEspaceDeJeuX/4*3+30, self.grandeurEspaceDeJeuY/4*3+50, "red", ["mobile","mechant"]))
        #Ajout des bordures
        uneListe.append(fichierForme.Bord(0, 0, 20, self.grandeurEspaceDeJeuY, "black", ["mechant","bord","haut"]))
        uneListe.append(fichierForme.Bord(0, 0, self.grandeurEspaceDeJeuX, 20, "black", ["mechant","bord","gauche"]))
        uneListe.append(fichierForme.Bord(0, self.grandeurEspaceDeJeuY, self.grandeurEspaceDeJeuX, self.grandeurEspaceDeJeuY-20, "black", ["mechant","bord","bas"]))
        uneListe.append(fichierForme.Bord(self.grandeurEspaceDeJeuX, 0, self.grandeurEspaceDeJeuX-20, self.grandeurEspaceDeJeuY, "black", ["mechant","bord","droit"]))

        return uneListe


    def getHighScore( self ):
        try:
            tampon = open("high.Score", 'r+')#rb == read binary
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
            tampon = open("high.Score", 'a')#ab == append
        except Exception as e:
            print(e)
            print("Tentative de création du fichier...")
            try:    #tentative d'ouverture du fichier en mode write
                tampon = open("high.Score", 'w+')#w == write
            except Exception as autreE:
                print(autreE)
        finally:
            if(tampon):
                name = name.rstrip()
                aEcrire = name + '-->' + str(self.points) + '\n'
                try:
                    tampon.write(aEcrire)
                except Exception as e:
                    print(e)
                else:
                    tampon.close()

            
        
		