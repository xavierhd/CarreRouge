import random

class Forme(object):    
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Forme, self).__init__()
        self.tag = tag
        self.listePointX = [x1,x2,x2,x1]
        self.listePointY = [y1,y1,y2,y2]
        self.couleur = couleur
        self.cooldown = None

    def __eq__(self, other):
        if(other):
            for i in range(len(self.listePointX)):
                if(self.listePointX[i] == other.listePointX[i] and self.listePointY[i] == other.listePointY[i]):
                    continue
                else:
                    break
            else:
                if(self.tag == other.tag and self.couleur == other.couleur):
                    return True
        return False
    def deplacer( self, var ):
        pass#fonction a overider

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
            if(not forme == self):
                if(not (self.couleur == "blue" and forme.couleur == "blue" and forme.tag == self.tag)):
                    if(not forme.cooldown or not forme.cooldown[0] == self):
                        if (self.couleur == "blue" or self.couleur == "red"):
                            for i in range(len(self.listePointX)):
                                if(self.estEnCollision( len(forme.listePointX), forme.listePointX, forme.listePointY, self.listePointX[i], self.listePointY[i])):
                                    self.cooldown = (forme,2)
                                    forme.cooldown = (self,2)
                                    return forme
                    else:
                        if(forme.cooldown[1] == 0):
                            forme.cooldown = None
                        else:
                            forme.cooldown = (forme.cooldown[0], forme.cooldown[1] - 1)
        else:
            return None
"""self.estEnCollision( len(forme.listePointX), forme.listePointX, forme.listePointY, self.listePointX[i], self.listePointY[i])   self.estEnCollision2(self.listePointX[i],self.listePointY[i])"""

                  

class Joueur(Forme):
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Joueur, self).__init__(x1, y1, x2, y2, couleur, tag)
        self.anciennePosClickX = 300
        self.anciennePosClickY = 300


    def deplacer( self, position ):
        diffX = self.anciennePosClickX - position[0]
        diffY = self.anciennePosClickY - position[1]
        for i in range(4):
            self.listePointX[i]-= diffX
            self.listePointY[i]-= diffY

        self.anciennePosClickX = position[0]
        self.anciennePosClickY = position[1]

    def isNotDead( self, listeForme ):
        forme = self.checkCollision(listeForme)
        if(forme): return False  
        else: return True

class Automatique(Forme):
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Automatique, self).__init__(x1, y1, x2, y2, couleur, tag)
        self.modDirX = None
        self.modDirY = None
        self.initModDir()

    def initModDir( self ):
        while((self.modDirX == None or self.modDirX < 1) and (self.modDirY == None or self.modDirY < 1)):
            self.modDirX = random.randrange(17)-8
            self.modDirY = random.randrange(17)-8

    def rebondire( self, forme ):
        if(forme.tag.count("droit")):
            self.modDirX = -self.modDirX

        elif(forme.tag.count("gauche")):
            self.modDirX = -self.modDirX

        elif(forme.tag.count("bas")):
            self.modDirY = -self.modDirY

        elif(forme.tag.count("haut")):
            self.modDirY = -self.modDirY

        elif(forme.tag.count("centre")):
            self.modDirY = -self.modDirY
            self.modDirX = -self.modDirX
        else:
            tempx = self.modDirX
            tempy = self.modDirY
            self.modDirX = forme.modDirX
            forme.modDirX = tempx
            self.modDirY = forme.modDirY
            forme.modDirY = tempy

    def deplacer( self, listeForme ):
        forme = self.checkCollision(listeForme)
        if(forme):
            print("COLLISION!!!!",end=' ')
            self.rebondire(forme)
        self.changerPosition()

    def changerPosition( self):
        for i in range(4):
            self.listePointX[i]-= self.modDirX
            self.listePointY[i]-= self.modDirY