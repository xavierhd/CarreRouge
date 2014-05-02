class Forme(object):    
    def __init__(self, x1, y1, x2, y2, couleur):
        super(Forme, self).__init__()
        listePointX = [x1,x2,x2,x1]
        listePointY = [y1,y1,y2,y2]
        self.couleur = couleur
        self.vitesse = None

    def estEnCollision(self, nbCoin = 4, listePointX, listePointY, x, y):
        i = -1
        etat = False
        while i < nbCoin-1:
            i+=1
            j = (i+1)%nbCoin
            if ((((listePointY[i]<=y) and (y<listePointY[j])) or ((listePointY[j]<=y) and (y<listePointY[i]))) and (x < (listePointX[j] - listePointX[i]) * (y - listePointY[i]) / (listePointY[j] - listePointY[i]) + listePointX[i])):
                etat = not etat
        return etat

    def deplacer(self):
        pass

class PieceDuJoueur(Forme):
    def __init__(self, x1, y1, x2, y2, couleur):
        super(Forme, self).__init__(x1, y1, x2, y2, couleur)

class Enemie(Forme):
    def __init__(self, arg):
        super(Forme, self).__init__(x1, y1, x2, y2, couleur)