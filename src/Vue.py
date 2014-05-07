from tkinter import *

class Vue(object):
    def __init__(self, parent):
        super(Vue, self).__init__()
        self.parent = parent
        self.root = Tk()
        self.carrebouge = 0
        self.canevas = Canvas(self.root,width=600,height=600,bg="white")
        self.posCarre = []
        self.posCarre.append(0)
        self.posCarre.append(0)
        self.premierClick = 1
        self.canevas.pack()
        self.canevas.bind("<Button-1>",self.gotclick)
        self.canevas.bind("<ButtonRelease>",self.forgotclick)
        self.canevas.bind("<Motion>",self.gotbouge)

    def gotbouge(self,event):
        if self.carrebouge:
            self.posCarre[0] = event.x
            self.posCarre[1] = event.y
        
    def gotclick(self,event):
        lestags=self.canevas.gettags("current")
        if "joueur" in lestags:
            if self.premierClick:
                self.premierClick=0
                self.parent.pause()
            self.carrebouge=1
            
    def forgotclick(self,event):
        self.carrebouge=0

    def menu( self ):
        self.canevas.delete("all")
        self.boutonJouer = Button(self.root, text='Jouer',width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command= lambda: self.parent.menu(1))
        self.boutonJouer.place(width=100, x=100, y=100)

    def menuHighScore( self ):
        pass
    def mettreA_Jour( self, listeForme):
        self.boutonJouer.pack_forget()
        self.boutonJouer.place_forget()
        self.canevas.delete("forme")
        for forme in listeForme:
            print(len(forme.listePointX))
            if(len(forme.listePointX)==4):
                print("JE RENTRE WOOOOWWW")
                self.canevas.create_rectangle( forme.listePointX[0], forme.listePointY[0], forme.listePointX[2], forme.listePointY[2], fill=forme.couleur, tags=forme.tag )

    def getPositionCarre( self ):
        return self.posCarre