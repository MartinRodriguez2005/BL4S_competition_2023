#### on importe les librairies ###################################################################################################
from tkinter import *
from math import *
from random import randint
#####################################################################################################################################


#### Fonctions pour l'affichage et les animations ############

def lancer():
    L = 900
    l = 600
    lvraie = float(larg.get())
    zonetest = float(long.get())
    B = float(champB.get())
    aimant0=float(l_aimant.get())
    aimant=L*float(l_aimant.get())/zonetest
    nrj=float(energie.get())
    detecteur0=float(distance_detect.get())
    detecteur=L*float(distance_detect.get())/zonetest
    c=2.99792458*10**8
    q=1.602*10**(-19)
    me=0.511*10**(-3)
    mp=0.938272
    mmu=0.10566
    mpion=0.140

    can.delete('all')
    can.create_line(25,l/2,L,l/2,width=2,fill='black',dash=(4,4))
    can.create_line(25,l/2,L/10,l/2,width=2,fill='red')
    can.create_line(L/20,l/2,L/20-10,l/2-5,width=2,fill='red')
    can.create_line(L/20,l/2,L/20-10,l/2+5,width=2,fill='red')

    can.create_line(30,20,L-20,20,width=1,fill='black')
    can.create_line(30,20,40,15,width=1,fill='black')
    can.create_line(30,20,40,25,width=1,fill='black')
    can.create_line(L-20,20,L-30,25,width=1,fill='black')
    can.create_line(L-20,20,L-30,15,width=1,fill='black')
    can.create_text(2*L/10, 35, text="L = {} m".format(zonetest), fill="black", font=('Helvetica 12'))


    can.create_line(20,20,20,l-20,width=1,fill='black')
    can.create_line(20,20,25,30,width=1,fill='black')
    can.create_line(20,20,15,30,width=1,fill='black')
    can.create_line(20,l-20,25,l-30,width=1,fill='black')
    can.create_line(20,l-20,15,l-30,width=1,fill='black')
    can.create_text(55, 2*l/10, text="l = {} m".format(lvraie), fill="black", font=('Helvetica 12'))



    can.create_line(L/10,l/2-l*0.05/lvraie,L/10+aimant,l/2-l*0.05/lvraie,width=3,fill='blue')
    can.create_line(L/10,l/2+l*0.05/lvraie,L/10+aimant,l/2+l*0.05/lvraie,width=3,fill='blue')
    can.create_text(L/10+aimant/2, l/2+l*0.05/lvraie+20, text="aimant :", fill="green", font=('Helvetica 10 bold'))
    can.create_text(L/10+aimant/2, l/2+l*0.05/lvraie+35, text="l = {} cm, B = {} T".format(int(aimant0*100),B), fill="green", font=('Helvetica 10 bold'))

    gammae=1+nrj/me
    gammap=1+nrj/mp
    gammapion=1+nrj/mpion

    pe=me*sqrt(gammae**2-1)
    pp=mp*sqrt(gammap**2-1)
    ppion=mpion*sqrt(gammapion**2-1)

    Re=((pe/c)*q*10**9)/(q*B)
    Rp=((pp/c)*q*10**9)/(q*B)
    Rpion=((ppion/c)*q*10**9)/(q*B)

    betae=sqrt(1-1/gammae**2)
    betap=sqrt(1-1/gammap**2)
    betapion=sqrt(1-1/gammapion**2)

    ys0e=Re*(1-cos(asin(aimant0/Re)))
    ys0p=Rp*(1-cos(asin(aimant0/Rp)))
    ys0pion=Rpion*(1-cos(asin(aimant0/Rpion)))

    d0e=detecteur0*tan(asin(aimant0/Re))+Re*(1-cos(asin(aimant0/Re)))
    d0p=detecteur0*tan(asin(aimant0/Rp))+Rp*(1-cos(asin(aimant0/Rp)))
    d0pion=detecteur0*tan(asin(aimant0/Rpion))+Rpion*(1-cos(asin(aimant0/Rpion)))

    yse=l*ys0e/lvraie
    ysp=l*ys0p/lvraie
    yspion=l*ys0pion/lvraie

    de=l*d0e/lvraie
    dp=l*d0p/lvraie
    dpion=l*d0pion/lvraie


    anglee=asin(aimant0/Re)*180/pi
    anglep=asin(aimant0/Rp)*180/pi
    anglepion=asin(aimant0/Rpion)*180/pi



    can.create_line(L/10+aimant,l/2-yse,L/10+aimant+detecteur,l/2-de,width=2,fill='green')
    can.create_line(L/10+aimant,l/2+ysp,L/10+aimant+detecteur,l/2+dp,width=2,fill='red')
    can.create_line(L/10+aimant,l/2+yspion,L/10+aimant+detecteur,l/2+dpion,width=2,fill='orange')


    ys0=ys0e
    d0=d0e
    ys=yse
    d=de
    angle=anglee
    p=pe
    R=Re
    gamma=gammae
    beta=betae




    can.create_line(L/10+aimant,3*l/4,L/10+aimant+detecteur,3*l/4,width=1,fill='black')
    can.create_line(L/10+aimant,3*l/4,L/10+aimant+10,3*l/4-5,width=1,fill='black')
    can.create_line(L/10+aimant,3*l/4,L/10+aimant+10,3*l/4+5,width=1,fill='black')
    can.create_line(L/10+aimant+detecteur,3*l/4,L/10+aimant+detecteur-10,3*l/4-5,width=1,fill='black')
    can.create_line(L/10+aimant+detecteur,3*l/4,L/10+aimant+detecteur-10,3*l/4+5,width=1,fill='black')
    can.create_text(L/10+aimant+detecteur/2, 3*l/4+25, text="Distance aimant-détecteur = {} m".format(detecteur0), fill="black", font=('Helvetica 12'))


#    can.create_rectangle(L/10+aimant+detecteur,l/2-d-l*0.1/lvraie,L/10+aimant+detecteur+l*0.01/lvraie,l/2-d+l*0.1/lvraie,width=2,fill='black')
#    can.create_text(L/10+aimant+detecteur+l*0.07/lvraie, l/2-d-l*0.05/lvraie-10, text="détecteur", fill="black", font=('Helvetica 12 bold'))


    can.create_text(L/10+aimant+detecteur+l*0.02/lvraie, l/2+l*0.1/lvraie, text="Ecart à {} m :".format(round(detecteur0,2)), fill="black", font=('Helvetica 10 bold'))
    can.create_text(L/10+aimant+detecteur+l*0.02/lvraie+80, l/2+l*0.1/lvraie, text="{} cm".format(round(100*d0e,3)), fill="green", font=('Helvetica 10 bold'))
    can.create_text(L/10+aimant+detecteur+l*0.02/lvraie+160, l/2+l*0.1/lvraie, text="{} cm".format(round(100*d0p,3)), fill="red", font=('Helvetica 10 bold'))
    can.create_text(L/10+aimant+detecteur+l*0.02/lvraie+240, l/2+l*0.1/lvraie, text="{} cm".format(round(100*d0pion,3)), fill="orange", font=('Helvetica 10 bold'))






    can.create_text(2*L/10+100, 2.6*l/10-20, text="electron", fill="green", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+200, 2.6*l/10-20, text="proton", fill="red", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+300, 2.6*l/10-20, text="pion", fill="orange", font=('Helvetica 10 bold'))


    can.create_text(2*L/10, 2.6*l/10, text="R courb =", fill="black", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+100, 2.6*l/10, text="{} m".format(round(Re,2)), fill="green", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+200, 2.6*l/10, text="{} m".format(round(Rp,2)), fill="red", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+300, 2.6*l/10, text="{} m".format(round(Rpion,2)), fill="orange", font=('Helvetica 10 bold'))

    can.create_text(2*L/10, 2.6*l/10+15, text="Qté mvt =", fill="black", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+100, 2.6*l/10+15, text="{} Gev/c".format(round(pe,4)), fill="green", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+200, 2.6*l/10+15, text="{} Gev/c".format(round(pp,4)), fill="red", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+300, 2.6*l/10+15, text="{} Gev/c".format(round(ppion,4)), fill="orange", font=('Helvetica 10 bold'))

    can.create_text(2*L/10, 2.6*l/10+30, text="Beta     =", fill="black", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+100, 2.6*l/10+30, text="{}".format(round(betae,10)), fill="green", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+200, 2.6*l/10+30, text="{}".format(round(betap,10)), fill="red", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+300, 2.6*l/10+30, text="{}".format(round(betapion,10)), fill="orange", font=('Helvetica 10 bold'))

    can.create_text(2*L/10, 2.6*l/10+45, text="Gamma  =", fill="black", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+100, 2.6*l/10+45, text="{}".format(round(gammae,1)), fill="green", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+200, 2.6*l/10+45, text="{}".format(round(gammap,1)), fill="red", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+300, 2.6*l/10+45, text="{}".format(round(gammapion,1)), fill="orange", font=('Helvetica 10 bold'))

    can.create_text(2*L/10, 2.6*l/10+60, text="Angle   =", fill="black", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+100, 2.6*l/10+60, text="{}°".format(round(anglee,2)), fill="green", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+200, 2.6*l/10+60, text="{}°".format(round(anglep,2)), fill="red", font=('Helvetica 10 bold'))
    can.create_text(2*L/10+300, 2.6*l/10+60, text="{}°".format(round(anglepion,2)), fill="orange", font=('Helvetica 10 bold'))

    ##########################################################################################################################"



def quitter():
    fenetre.destroy()               #ferme la fenetre !


#####################################################################################################################################





#### 3) Création de la fenetre ######################################################################################################
                                                                    # Fenetre principale avec son titre
fenetre=Tk()
fenetre.title("bl4s simulation project")

                                                                    #les deux zones de la fenetre : les "canvas".
L=900                                                               #côtés du canvas du dessin
l=600
can=Canvas(fenetre,bg='white',height=l,width=L)                     #creation du canvas de gauche où l'on dessine
can.grid(row=1,column=0)

can2=Canvas(fenetre)                                                #creation du canvas de droite où sont les boutons et champs de saisie
can2.grid(row=1,column=1,sticky='ns')
#####################################################################################################################################



#### 4) Création des boutons et champs ##############################################################################################

#les champs de saisie

Label(can2,text="").pack(side=TOP)
Label(can2,text="Largeur de la zone de test (m)").pack(pady=2,side=TOP)
larg=Entry(can2,width=10)
larg.pack(pady=2,side=TOP)
larg.insert(0,0.8)

Label(can2,text="Longueur de la zone de test (m)").pack(pady=2,side=TOP)
long=Entry(can2,width=10)
long.pack(pady=2,side=TOP)
long.insert(0,2)

Label(can2,text="Energie du faisceau (GeV)").pack(pady=2,side=TOP)
energie=Entry(can2,width=10)
energie.pack(pady=2,side=TOP)
energie.insert(0,2.75)

Label(can2,text="Intensité du champ B (Tesla)").pack(pady=2,side=TOP)
champB=Entry(can2,width=10)
champB.pack(pady=2,side=TOP)
champB.insert(0,1.75)

Label(can2,text="Longueur de l'aimant (m)").pack(pady=2,side=TOP)
l_aimant=Entry(can2,width=10)
l_aimant.pack(pady=2,side=TOP)
l_aimant.insert(0,0.1)

Label(can2,text="Distance aimant - détecteurs (m)").pack(pady=2,side=TOP)
distance_detect=Entry(can2,width=10)
distance_detect.pack(pady=2,side=TOP)
distance_detect.insert(0,1)

#bouton initialiser
I=Button(can2,text='Lancer l\'experience',height=2,width=20,relief=GROOVE,activebackground="dark green",activeforeground="white",command=lancer)
I.pack(pady=20,side=TOP)

var=IntVar()
button = Checkbutton(can2, text="Afficher les calculs ?", variable=var)
button.pack(pady=5,side=TOP)


Button(can2,text='Quitter!',command=quitter).pack(pady=20,side=BOTTOM)      #bouton quitter
















#####################################################################################################################################

######  Main  #######################################################################################

can.create_line(25,l/2,L,l/2,width=2,fill='black',dash=(4,4))
can.create_line(25,l/2,L/10,l/2,width=2,fill='red')
can.create_line(L/20,l/2,L/20-10,l/2-5,width=2,fill='red')
can.create_line(L/20,l/2,L/20-10,l/2+5,width=2,fill='red')




fenetre.mainloop() #boucle de la fenetre