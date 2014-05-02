from tkinter import *

class Vue():
    def __init__(self, parent):
        super(Vue, self).__init__()
        self.parent = parent
        self.root = Tk()
        self.carrebouge = 0
        self.canevas = Canvas(self.root,width=600,height=600,bg="red")
        self.posCarreX = None
        self.posCarreY = None
        self.menu()

    def menu( self ):
    	pass
    def menuHighScore( self ):
    	pass
    def mettreA_Jour( self, listeForme ):
    	pass
    def initPartie( self, listeForme ):
    	pass

    def getPositionCarre( self ):
    	return (self.posCarreX, self.posCarreY)