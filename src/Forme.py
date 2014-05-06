class Forme(object):    
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Forme, self).__init__()
        self.tag = []
        self.tag.extend(tag)
        self.listePointX = [x1,x2,x2,x1]
        self.listePointY = [y1,y1,y2,y2]
        self.couleur = couleur

    def estEnCollision(self, nbCoin = 4, listePointX, listePointY, x, y):
        i = -1
        etat = False
        while i < nbCoin-1:
            i+=1
            j = (i+1)%nbCoin
            if ((((listePointY[i]<=y) and (y<listePointY[j])) or ((listePointY[j]<=y) and (y<listePointY[i]))) and (x < (listePointX[j] - listePointX[i]) * (y - listePointY[i]) / (listePointY[j] - listePointY[i]) + listePointX[i])):
                etat = not etat
        return etat

    def checkCollision(self, listeForme):
        for forme in self.listeForme:
            for i in range(len(self.listePointX)):
                if(self.estEnCollision( len(forme.listePointX), forme.listePointX, forme.listePointY, self.listePointX[i], self.listePointY[i]):
                    return (True,forme)
        else:
            return (False,None)

    

            

class PieceDuJoueur(Forme):
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Forme, self).__init__(x1, y1, x2, y2, couleur, tag)

class Ennemi(Forme):
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Forme, self).__init__(x1, y1, x2, y2, couleur, tag)
        self.modDirX = None
        self.modDirY = None


    def rebondire(self, forme):
        if(forme.tag.count("droit") or forme.tag.count("gauche")):
            self.modDirX = -self.modDirX

	    if(forme.tag.count("bas") or forme.tag.count("haut")):
            self.modDirY = -self.modDirY


    def deplacer( self, listeForme ):
        (collision, forme) = self.checkCollision(listeForme)
        if(collision):
            self.rebondire(forme)
        else:
            changerPosition()

    def changerPosition(self):
        for point in listePointX:
            point += self.modDirX
        for point in listePointY:
            point += self.modDirY

class Bord(Ennemi):
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Forme, self).__init__(x1, y1, x2, y2, couleur, tag)