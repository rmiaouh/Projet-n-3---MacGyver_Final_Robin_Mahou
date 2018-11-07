#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Programme MAIN du jeu
"""
import pygame, MazeGenerator_1,MazeGenerator_2,MazeGenerator_3, random
from random import randint
from pygame.locals import *

from Display import *
from Datas import *

pygame.init()

#fenêtre Pygame 
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre du jeu
pygame.display.set_caption(titre_fenetre)


#BOUCLE PRINCIPALE
continuer = 1
main_itemtot=0
main_item1=0
main_item2=0
main_item3=0
lumiere = 0
rire_son = True
main_case_x = 0
main_case_y = 0

#Variables liées au timer
timer = pygame.time.Clock()
frameRate = 60
frameCount = 1



#Musiques & sons utilisés

sound_item = pygame.mixer.Sound(data_sound_item)
sound_sword = pygame.mixer.Sound(data_sound_sword)
sound_musique_0=pygame.mixer.Sound(data_sound_musique_0)
sound_gameover = pygame.mixer.Sound(data_sound_gameover)
sound_rire = pygame.mixer.Sound(data_sound_rire)
sound_win = pygame.mixer.Sound(data_sound_win)


while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1
	choix_niveau = 0

	sound_background = pygame.mixer.Sound(sound_musique_0)
	sound_background.set_volume(0.2)
	sound_background.play(-1)
	
	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0
				
			elif event.type == KEYDOWN:				
				#Lancement du niveau 1
				if event.key == K_F1: #easy mode
					continuer_accueil = 0
					#Pour générer un labyrinthe aléatoire on fait appel aux deux programmes de générations de labyrinthe 
					MazeGenerator_1.maze(15,15)
					MazeGenerator_2.mazeFinal()
					#On vient selectionner le fichier .txt que nous rend les deux programmes qui génèrent un labyrinthe aléatoire
					choix = 'mazeFinal.txt'
					#rire_son est une variable qui sert à lancer le son "rire" uniquement une fois, afin de ne pas 'flooder' le canal audio du jeu
					rire_son = True
					#Afin d'appliquer les bon paramêtres selon le bon niveau, une variable sera affecté à cette tache
					choix_niveau = 1
				if event.key == K_F2: #medium mode
					continuer_accueil = 0
					#Pour générer un labyrinthe aléatoire on fait appel aux deux programmes de générations de labyrinthe
					MazeGenerator_1.maze(15,15)
					MazeGenerator_3.mazeFinal()
					#On vient selectionner le fichier .txt que nous rend les deux programmes qui génèrent un labyrinthe aléatoire
					choix = 'mazeFinal.txt'
					#rire_son est une variable qui sert à lancer le son "rire" uniquement une fois, afin de ne pas 'flooder' le canal audio du jeu
					rire_son = True
					#Afin d'appliquer les bon paramêtres selon le bon niveau, une variable sera affecté à cette tache
					choix_niveau = 2
				if event.key == K_F3: #hard mode
					continuer_accueil = 0
					#Pour générer un labyrinthe aléatoire on fait appel aux deux programmes de générations de labyrinthe
					MazeGenerator_1.maze(15,15)
					MazeGenerator_2.mazeFinal()
					#On vient selectionner le fichier .txt que nous rend les deux programmes qui génèrent un labyrinthe aléatoire
					choix = 'mazeFinal.txt'
					#rire_son est une variable qui sert à lancer le son "rire" uniquement une fois, afin de ne pas 'flooder' le canal audio du jeu
					rire_son = True
					#Afin d'appliquer les bon paramêtres selon le bon niveau, une variable sera affecté à cette tache
					choix_niveau = 3

			
		

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création de Donkey Kong
		mc = Perso("Images/MacGyver2.png", "Images/MacGyver2.png", 
		"Images/MacGyver2.png", "Images/MacGyver2.png", niveau)


	if choix_niveau == 1:

			#BOUCLE DE JEU
		while continuer_jeu:
		
			#Limitation de vitesse de la boucle
			#Variables timer

			pygame.time.Clock().tick(60)
			
			totalSeconds = frameCount // frameRate
			seconds = totalSeconds % 31
			time = "00:{}".format(seconds)

			for event in pygame.event.get():
			
				#Si l'utilisateur quitte, on met la variable qui continue le jeu
				#ET la variable générale à 0 pour fermer la fenêtre
				if event.type == QUIT:
					continuer_jeu = 0
					continuer = 0

				elif event.type == KEYDOWN:
					#Si l'utilisateur presse Echap ici, on revient seulement au menu
					if event.key == K_ESCAPE:
						continuer_jeu = 0
						#Variables pour savoir quelle item le joueur dispose
						main_item1 = 0
						main_item2 = 0 
						main_item3 = 0
						#Compte le nombre d'objets que le joueur à (de 0 à 3)
						main_itemtot = 0
						choix_niveau = 0
						#init timer
						frameCount = 0
						rire_son = False
						
						sound_background.stop()

					#Touches de déplacement
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
			fenetre.blit(fond, (0,0))
			niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)


			#Variables de police d'écriture
			myfont = pygame.font.Font("Images/font.ttf", 19)

			#Message different selon le nombre d'item qu'a le joueur
			if main_itemtot != 3:
				label = myfont.render("You have {}/3 items".format(main_itemtot), 1, (255,255,255))
			else : 
				label = myfont.render("You have {}/3 items - You can now kill the Boss".format(main_itemtot), 1, (120,255,120))
			fenetre.blit(label, (10,425))
			#niveau.afficher(fenetre)

			#Compteur de temps
			if seconds < 11:
				timeOutput = myfont.render(time, True, (250,85,45))
			elif seconds < 21 and seconds > 10:
				timeOutput = myfont.render(time, True, (250,165,45))
			else :
				timeOutput = myfont.render(time, True, (250,250,250))

			if seconds == 1:
				#Si les secondes tombent à 1 du timer, on reset le jeu et gameover + retour accueil
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
			if niveau.structure[mc.case_y][mc.case_x] == '1':
				if main_item1 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()

				main_item1 = 1

				#Cette fonction génère l'affichage selon l'item pris ou non
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
			main_itemtot = main_item1 + main_item2 + main_item3





########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################


# Fin du programme (les lignes suivantes ne sont pas à prendre en compte car elles réalisent des fonctions ajoutés et "BETA" par rapport à la consigne)





























































































	if choix_niveau == 3: #hardmode	
	#BOUCLE DE JEU
		while continuer_jeu:
		
			#Limitation de vitesse de la boucle
			pygame.time.Clock().tick(60)
			#On vient générer un timer en comptant le nombre de tick de clock et en configurant ce calcul selon notre fonctionnement horaire
			totalSeconds = frameCount // frameRate
			#On définit le nombre de seconde que l'on désire afficher à notre compteur, ici 59 secondes.
			seconds = totalSeconds % 59
			#On génère le texte à afficher
			time = "00:{}".format(seconds)

			for event in pygame.event.get():
			
				#Si l'utilisateur quitte, on met la variable qui continue le jeu
				#ET la variable générale à 0 pour fermer la fenêtre
				if event.type == QUIT:
					continuer_jeu = 0
					continuer = 0

				elif event.type == KEYDOWN:
					#Si l'utilisateur presse Echap ici, on revient seulement au menu
					if event.key == K_ESCAPE:
						continuer_jeu = 0
						#Correspond à la variable de l'item 1, si celle-ci est à 0, l'utilisateur n'a pas d'item, si celle-ci est à 1 : l'utilisateur à l'item en question.
						main_item1 = 0
						main_item2 = 0 
						main_item3 = 0
						#Correspond au nombre d'item total ( de 0 à 3)
						main_itemtot = 0
						#Correspond à la position en x du joueur
						main_case_x = 0
						#Correspond à la position en y du joueur
						main_case_y = 0
						#Variable de niveau
						choix_niveau = 0
						#Variable pour savoir si la fonction qui empeche le joeur de voir la carte dans sa totalité est activée ou non
						lumiere = 0
						rire_son = False
						sound_background.stop()

					#Touches de déplacement
					elif event.key == K_RIGHT:
						mc.deplacer('droite')
						main_case_x = mc.case_x
					elif event.key == K_LEFT:
						mc.deplacer('gauche')
						main_case_x = mc.case_x
					elif event.key == K_UP:
						mc.deplacer('haut')
						main_case_y = mc.case_y
					elif event.key == K_DOWN:
						mc.deplacer('bas')
						main_case_y = mc.case_y	
					elif event.key == K_RETURN:
						sound_background.stop()
		

			#Affichages aux nouvelles positions
			fenetre.blit(fond, (0,0))
			if lumiere !=1:
				niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)
			else:
				niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)
				lumiere = 0
					
			#Variables qui gèrent la font/police d'écriture
			myfont = pygame.font.Font("Images/font.ttf", 19)
			myfont2 = pygame.font.Font("Images/font.ttf", 14)

			#selon le nombre d'item on affiche un message different
			if main_itemtot != 3:
				label = myfont.render("You have {}/3 items".format(main_itemtot), 1, (255,255,255))
			else : 
				label = myfont.render("You have {}/3 items - You can now kill the Boss".format(main_itemtot), 1, (120,255,120))
			fenetre.blit(label, (10,425))


			label2 = myfont2.render("X: {} | Y: {}".format(main_case_x,main_case_y), 1, (255,255,255))
			fenetre.blit(label2, (200,2))
			#niveau.afficher(fenetre)

			#Compteur de temps
			if seconds < 11:
				timeOutput = myfont.render(time, True, (250,85,45))
			elif seconds < 21 and seconds > 10:
				timeOutput = myfont.render(time, True, (250,165,45))
			else :
				timeOutput = myfont.render(time, True, (250,250,250))

			if seconds == 1:
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
			fenetre.blit(timeOutput, (395,0))
			frameCount -= 1
			timer.tick(frameRate)

			fenetre.blit(mc.direction, (mc.x, mc.y)) #mc.direction = l'image dans la bonne direction
			pygame.display.flip()

			#Victoire -> Retour à l'accueil
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
				main_case_x = 0
				main_case_y = 0
				lumiere = 0
				rire_son = False
				sound_gameover.set_volume(0.3)
				sound_gameover.play()
				sound_background.stop()

				#Selon sur quoi marche le joueur, un son est déployé
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

			#Selon sur quelle item marche le joueur on affecte nos variables
			if niveau.structure[mc.case_y][mc.case_x] == '1':
				if main_item1 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()

				main_item1 = 1
				niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)


			if niveau.structure[mc.case_y][mc.case_x] == '2':
				if main_item2 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()
				main_item2 = 1
				niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)


			if niveau.structure[mc.case_y][mc.case_x] == '3':
				if main_item3 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()
				main_item3 = 1
				niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)

			#Si case départ activée
			if niveau.structure[mc.case_y][mc.case_x] == 'd' and main_item1==1 and main_item2==1 and main_item3 == 1:
				lumiere = 1
				niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)
				
			main_itemtot = main_item1 + main_item2 + main_item3
			

	if choix_niveau == 2: #hardmode	
		#BOUCLE DE JEU
			while continuer_jeu:
			
				#Limitation de vitesse de la boucle
				pygame.time.Clock().tick(60)
				totalSeconds = frameCount // frameRate
				seconds = totalSeconds % 51
				time = "00:{}".format(seconds)

				for event in pygame.event.get():
				
					#Si l'utilisateur quitte, on met la variable qui continue le jeu
					#ET la variable générale à 0 pour fermer la fenêtre
					if event.type == QUIT:
						continuer_jeu = 0
						continuer = 0

					elif event.type == KEYDOWN:
						#Si l'utilisateur presse Echap ici, on revient seulement au menu
						if event.key == K_ESCAPE:
							continuer_jeu = 0
							main_item1 = 0
							main_item2 = 0 
							main_item3 = 0
							main_itemtot = 0
							main_case_x = 0
							main_case_y = 0
							choix_niveau = 0
							lumiere = 0
							rire_son = False
							sound_background.stop()

						#Touches de déplacement
						elif event.key == K_RIGHT:
							mc.deplacer('droite')
							main_case_x = mc.case_x
						elif event.key == K_LEFT:
							mc.deplacer('gauche')
							main_case_x = mc.case_x
						elif event.key == K_UP:
							mc.deplacer('haut')
							main_case_y = mc.case_y
						elif event.key == K_DOWN:
							mc.deplacer('bas')
							main_case_y = mc.case_y	
						elif event.key == K_RETURN:
							sound_background.stop()


				#Affichages aux nouvelles positions
				fenetre.blit(fond, (0,0))
				if lumiere !=1:
					niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)
				else:
					niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)
					lumiere = 0


				myfont = pygame.font.Font("Images/font.ttf", 19)
				myfont2 = pygame.font.Font("Images/font.ttf", 14)

				if main_itemtot != 3:
					label = myfont.render("You have {}/3 items".format(main_itemtot), 1, (255,255,255))
				else : 
					label = myfont.render("You have {}/3 items - You can now kill the Boss".format(main_itemtot), 1, (120,255,120))
				fenetre.blit(label, (10,425))


				label2 = myfont2.render("X: {} | Y: {}".format(main_case_x,main_case_y), 1, (255,255,255))
				fenetre.blit(label2, (200,2))
				#niveau.afficher(fenetre)

				#Compteur de temps
				if seconds < 11:
					timeOutput = myfont.render(time, True, (250,85,45))
				elif seconds < 21 and seconds > 10:
					timeOutput = myfont.render(time, True, (250,165,45))
				else :
					timeOutput = myfont.render(time, True, (250,250,250))

				if seconds == 1:
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
					main_case_x = 0
					main_case_y = 0
					lumiere = 0
					rire_son = False
					sound_background.stop()


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


				if niveau.structure[mc.case_y][mc.case_x] == '1':
					if main_item1 == 0:
						sound_item.set_volume(0.15)
						sound_item.play()

					main_item1 = 1
					niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)


				if niveau.structure[mc.case_y][mc.case_x] == '2':
					if main_item2 == 0:
						sound_item.set_volume(0.15)
						sound_item.play()
					main_item2 = 1
					niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)


				if niveau.structure[mc.case_y][mc.case_x] == '3':
					if main_item3 == 0:
						sound_item.set_volume(0.15)
						sound_item.play()
					main_item3 = 1
					niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)

				if niveau.structure[mc.case_y][mc.case_x] == 'd' and main_item1==0 and main_item2==0 and main_item3 == 0:
					lumiere = 1
					niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)

				main_itemtot = main_item1 + main_item2 + main_item3


