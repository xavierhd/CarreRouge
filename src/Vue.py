from tkinter import *

class Vue():
    def __init__(self, parent):
        super(Vue, self).__init__()
        self.parent = parent
        self.root = Tk()
        self.carrebouge = 0
        self.canevas = Canvas(self.root,width=600,height=600,bg="white")
        self.posCarreX = None
        self.posCarreY = None
        self.canevas.pack()
        self.canevas.bind("<Button-1>",self.gotclick)
        self.canevas.bind("<ButtonRelease>",self.forgotclick)
        self.canevas.bind("<Motion>",self.gotbouge)

    def gotbouge(self,event):
        if self.carrebouge:
            self.parent.carrebouge(evt.x,evt.y)
        
    def gotclick(self,event):
        lestags=self.canevas.gettags("current")
        if "carre" in lestags:
            self.carrebouge=1
            
    def forgotclick(self,event):
        self.carrebouge=0

    def menu( self ):
        self.boutonJouer = Button(self.root, text='Jouer',width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command= lambda: self.parent.menu(1))
        self.boutonJouer.place(width=100, x=100, y=100)

    def menuHighScore( self ):
        pass
    def mettreA_Jour( self, listeForme):
        self.canevas.delete("forme")
        for forme in listeForme:
            self.canevas.create_rectangle( forme.listePointX[0], forme.listePointY[0], forme.listePointX[2], forme.listePointY[2], fill=forme.couleur, tags=forme.tag )


    def initPartie( self, listeForme ):
        pass

    def getPositionCarre( self ):
        return (self.posCarreX, self.posCarreY)