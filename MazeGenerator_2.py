import random
from random import randint
import sys

def mazeFinal():
    crimefile = open('maze.txt', 'r')
    t = crimefile.read()
    #print(t)

    rand1 = randint(15, 210)
    rand2 = rand1 +1
    x = True
    y = True
    z = True
    while x == True:

        rand1 = randint(55, 210)
        rand2 = rand1 +1

        if t[rand1:rand2]=='0':
            tab1 = t[:rand1] + "a" + t[rand2:]
            #print(tab1)
            x = False
    x = True
    while x == True:

        rand1 = randint(30, 90)
        rand2 = rand1 +1

        if tab1[rand1:rand2]=='0':
            tab2 = tab1[:rand1] + "1" + tab1[rand2:]
            #print(tab2)
            x = False
    x = True
    while x == True:

        rand1 = randint(91, 150)
        rand2 = rand1 +1

        if tab2[rand1:rand2]=='0':
            tab3 = tab2[:rand1] + "2" + tab2[rand2:]
            #print(tab3)
            x = False
    x= True

    while x == True:

        rand1 = randint(151, 210)
        rand2 = rand1 +1

        if tab3[rand1:rand2]=='0':
            tab4 = tab3[:rand1] + "3" + tab3[rand2:]
            #print(tab4)
            x = False
    x= True

    while x == True:

        rand1 = randint(172, 210)
        rand2 = rand1 +1

        if tab4[rand1:rand2]=='0':
            tab5 = tab4[:rand1] + "0" + tab4[rand2:]
            orig_stdout = sys.stdout
            f = open('mazeFinal.txt', 'w')
            sys.stdout = f
            print(tab5)
            f.close()
            x = False
    
    #Partie ajoutée pour éviter le bug du personnage bloqué.    
    x= True
    while x == True:

        
            tab6 = tab5[:0] + "d" + tab5[1:]
            orig_stdout = sys.stdout
            f = open('mazeFinal.txt', 'w')
            sys.stdout = f
            print(tab6)
            f.close()
            x = False
    x= True    
    while x == True:

        
            tab7 = tab6[:1] + "0" + tab6[2:]
            orig_stdout = sys.stdout
            f = open('mazeFinal.txt', 'w')
            sys.stdout = f
            print(tab7)
            f.close()
            x = False
    x= True
    while x == True:

        
            tab8 = tab7[:16] + "0" + tab7[17:]
            orig_stdout = sys.stdout
            f = open('mazeFinal.txt', 'w')
            sys.stdout = f
            print(tab8)
            f.close()
            x = False

#mazeFinal()