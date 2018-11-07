"""Classes"""

import pygame
from pygame.locals import * 
from Datas import *
from pygame.locals import *


class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
	
	
	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		mur = pygame.image.load(image_mur).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		item1 = pygame.image.load(image_item1).convert_alpha()
		item2 = pygame.image.load(image_item2).convert_alpha()
		item3 = pygame.image.load(image_item3).convert_alpha()
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x,y))
				elif sprite == '1':		   #1 = PVC
					fenetre.blit(item1, (x,y))
				elif sprite == '2':		   #2 = Seringue
					fenetre.blit(item2, (x,y))
				elif sprite == '3':		   #3= Ether
					fenetre.blit(item3, (x,y))
				num_case += 1
			num_ligne += 1
	


	def afficher_tot_1(self, fenetre, item_1, item_2, item_3):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		mur = pygame.image.load(image_mur).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		item1 = pygame.image.load(image_item1).convert_alpha()
		item2 = pygame.image.load(image_item2).convert_alpha()
		item3 = pygame.image.load(image_item3).convert_alpha()
		item1_sol = pygame.image.load(image_item1_sol).convert_alpha()
		item2_sol =	pygame.image.load(image_item2_sol).convert_alpha()
		item3_sol = pygame.image.load(image_item3_sol).convert_alpha()
		
		#Cas n°1/8
		if (item_1 == 0) and (item_2 == 0) and (item_3 == 0) :
			#On parcourt la liste du niveau
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					if sprite == 'm':		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'd':		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'a':		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == '1':		   #1 = PVC
						fenetre.blit(item1, (x,y))
					elif sprite == '2':		   #2 = Seringue
						fenetre.blit(item2, (x,y))
					elif sprite == '3':		   #3= Ether
						fenetre.blit(item3, (x,y))
					num_case += 1
				num_ligne += 1
		
		#Cas n°2/8
		if (item_1 == 1) and (item_2 == 0) and (item_3 == 0) :
			#On parcourt la liste du niveau
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					if sprite == 'm':		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'd':		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'a':		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == '1':		   #1 = PVC
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '2':		   #2 = Seringue
						fenetre.blit(item2, (x,y))
					elif sprite == '3':		   #3= Ether
						fenetre.blit(item3, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°3/8
		if (item_1 == 0) and (item_2 == 1) and (item_3 == 0) :
			#On parcourt la liste du niveau
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					if sprite == 'm':		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'd':		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'a':		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == '1':		   #1 = PVC
						fenetre.blit(item1, (x,y))
					elif sprite == '2':		   #2 = Seringue
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '3':		   #3= Ether
						fenetre.blit(item3, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°4/8
		if (item_1 == 1) and (item_2 == 1) and (item_3 == 0) :
			#On parcourt la liste du niveau
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					if sprite == 'm':		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'd':		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'a':		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == '1':		   #1 = PVC
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '2':		   #2 = Seringue
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '3':		   #3= Ether
						fenetre.blit(item3, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°5/8
		if (item_1 == 0) and (item_2 == 0) and (item_3 == 1) :
			#On parcourt la liste du niveau
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					if sprite == 'm':		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'd':		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'a':		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == '1':		   #1 = PVC
						fenetre.blit(item1, (x,y))
					elif sprite == '2':		   #2 = Seringue
						fenetre.blit(item2, (x,y))
					elif sprite == '3':		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°6/8
		if (item_1 == 1) and (item_2 == 0) and (item_3 == 1) :
			#On parcourt la liste du niveau
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					if sprite == 'm':		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'd':		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'a':		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == '1':		   #1 = PVC
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '2':		   #2 = Seringue
						fenetre.blit(item2, (x,y))
					elif sprite == '3':		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					num_case += 1
				num_ligne += 1
		#Cas n°7/8
		if (item_1 == 0) and (item_2 == 1) and (item_3 == 1) :
			#On parcourt la liste du niveau
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					if sprite == 'm':		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'd':		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'a':		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == '1':		   #1 = PVC
						fenetre.blit(item1, (x,y))
					elif sprite == '2':		   #2 = Seringue
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '3':		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°8/8
		if (item_1 == 1) and (item_2 == 1) and (item_3 == 1) :
			#On parcourt la liste du niveau
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					if sprite == 'm':		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'd':		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'a':		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == '1':		   #1 = PVC
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '2':		   #2 = Seringue
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '3':		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					num_case += 1
				num_ligne += 1


#################################################################################################################################################################
#################################################################################################################################################################

	#La fonction suivante ne doit pas être prise en compte, elle est le résultat d'un essai béta du jeu (que l'on peut activer en appuyant sur F2 (mode medium) ou F3 (mode hard) à l'écran d'accueil)

	def afficher_tot(self, fenetre, item_1, item_2, item_3, case_x,case_y):
		"""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()"""
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		mur = pygame.image.load(image_mur).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		item1 = pygame.image.load(image_item1).convert_alpha()
		item2 = pygame.image.load(image_item2).convert_alpha()
		item3 = pygame.image.load(image_item3).convert_alpha()
		item1_sol = pygame.image.load(image_item1_sol).convert_alpha()
		item2_sol =	pygame.image.load(image_item2_sol).convert_alpha()
		item3_sol = pygame.image.load(image_item3_sol).convert_alpha()
		mur_noir = pygame.image.load(image_mur_noir).convert_alpha()
		
		#Cas n°1/8
		if (item_1 == 0) and (item_2 == 0) and (item_3 == 0) :
			#On parcourt la liste du niveau
			case_perso_x = case_x
			case_perso_y = case_y
			case_plus_x = case_x + 1
			case_moins_x = case_x - 1
			case_plus_y = case_y + 1
			case_moins_y = case_y - 1
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					#mur
					if sprite == 'm' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					#depart
					elif sprite == 'd' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))	
					#arrivée
					elif sprite == 'a' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))	
					#barre
					elif sprite == '1' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #1 = PVC
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					#Seringue
					elif sprite == '2' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #2 = Seringue
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					#Ether
					elif sprite == '3' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					#Sol
					elif sprite == '0' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					
					else :
						fenetre.blit(mur_noir, (x,y))
					num_case += 1
				num_ligne += 1
		
		#Cas n°2/8
		if (item_1 == 1) and (item_2 == 0) and (item_3 == 0) :
			#On parcourt la liste du niveau
			case_perso_x = case_x
			case_perso_y = case_y
			case_plus_x = case_x + 1
			case_moins_x = case_x - 1
			case_plus_y = case_y + 1
			case_moins_y = case_y - 1
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					#mur
					if sprite == 'm' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					#depart
					elif sprite == 'd' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))	
					#arrivée
					elif sprite == 'a' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))	
					#barre
					elif sprite == '1' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #1 = PVC
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					#Seringue
					elif sprite == '2' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #2 = Seringue
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					#Ether
					elif sprite == '3' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					#Sol
					elif sprite == '0' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					
					else :
						fenetre.blit(mur_noir, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°3/8
		if (item_1 == 0) and (item_2 == 1) and (item_3 == 0) :
			#On parcourt la liste du niveau
			case_perso_x = case_x
			case_perso_y = case_y
			case_plus_x = case_x + 1
			case_moins_x = case_x - 1
			case_plus_y = case_y + 1
			case_moins_y = case_y - 1
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					#mur
					if sprite == 'm' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					#depart
					elif sprite == 'd' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))	
					#arrivée
					elif sprite == 'a' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))	
					#barre
					elif sprite == '1' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #1 = PVC
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					#Seringue
					elif sprite == '2' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #2 = Seringue
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					#Ether
					elif sprite == '3' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					#Sol
					elif sprite == '0' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					
					else :
						fenetre.blit(mur_noir, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°4/8
			#On parcourt la liste du niveau
		if (item_1 == 1) and (item_2 == 1) and (item_3 == 0) :
			case_perso_x = case_x
			case_perso_y = case_y
			case_plus_x = case_x + 1
			case_moins_x = case_x - 1
			case_plus_y = case_y + 1
			case_moins_y = case_y - 1
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					#mur
					if sprite == 'm' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					#depart
					elif sprite == 'd' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))	
					#arrivée
					elif sprite == 'a' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))	
					#barre
					elif sprite == '1' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #1 = PVC
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					#Seringue
					elif sprite == '2' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #2 = Seringue
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					#Ether
					elif sprite == '3' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3, (x,y))
					#Sol
					elif sprite == '0' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					
					else :
						fenetre.blit(mur_noir, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°5/8
		if (item_1 == 0) and (item_2 == 0) and (item_3 == 1) :
			#On parcourt la liste du niveau
			case_perso_x = case_x
			case_perso_y = case_y
			case_plus_x = case_x + 1
			case_moins_x = case_x - 1
			case_plus_y = case_y + 1
			case_moins_y = case_y - 1
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					#mur
					if sprite == 'm' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					#depart
					elif sprite == 'd' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))	
					#arrivée
					elif sprite == 'a' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))	
					#barre
					elif sprite == '1' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #1 = PVC
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					#Seringue
					elif sprite == '2' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #2 = Seringue
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					#Ether
					elif sprite == '3' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					#Sol
					elif sprite == '0' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					
					else :
						fenetre.blit(mur_noir, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°6/8
		if (item_1 == 1) and (item_2 == 0) and (item_3 == 1) :
			#On parcourt la liste du niveau
			case_perso_x = case_x
			case_perso_y = case_y
			case_plus_x = case_x + 1
			case_moins_x = case_x - 1
			case_plus_y = case_y + 1
			case_moins_y = case_y - 1
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					#mur
					if sprite == 'm' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					#depart
					elif sprite == 'd' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))	
					#arrivée
					elif sprite == 'a' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))	
					#barre
					elif sprite == '1' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #1 = PVC
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					#Seringue
					elif sprite == '2' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #2 = Seringue
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2, (x,y))
					#Ether
					elif sprite == '3' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					#Sol
					elif sprite == '0' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					
					else :
						fenetre.blit(mur_noir, (x,y))
					num_case += 1
				num_ligne += 1
		#Cas n°7/8
		if (item_1 == 0) and (item_2 == 1) and (item_3 == 1) :
			#On parcourt la liste du niveau
			case_perso_x = case_x
			case_perso_y = case_y
			case_plus_x = case_x + 1
			case_moins_x = case_x - 1
			case_plus_y = case_y + 1
			case_moins_y = case_y - 1
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					#mur
					if sprite == 'm' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					#depart
					elif sprite == 'd' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))	
					#arrivée
					elif sprite == 'a' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))	
					#barre
					elif sprite == '1' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #1 = PVC
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1, (x,y))
					#Seringue
					elif sprite == '2' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #2 = Seringue
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					#Ether
					elif sprite == '3' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					#Sol
					elif sprite == '0' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					
					else :
						fenetre.blit(mur_noir, (x,y))
					num_case += 1
				num_ligne += 1

		#Cas n°8/8
		if (item_1 == 1) and (item_2 == 1) and (item_3 == 1) :
			#On parcourt la liste du niveau
			case_perso_x = case_x
			case_perso_y = case_y
			case_plus_x = case_x + 1
			case_moins_x = case_x - 1
			case_plus_y = case_y + 1
			case_moins_y = case_y - 1
			num_ligne = 0
			for ligne in self.structure:
				#On parcourt les listes de lignes
				num_case = 0
				for sprite in ligne:
					#On calcule la position réelle en pixels
					x = num_case * taille_sprite
					y = num_ligne * taille_sprite
					#mur
					if sprite == 'm' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					elif sprite == 'm' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(mur, (x,y))
					#depart
					elif sprite == 'd' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #d = Départ
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(depart, (x,y))
					elif sprite == 'd' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(depart, (x,y))	
					#arrivée
					elif sprite == 'a' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #a = Arrivée
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))
					elif sprite == 'a' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(arrivee, (x,y))	
					#barre
					elif sprite == '1' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #1 = PVC
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					elif sprite == '1' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item1_sol, (x,y))
					#Seringue
					elif sprite == '2' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #2 = Seringue
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					elif sprite == '2' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item2_sol, (x,y))
					#Ether
					elif sprite == '3' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '3' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					#Sol
					elif sprite == '0' and (num_case == case_plus_x and num_ligne == case_perso_y):		   #3= Ether
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_moins_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_plus_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_moins_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					elif sprite == '0' and (num_case == case_perso_x and num_ligne == case_perso_y):		   #m = Mur
						fenetre.blit(item3_sol, (x,y))
					
					else :
						fenetre.blit(mur_noir, (x,y))
					num_case += 1
				num_ligne += 1


#################################################################################################################################################################
#################################################################################################################################################################


class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		pygame.display.flip()
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau
	
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas

