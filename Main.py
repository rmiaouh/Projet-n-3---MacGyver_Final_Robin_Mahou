#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Programme MAIN du jeu
"""
import pygame, MazeGenerator_1,MazeGenerator_2, random
from random import randint
from pygame.locals import *
from Display import *
from Datas import *

pygame.init()

#fenêtre Pygame // Pygame Window
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone // Icon
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre du jeu // Game Title
pygame.display.set_caption(titre_fenetre)


#BOUCLE PRINCIPALE // MAIN LOOP
continuer = 1
main_itemtot=0
main_item1=0
main_item2=0
main_item3=0
lumiere = 0
rire_son = True
main_case_x = 0
main_case_y = 0

#Variables liées au timer // Timer variables
timer = pygame.time.Clock()
frameRate = 60
frameCount = 1



#Musiques & sons utilisés // Sound variables

sound_item = pygame.mixer.Sound(data_sound_item)
sound_sword = pygame.mixer.Sound(data_sound_sword)
sound_musique_0=pygame.mixer.Sound(data_sound_musique_0)
sound_gameover = pygame.mixer.Sound(data_sound_gameover)
sound_rire = pygame.mixer.Sound(data_sound_rire)
sound_win = pygame.mixer.Sound(data_sound_win)


while continuer:	
	#Chargement et affichage de l'écran d'accueil // home loading
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement // Refreshing
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle // each loop we put variables to 0
	continuer_jeu = 1
	continuer_accueil = 1
	choix_niveau = 0

	#We put some sound for the home page
	sound_background = pygame.mixer.Sound(sound_musique_0)
	sound_background.set_volume(0.2)
	sound_background.play(-1)
	
	#BOUCLE D'ACCUEIL // HOME LOOP
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle // Clock Speed
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			#If the user quit, we reset loop variables
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable du niveau // level variable
				choix = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1 // Level 1 launching
				if event.key == K_F1: #easy mode
					continuer_accueil = 0
					#Pour générer un labyrinthe aléatoire on fait appel aux deux programmes de générations de labyrinthe
					#Maze generator programs
					MazeGenerator_1.maze(15,15)
					MazeGenerator_2.mazeFinal()
					#On vient selectionner le fichier .txt que nous rend les deux programmes qui génèrent un labyrinthe aléatoire
					#We use the .txt generated by the MazeGenetor programs
					choix = 'mazeFinal.txt'
					#rire_son est une variable qui sert à lancer le son "rire" uniquement une fois, afin de ne pas 'flooder' le canal audio du jeu
					#rire_son allows to launch only one time the sound of laughts
					rire_son = True
					#Afin d'appliquer les bon paramêtres selon le bon niveau, une variable sera affecté à cette tache
					#Level number variable
					choix_niveau = 1


			
		

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	#We check if the user choosed a level
	if choix != 0:
		#Chargement du fond // background loading
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		#level generation with the MazeGenerator .txt
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)


		#Création de MacGyver
		#MacGyverCreation
		mc = Perso("Images/MacGyver2.png", "Images/MacGyver2.png", 
		"Images/MacGyver2.png", "Images/MacGyver2.png", niveau)


	if choix_niveau == 1:

			#BOUCLE DE JEU // LOOP GAME
		while continuer_jeu:
		
			#Limitation de vitesse de la boucle
			#Variables timer
			#Clock game variable
			pygame.time.Clock().tick(60)
			
			totalSeconds = frameCount // frameRate
			seconds = totalSeconds % 31
			time = "00:{}".format(seconds)

			for event in pygame.event.get():
			
				#Si l'utilisateur quitte, on met la variable qui continue le jeu
				#ET la variable générale à 0 pour fermer la fenêtre
				#If the user quit, we stop the game and we close the window
				if event.type == QUIT:
					continuer_jeu = 0
					continuer = 0

				elif event.type == KEYDOWN:
					#Si l'utilisateur presse Echap ici, on revient seulement au menu
					#If escape is pressed, we stop the game
					if event.key == K_ESCAPE:
						continuer_jeu = 0
						#Variables pour savoir quelle item le joueur dispose
						#Items variable
						main_item1 = 0
						main_item2 = 0 
						main_item3 = 0
						#Compte le nombre d'objets que le joueur à (de 0 à 3)
						#Count how many items got the user
						main_itemtot = 0
						choix_niveau = 0
						#init timer
						frameCount = 0
						rire_son = False
						
						sound_background.stop()

					#Touches de déplacement
					#Move keys
					elif event.key == K_RIGHT:
						mc.deplacer('droite')
					elif event.key == K_LEFT:
						mc.deplacer('gauche')
					elif event.key == K_UP:
						mc.deplacer('haut')
					elif event.key == K_DOWN:
						mc.deplacer('bas')	
					elif event.key == K_RETURN:
						sound_background.stop()


			#Affichages aux nouvelles positions
			#Position refreshing
			fenetre.blit(fond, (0,0))
			niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)


			#Variables de police d'écriture
			#Font variables
			myfont = pygame.font.Font("Images/font.ttf", 19)

			#Message different selon le nombre d'item qu'a le joueur
			#Different message according to the items number
			if main_itemtot != 3:
				label = myfont.render("You have {}/3 items".format(main_itemtot), 1, (255,255,255))
			else : 
				label = myfont.render("You have {}/3 items - You can now kill the Boss".format(main_itemtot), 1, (120,255,120))
			fenetre.blit(label, (10,425))
			#Compteur de temps
			#Time counter
			if seconds < 11:
				timeOutput = myfont.render(time, True, (250,85,45))
			elif seconds < 21 and seconds > 10:
				timeOutput = myfont.render(time, True, (250,165,45))
			else :
				timeOutput = myfont.render(time, True, (250,250,250))

			if seconds == 1:
				#Si les secondes tombent à 1 du timer, on reset le jeu et gameover + retour accueil
				#If time counting == 1 , then gameover + home page return
				continuer_jeu = 0
				main_item1 = 0
				main_item2 = 0 
				main_item3 = 0
				main_itemtot = 0
				choix_niveau = 0
				#init timer
				frameCount = 0
				rire_son = False
				sound_gameover.set_volume(0.3)
				sound_gameover.play()
				sound_background.stop()
			
			fenetre.blit(timeOutput, (395,0))
			frameCount -= 1
			timer.tick(frameRate)

			fenetre.blit(mc.direction, (mc.x, mc.y)) #mc.direction = l'image dans la bonne direction
			pygame.display.flip()



			#Victoire -> Retour à l'accueil
			#If victory -> Home page 
			if niveau.structure[mc.case_y][mc.case_x] == 'a' and main_item1==1 and main_item2==1 and main_item3 == 1:
				sound_sword.set_volume(0.7)
				sound_sword.play()
				sound_win.set_volume(0.4)
				sound_win.play()
				continuer_jeu = 0
				main_item1 = 0
				main_item2 = 0 
				main_item3 = 0
				main_itemtot = 0
				choix_niveau = 0
				#init timer
				frameCount = 0
				rire_son = False
				sound_background.stop()

			#Fonction cachée, qui fait rire le boss si on n'a pas les items necessaires (cette fonction ne sert pas à grand chose)
			#Boss Laught
			if niveau.structure[mc.case_y][mc.case_x] == 'a' and main_item1==0 and main_item2==0 and main_item3==0 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)

			if niveau.structure[mc.case_y][mc.case_x] == 'a' and main_item1==1 and main_item2==0 and main_item3==0 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)


			if niveau.structure[mc.case_y][mc.case_x] == 'a' and main_item1==0 and main_item2==1 and main_item3==0 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)


			if niveau.structure[mc.case_y][mc.case_x] == 'a' and main_item1==0 and main_item2==0 and main_item3==1 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)

			#Selon l'item que récupère le joueur, on vient mettre un son et incrémenter la variable de l'objet en question
			#depending on the number of objects the player has 
			if niveau.structure[mc.case_y][mc.case_x] == '1':
				if main_item1 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()

				main_item1 = 1

				#Cette fonction génère l'affichage selon l'item pris ou non
				#display refreshing
				niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)


			if niveau.structure[mc.case_y][mc.case_x] == '2':
				if main_item2 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()
				main_item2 = 1
				niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)

			if niveau.structure[mc.case_y][mc.case_x] == '3':
				if main_item3 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()
				main_item3 = 1
				niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)

			#On calcule le nombre total d'item (de 0 à 3)
			#Total item number
			main_itemtot = main_item1 + main_item2 + main_item3
