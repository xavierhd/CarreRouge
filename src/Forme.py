import random

class Forme(object):    
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Forme, self).__init__()
        self.tag = ["forme"]
        self.tag.extend(tag)
        self.listePointX = [x1,x2,x2,x1]
        self.listePointY = [y1,y1,y2,y2]
        self.couleur = couleur

    def estEnCollision(self, nbCoin, listePointX, listePointY, x, y):
        i = -1
        etat = False
        while i < nbCoin-1:
            i+=1
            j = (i+1)%nbCoin
            if ((((listePointY[i]<=y) and (y<listePointY[j])) or ((listePointY[j]<=y) and (y<listePointY[i]))) and (x < (listePointX[j] - listePointX[i]) * (y - listePointY[i]) / (listePointY[j] - listePointY[i]) + listePointX[i])):
                etat = not etat
        return etat

    def checkCollision(self, listeForme):
        for forme in listeForme:
            if(forme != self):
                if not (forme.tag.count("mechant") and forme.tag.count("mobile")):
                    for i in range(len(self.listePointX)):
                        if(self.estEnCollision( len(forme.listePointX), forme.listePointX, forme.listePointY, self.listePointX[i], self.listePointY[i])):
                            return (True,forme)
        else:
            return (False,None)

                  

class Manuel(Forme):
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Manuel, self).__init__(x1, y1, x2, y2, couleur, tag)
        self.anciennePosClickX = 0
        self.anciennePosClickY = 0

    def updateCarre(self, position):
        diffX = self.anciennePosClickX - position[0]
        diffY = self.anciennePosClickY - position[1]
        for point in self.listePointX:
            point += diffX
        for point in self.listePointY:
            point += diffY

    def isNotDead( self, listeForme ):
        collision, forme = self.checkCollision(listeForme)
        print(collision)
        if(forme):
            print(forme.tag)
        if(collision): return False  
        else: return True

class Automatique(Forme):
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Automatique, self).__init__(x1, y1, x2, y2, couleur, tag)
        self.modDirX = None
        self.modDirY = None
        self.initModDir()

    def initModDir( self ):
        self.modDirX = random.randrange(9)-4
        self.modDirY = random.randrange(9)-4

    def rebondire( self, forme ):
        if(forme.tag.count("droit") or forme.tag.count("gauche")):
            self.modDirX = -self.modDirX

        if(forme.tag.count("bas") or forme.tag.count("haut")):
            self.modDirY = -self.modDirY


    def deplacer( self, listeForme ):
        (collision, forme) = self.checkCollision(listeForme)
        if(collision):
            self.rebondire(forme)
        self.changerPosition()

    def changerPosition( self ):
        for point in self.listePointX:
            point += self.modDirX
        for point in self.listePointY:
            point += self.modDirY