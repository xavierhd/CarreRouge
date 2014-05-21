import random

class Forme(object):    
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Forme, self).__init__()
        self.tag = tag
        self.listePointX = [x1,x2,x2,x1]
        self.listePointY = [y1,y1,y2,y2]
        self.couleur = couleur

    def __eq__(self, other): 
        for i in range(len(self.listePointX)):
            if(self.listePointX[i] == other.listePointX[i] and self.listePointY[i] == other.listePointY[i]):
                continue
            else:
                break
        else:
            return True
        return False


    def estEnCollision(self, nbCoin, listePointX, listePointY, x, y):
        i = -1
        etat = False
        while i < nbCoin-1:
            i+=1
            j = (i+1)%nbCoin
            if ((((listePointY[i]<=y) and (y<listePointY[j])) or ((listePointY[j]<=y) and (y<listePointY[i]))) and (x < (listePointX[j] - listePointX[i]) * (y - listePointY[i]) / (listePointY[j] - listePointY[i]) + listePointX[i])):
                etat = not etat
        return etat

    '''def estEnCollision2( self, x, y ):
        print("ICI EN COLLISION ------------------------------")
        if(x > self.listePointX[0]):
            return True
            
        elif(x < self.listePointX[1]):
            return True
        
        elif(y > self.listePointY[0]):
            return True
        
        elif(y < self.listePointY[2]):
            return True
        
        return False'''

    def checkCollision(self, listeForme):
        for forme in listeForme:
            if(not forme == self):
                if (self.couleur == "blue" and not forme.tag.count("mobile") or self.couleur == "red" and forme.tag.count("mechant")):
                    for i in range(len(self.listePointX)):
                        if(self.estEnCollision( len(forme.listePointX), forme.listePointX, forme.listePointY, self.listePointX[i], self.listePointY[i])):
                            return forme
        else:
            return None
"""self.estEnCollision( len(forme.listePointX), forme.listePointX, forme.listePointY, self.listePointX[i], self.listePointY[i])   self.estEnCollision2(self.listePointX[i],self.listePointY[i])"""

                  

class Manuel(Forme):
    def __init__(self, x1, y1, x2, y2, couleur, tag):
        super(Manuel, self).__init__(x1, y1, x2, y2, couleur, tag)
        self.anciennePosClickX = 300
        self.anciennePosClickY = 300


    def updateCarre(self, position):
        diffX = self.anciennePosClickX - position[0]
        diffY = self.anciennePosClickY - position[1]
        for i in range(4):
            self.listePointX[i]-= diffX
            self.listePointY[i]-= diffY
        '''
        for point in self.listePointX:
            print(point)
            point += diffX
            print(point)
        for point in self.listePointY:
            point += diffY
        '''
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
        self.modDirX = random.randrange(15)-7
        self.modDirY = random.randrange(15)-7

    def rebondire( self, forme ):
        if(forme.tag.count("droit")):
            self.modDirX = -self.modDirX

        if(forme.tag.count("gauche")):
            self.modDirX = -self.modDirX

        if(forme.tag.count("bas")):
            self.modDirY = -self.modDirY

        if(forme.tag.count("haut")):
            self.modDirY = -self.modDirY


    def deplacer( self, listeForme ):
        forme = self.checkCollision(listeForme)
        if(forme):
            print("COLLISION!!!!")
            self.rebondire(forme)
        self.changerPosition()

    def changerPosition( self):
        for i in range(4):
            self.listePointX[i]-= self.modDirX
            self.listePointY[i]-= self.modDirY