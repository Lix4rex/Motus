###########################
#                         #
#       Bibliothèques     #
#                         #
###########################
from tkinter import *
from random import *
###########################
#                         #
#        Variables        #
#                         #
###########################
motSecret=""
motdeverif=""
demandec=""
chiffredetableau=114
lignehorizontale=[12.5,38,64,88,114,138,162,188]
ligneverticale=[188,162,138,114,88,64,38,12.5]
font100="-size 14"
###########################
#                         #
#        Fonctions        #
#                         #
###########################
def lettrejuste():
    '''
    fonction: regarde si la lettre concorde avec la lettre du motsecret
    entree: rien
    sortie: rien
    '''
    global score
    for j in range(8):
        if demande[j]==motSecret[j]:
            for i in range(8):
                if coupsrestants==i:
                    canvas_text1=canvas.create_text(lignehorizontale[j], ligneverticale[i], text= demande[j], fill="green",font=font100)

def lettredansmot():
    '''
    fonction: regarde si la lettre est dans le motSecret
    entree: rien
    sortie: rien
    '''
    global score
    for j in range(8):
        if demande[j] in motSecret and demande[j]!=motSecret[j]:
            for i in range(8):
                if coupsrestants==i:
                    canvas_text1=canvas.create_text(lignehorizontale[j], ligneverticale[i], text= demande[j], fill="blue",font=font100)

def lettrefausse():
    '''
    fonction: regarde si la lettre n'est pas dans le mot
    entree: rien
    sortie: rien
    '''
    global score
    for j in range(8):
        if demande[j] not in motSecret:
            for i in range(8):
                if coupsrestants==i:
                    canvas_text1=canvas.create_text(lignehorizontale[j], ligneverticale[i], text= demande[j], fill="black",font=font100)

def creertableau():
    '''
    fonction: permet d'afficher le tableau de jeu
    entree: rien
    sortie: rien
    '''
    global canvas

    canvas = Canvas(fenetreprincipale, width=195, height=170, background="yellow")
    for i in range (0,176,25):
        ligne1 = canvas.create_line(i, 0, i, 175)
    for i in range (0,175,25):
        ligne2 = canvas.create_line(0, i, 200, i)
    canvas.pack()

def choisirmotdansdico():
    '''
    fonction: le programme va chercher dans le dico un mot de 8 lettres
    entree: rien
    sortie: rien
    '''
    global motSecret

    words = [motSecret.strip() for motSecret in open("dico.txt")]
    motSecret = choice(words)
    while len(motSecret) != 8 :
        motSecret = choice(words)
    print(motSecret)

def AfficherDemandeJoueur():
    '''
    fonction: permet d'afficher le mot que le joueur a demande dans la ligne correspondante et permet de dire si elle fait parti du mot, si elle est à la bonne place, ou si elle n'est pas dans le mot
    entree: rien
    sortie: rien
    '''
    global demande
    global coupsrestants

    demande=proposerunelettre.get()
    if len(demande)!=8:
        condition = Toplevel(fenetreprincipale)
        condition.configure(bg="red")
        Label(condition,text="MOT DE 8 LETTRE S'IL VOUS PLAÎT",font=font100,bg="red").pack()
        Button(condition, text="FERMER", command = condition.destroy, fg="black", bg="blue").pack()
    if len(demande)==8:
        for i in range (1,8):
            if coupsrestants==i:
                lettrejuste()
                lettredansmot()
                lettrefausse()
        coupsrestants-=1
        perdu()
        gagner()

def gagner():
    '''
    fonction: affiche une nouvelle fenetre qui affirme que le joueur a gagne
    entree: rien
    sortie: rien
    '''
    global score
    global scoreenmoins
    font50="-underline 1"
    if demande==motSecret:
        win = Toplevel(fenetreprincipale)
        win.configure(bg="yellow")
        Label(win, text="VOUS AVEZ GAGNE !! BIEN JOUER",font=font100,fg="red",bg="yellow").pack()
        for i in range(8):
            if coupsrestants==i:
                score=score-scoreenmoins
            scoreenmoins=scoreenmoins-50
        Label(win, text="Vous avez fait un score de :",font=font50,bg="yellow").pack()
        Label(win, text=score,font=font20,bg="yellow").pack()
        Button(win, text="FERMER", command = win.destroy and fenetreprincipale.destroy, fg="black", bg="blue").pack()

def perdu():
    '''
    fonction: afficher une nouvelle fenêtre qui affirme au joueur qu'il a perdu
    entre: rien
    sortie: rien
    '''
    global score
    font50="-underline 1"
    font11="-size 11"
    if coupsrestants==0 and demande!=motSecret:
        lose = Toplevel(fenetreprincipale)
        lose.configure(bg="red")
        Label(lose, text="VOUS AVEZ PERDU !! C'EST DOMMAGE",font=font100,bg="red").pack()
        Label(lose, text="Le mot a trouvé était :",font=font50,bg="red").pack()
        Label(lose, text=motSecret,bg="red",font=font11).pack()
        score=0
        for j in range(8):
            if demande[j]==motSecret[j]:
                score+=2
            if demande[j] in motSecret:
                score+=1
        Label(lose, text="Vous avez fait un score de :",font=font50,bg="red").pack()
        Label(lose, text=score,font=font20,bg="red").pack()
        Button(lose, text = "FERMER", command = lose.destroy and fenetreprincipale.destroy, fg="black", bg="blue").pack()

def creerfenetrejeu():
    '''
    fonction: permet de creer la fenetre de jeu à partir du bouton jouer
    entree: rien
    sortie: rien
    '''
    global coupsrestants
    global fenetreprincipale
    global proposerunelettre
    global score
    global scoreenmoins

    coupsrestants=7
    score=450
    scoreenmoins=350
    fenetreprincipale = Toplevel(debut)
    fenetreprincipale.title("JEU DU MOTUS")
    fenetreprincipale.geometry("800x600")
    fenetreprincipale.configure(bg="#7FFF00")
    choisirmotdansdico()

    font10="-size 20"

    Label(fenetreprincipale, text = "MOTUS",font=font10, fg = 'red',bg="#7FFF00").pack()

    Label(fenetreprincipale,text=" ", height=2,bg="#7FFF00").pack()

    proposerunelettre=Entry(fenetreprincipale, width=20)
    proposerunelettre.pack()

    #Ce label ne permet que d'espacer les différent interfaces de jeu
    Label(fenetreprincipale,text=" ", height=2,bg="#7FFF00").pack()

    Button(fenetreprincipale, text="ENTRER", command=AfficherDemandeJoueur,fg="black",bg="blue").pack()

    Label(fenetreprincipale,text=" ",height=4,bg="#7FFF00").pack()

    creertableau()

    Label(fenetreprincipale,text=" ", height=11,bg="#7FFF00").pack()

    Button(fenetreprincipale, text ='FERMER', command = fenetreprincipale.destroy,fg="black",bg="blue").pack()

def conseilsdejeu():
    '''
    fonction: affiche des conseils sur le jeu
    entree: rien
    sortie: rien
    '''
    font1="-size 11"
    font2="-size 13"

    Label(debut,text="CONSEIL :", bg="#007FFF", fg="#8E2323", font=font1).pack()

    Label(debut, text="Si votre lettre s'affiche en vert, cela veut dire qu'elle est à la bonne place", bg="#007FFF", fg="green", font=font1).pack()

    Label(debut, text="Si votre lettre s'affiche en bleue, cela veut dire qu'elle est dans le mot mais non à la bonne place", bg="#007FFF", fg="blue", font=font1).pack()

    Label(debut, text="Si votre lettre s'affiche en noire, cela veut dire qu'elle n'est pas dans le mot",bg="#007FFF",font=font1).pack()

###########################
#                         #
#        fenetre de       #
#       présentation      #
#                         #
###########################
font20="-size 40"
debut=Tk()

debut.configure(bg="#007FFF")
debut.geometry("800x600")
debut.title("JEU DU MOTUS")

Label(debut, text="JEU DU MOTUS",font=font20,bg="#007FFF", fg="#FF2400", height=2).pack()

Label(debut,text=" ",height=6,bg="#007FFF").pack()

conseilsdejeu()

Label(debut,text=" ",height=8,bg="#007FFF").pack()

Button(debut, text="JOUER", bg="yellow", fg="red", font=font20,command=creerfenetrejeu).pack()

Label(debut,text=" ",height=2,bg="#007FFF").pack()

debut.mainloop()