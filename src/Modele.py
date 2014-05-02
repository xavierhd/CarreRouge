class Modele(object):
    def __init__( self, grandeurEspaceDeJeuX, grandeurEspaceDeJeuY ):
        super(Modele, self).__init__()
        self.listeObjet = []
        self.initObjet()
        self.toi = PieceDuJoueur()

    def mettreA_Jour( self, x, y ):
        for objet in listeObjet:
            objet.deplacer()


    def initObjet( self ):
        pass




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

            
        
		