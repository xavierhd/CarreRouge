from tkinter import *

class Vue(object):
    def __init__(self, parent):
        super(Vue, self).__init__()
        self.parent = parent
        self.root = Tk()
        self.carrebouge = 0
        self.canevas = Canvas(self.root,width=600,height=600,bg="white")
        self.posCarre = None
        self.premierClick = 1
        self.canevas.pack()
        self.canevas.bind("<Button-1>",self.gotclick)
        self.canevas.bind("<ButtonRelease>",self.forgotclick)
        self.canevas.bind("<Motion>",self.gotbouge)
        self.boutonJouer = Button(self.root, text='Jouer',width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command= lambda: self.parent.menu(1))
        self.boutonOption = Button(self.root, text='Option',width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command= lambda: self.parent.menu(2))
        self.boutonQuitter = Button(self.root, text='Quitter', width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command= lambda: self.parent.menu(4))
        self.boutonRetourMenu = Button(self.root, text='Retour au menu', width=70, bg='black', fg='white',activebackground='black', activeforeground='white', command=self.menu)
        self.boutonRetourMenu2 = Button(self.root, text='Retour au menu', width=70, bg='black', fg='white',activebackground='black', activeforeground='white', command= lambda: self.menu( self.parent.setDifficulte( self.slider.get() ) ))
        self.boutonSave = Button(self.root, text='Save', width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command= lambda: self.parent.setHighScore(self.entryWidget.get()))
        self.boutonHighScore = Button(self.root, text='HighScore', width=50, bg='black', fg='white',activebackground='black', activeforeground='white', command= lambda: self.parent.menu(3))
        self.splashBox = Text(width=600, bg='black', fg='white', font=('Arial', 18))
        self.textBox = Text(width=600, bg='black', fg='white', font=('Arial', 18))
        self.entryWidget = Entry(self.root)


    def gotbouge(self,event):
        if self.carrebouge:
            self.posCarre = (event.x, event.y)
        
    def gotclick(self,event):
        lestags=self.canevas.gettags("current")
        if "joueur" in lestags:
            if self.premierClick:
                self.premierClick=0
                self.parent.pause()
            self.carrebouge=1
            
    def forgotclick(self,event):
        self.carrebouge=0

    def menu( self, val = None ):
        self.cleanMenu()
        self.boutonJouer.place(width=100, x=250, y=200)
        self.boutonOption.place(width=100, x=250, y=250)
        self.boutonHighScore.place(width=100, x=250, y=300)
        self.boutonQuitter.place(width=100, x=250, y=350)

    def entrerScore( self ):
        self.cleanMenu()
        
        self.splashBox.delete(1.0, END)
        self.splashBox.place(height=450, x=0, y=0)
        self.splashBox.insert(INSERT,"Fin de la partie, Entrez votre nom :")
        
        
        self.entryWidget.place(height=40, x=10, y=self.root.winfo_height()/2-100)
        self.entryWidget.delete(0, END)
        
        self.boutonSave.place(width=100, x=250, y=500)
        
        self.root.update()
        

    def menuHighScore( self, listeDeScore ):
        self.cleanMenu()
        self.canevas.delete("all")
        self.boutonRetourMenu.place(width=130, x=250, y=500)
        
        self.textBox.place(height=400, x=0, y=0)
        self.textBox.delete(1.0, END)
        self.textBox.insert(INSERT,"High Score\n")

        for i in listeDeScore:
            self.textBox.insert(INSERT, i)

    def menuOption( self ):
        self.cleanMenu()
        self.splashBox.delete(1.0, END)
        self.splashBox.place(height=450, x=0, y=0)
        self.splashBox.insert(INSERT,"Option :")
        self.slider = Scale(self.root,from_=1,to=4, orient=HORIZONTAL,label="Difficulté du jeu :", bg='gray40',length=250)
        slider_dansCanvas = self.canevas.create_window(150,100,window=self.slider,tags=('slider'))
        self.boutonRetourMenu2.place(width=130, x=250, y=510)


    def cleanMenu( self ):
        self.canevas.delete("all")
        self.boutonJouer.pack_forget()
        self.boutonJouer.place_forget()
        self.boutonOption.pack_forget()
        self.boutonOption.place_forget()
        self.boutonHighScore.pack_forget()
        self.boutonHighScore.place_forget()
        self.boutonQuitter.pack_forget()
        self.boutonQuitter.place_forget()
        self.boutonSave.pack_forget()
        self.boutonSave.place_forget()
        self.boutonRetourMenu.pack_forget()
        self.boutonRetourMenu.place_forget()
        self.splashBox.pack_forget()
        self.splashBox.place_forget()
        self.textBox.pack_forget()
        self.textBox.place_forget()
        self.entryWidget.pack_forget()
        self.entryWidget.place_forget()
        self.boutonRetourMenu2.pack_forget()
        self.boutonRetourMenu2.place_forget()

    def mettreA_Jour( self, listeForme):
        self.canevas.delete("all")
        if(self.premierClick):
            self.cleanMenu()
        for forme in listeForme:
            if(len(forme.listePointX)==4):
                self.canevas.create_rectangle( forme.listePointX[0], forme.listePointY[0], forme.listePointX[2], forme.listePointY[2], fill=forme.couleur, tags="joueur" )

    def getPositionCarre( self ):
        pos = self.posCarre
        self.posCarre = None
        return pos