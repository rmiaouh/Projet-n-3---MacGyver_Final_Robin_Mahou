#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu
"""
import pygame, MazeGenerator_1,MazeGenerator_2,MazeGenerator_3, random
from random import randint
from pygame.locals import *

from maze_Test_2 import *
from maze_Test_3 import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
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

timer = pygame.time.Clock()
frameRate = 60
frameCount = 1



#Musiques
sound_item = pygame.mixer.Sound("Images/item2.wav")
sound_sword = pygame.mixer.Sound("Images/combatsound.wav")
sound_musique_0=pygame.mixer.Sound("Images/musique_0.wav")
sound_musique_1=pygame.mixer.Sound("Images/musique_1.wav")
sound_musique_2=pygame.mixer.Sound("Images/musique_2.wav")
sound_musique_3=pygame.mixer.Sound("Images/musique_3.wav")
sound_musique_4=pygame.mixer.Sound("Images/musique_4.wav")
sound_musique_5=pygame.mixer.Sound("Images/musique_5.wav")
sound_musique_6=pygame.mixer.Sound("Images/musique_6.wav")
sound_musique_7=pygame.mixer.Sound("Images/musique_7.wav")
sound_musique_8=pygame.mixer.Sound("Images/musique_8.wav")
sound_musique_9=pygame.mixer.Sound("Images/musique_9.wav")
sound_gameover = pygame.mixer.Sound("Images/gameover.wav")

sound_rire = pygame.mixer.Sound("Images/rire.wav")
sound_win = pygame.mixer.Sound("Images/youwin.wav")


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
	randome_int = randint(0,9)
	randomstr = "Images/musique_{}.wav".format(randome_int)
	sound_background = pygame.mixer.Sound(randomstr)
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
					MazeGenerator_1.maze(15,15)
					MazeGenerator_2.mazeFinal()
					choix = 'mazeFinal.txt'
					rire_son = True
					choix_niveau = 1
				if event.key == K_F2: #medium mode
					continuer_accueil = 0
					MazeGenerator_1.maze(15,15)
					MazeGenerator_3.mazeFinal()
					choix = 'mazeFinal.txt'
					rire_son = True
					choix_niveau = 2
				if event.key == K_F3: #hard mode
					continuer_accueil = 0
					MazeGenerator_1.maze(15,15)
					MazeGenerator_2.mazeFinal()
					choix = 'mazeFinal.txt'
					rire_son = True
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
		dk = Perso("Images/MacGyver2.png", "Images/MacGyver2.png", 
		"Images/MacGyver2.png", "Images/MacGyver2.png", niveau)
		
	if choix_niveau == 3: #hardmode	
	#BOUCLE DE JEU
		while continuer_jeu:
		
			#Limitation de vitesse de la boucle
			pygame.time.Clock().tick(60)

			totalSeconds = frameCount // frameRate
			seconds = totalSeconds % 59
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
						dk.deplacer('droite')
						main_case_x = dk.case_x
					elif event.key == K_LEFT:
						dk.deplacer('gauche')
						main_case_x = dk.case_x
					elif event.key == K_UP:
						dk.deplacer('haut')
						main_case_y = dk.case_y
					elif event.key == K_DOWN:
						dk.deplacer('bas')
						main_case_y = dk.case_y	
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
				sound_background.stop()
			fenetre.blit(timeOutput, (395,0))
			frameCount -= 1
			timer.tick(frameRate)

			fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
			pygame.display.flip()

			#Victoire -> Retour à l'accueil
			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==1 and main_item2==1 and main_item3 == 1:
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


			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==0 and main_item2==0 and main_item3==0 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)

			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==1 and main_item2==0 and main_item3==0 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)


			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==0 and main_item2==1 and main_item3==0 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)


			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==0 and main_item2==0 and main_item3==1 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)


			if niveau.structure[dk.case_y][dk.case_x] == '1':
				if main_item1 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()

				main_item1 = 1
				niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)


			if niveau.structure[dk.case_y][dk.case_x] == '2':
				if main_item2 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()
				main_item2 = 1
				niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)


			if niveau.structure[dk.case_y][dk.case_x] == '3':
				if main_item3 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()
				main_item3 = 1
				niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)

			if niveau.structure[dk.case_y][dk.case_x] == 'd' and main_item1==1 and main_item2==1 and main_item3 == 1:
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
							dk.deplacer('droite')
							main_case_x = dk.case_x
						elif event.key == K_LEFT:
							dk.deplacer('gauche')
							main_case_x = dk.case_x
						elif event.key == K_UP:
							dk.deplacer('haut')
							main_case_y = dk.case_y
						elif event.key == K_DOWN:
							dk.deplacer('bas')
							main_case_y = dk.case_y	
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

				fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
				pygame.display.flip()

				#Victoire -> Retour à l'accueil
				if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==1 and main_item2==1 and main_item3 == 1:
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


				if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==0 and main_item2==0 and main_item3==0 and rire_son == True:
					sound_rire.set_volume(0.1)
					sound_rire.play(1)

				if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==1 and main_item2==0 and main_item3==0 and rire_son == True:
					sound_rire.set_volume(0.1)
					sound_rire.play(1)


				if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==0 and main_item2==1 and main_item3==0 and rire_son == True:
					sound_rire.set_volume(0.1)
					sound_rire.play(1)


				if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==0 and main_item2==0 and main_item3==1 and rire_son == True:
					sound_rire.set_volume(0.1)
					sound_rire.play(1)


				if niveau.structure[dk.case_y][dk.case_x] == '1':
					if main_item1 == 0:
						sound_item.set_volume(0.15)
						sound_item.play()

					main_item1 = 1
					niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)


				if niveau.structure[dk.case_y][dk.case_x] == '2':
					if main_item2 == 0:
						sound_item.set_volume(0.15)
						sound_item.play()
					main_item2 = 1
					niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)


				if niveau.structure[dk.case_y][dk.case_x] == '3':
					if main_item3 == 0:
						sound_item.set_volume(0.15)
						sound_item.play()
					main_item3 = 1
					niveau.afficher_tot(fenetre,main_item1,main_item2,main_item3,main_case_x,main_case_y)

				if niveau.structure[dk.case_y][dk.case_x] == 'd' and main_item1==0 and main_item2==0 and main_item3 == 0:
					lumiere = 1
					niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)

				main_itemtot = main_item1 + main_item2 + main_item3

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
						main_item1 = 0
						main_item2 = 0 
						main_item3 = 0
						main_itemtot = 0
						choix_niveau = 0
						#init timer
						frameCount = 0
						rire_son = False
						
						sound_background.stop()

					#Touches de déplacement
					elif event.key == K_RIGHT:
						dk.deplacer('droite')
					elif event.key == K_LEFT:
						dk.deplacer('gauche')
					elif event.key == K_UP:
						dk.deplacer('haut')
					elif event.key == K_DOWN:
						dk.deplacer('bas')	
					elif event.key == K_RETURN:
						sound_background.stop()


			#Affichages aux nouvelles positions
			fenetre.blit(fond, (0,0))
			niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)

			myfont = pygame.font.Font("Images/font.ttf", 19)
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

			fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
			pygame.display.flip()



			#Victoire -> Retour à l'accueil
			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==1 and main_item2==1 and main_item3 == 1:
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


			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==0 and main_item2==0 and main_item3==0 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)

			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==1 and main_item2==0 and main_item3==0 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)


			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==0 and main_item2==1 and main_item3==0 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)


			if niveau.structure[dk.case_y][dk.case_x] == 'a' and main_item1==0 and main_item2==0 and main_item3==1 and rire_son == True:
				sound_rire.set_volume(0.1)
				sound_rire.play(1)


			if niveau.structure[dk.case_y][dk.case_x] == '1':
				if main_item1 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()

				main_item1 = 1
				niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)


			if niveau.structure[dk.case_y][dk.case_x] == '2':
				if main_item2 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()
				main_item2 = 1
				niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)

			if niveau.structure[dk.case_y][dk.case_x] == '3':
				if main_item3 == 0:
					sound_item.set_volume(0.15)
					sound_item.play()
				main_item3 = 1
				niveau.afficher_tot_1(fenetre,main_item1,main_item2,main_item3)

			main_itemtot = main_item1 + main_item2 + main_item3

