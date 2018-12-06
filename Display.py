"""Classes"""

import pygame
from pygame.locals import *
from Datas import *
from pygame.locals import *


class Niveau:
    """CLASS LEVEL CREATOR"""

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = 0

    def generer(self):
        with open(self.fichier, "r") as fichier:  # File opening + reading
            structure_niveau = []
            for ligne in fichier:  # For each line in the file
                ligne_niveau = []
                # we read all lines and characters in the file
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)
            self.structure = structure_niveau  # We save the level structure

    def afficher_tot_1(self, fenetre, item_1, item_2, item_3):
        mur = pygame.image.load(IMAGE_MUR).convert()  # images loading
        depart = pygame.image.load(IMAGE_DEPART).convert()
        arrivee = pygame.image.load(IMAGE_ARRIVEE).convert_alpha()
        item1 = pygame.image.load(IMAGE_ITEM1).convert_alpha()
        item2 = pygame.image.load(IMAGE_ITEM2).convert_alpha()
        item3 = pygame.image.load(IMAGE_ITEM3).convert_alpha()
        item1_sol = pygame.image.load(IMAGE_ITEM1_SOL).convert_alpha()
        item2_sol = pygame.image.load(IMAGE_ITEM2_SOL).convert_alpha()
        item3_sol = pygame.image.load(IMAGE_ITEM3_SOL).convert_alpha()

        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:  # We read all lines and characters
                x = num_case * taille_sprite
                y = num_ligne * taille_sprite
                if sprite == 'm':  # m = Mur = wall
                    fenetre.blit(mur, (x, y))
                elif sprite == 'd':  # d = Départ = start
                    fenetre.blit(depart, (x, y))
                elif sprite == 'a':  # a = Arrivée = end
                    fenetre.blit(arrivee, (x, y))
                if sprite == '1' and (item_1 == 1):  # 1 = PVC
                    fenetre.blit(item1_sol, (x, y))
                elif sprite == '1' and (item_1 == 0):  #
                    fenetre.blit(item1, (x, y))
                if sprite == '2' and (item_2 == 1):  # 2 = Seringue
                    fenetre.blit(item2_sol, (x, y))
                elif sprite == '2' and (item_2 == 0):  #
                    fenetre.blit(item2, (x, y))
                if sprite == '3' and (item_3 == 1):  # 1 = Ether
                    fenetre.blit(item3_sol, (x, y))
                elif sprite == '3' and (item_3 == 0):  #
                    fenetre.blit(item3, (x, y))
                num_case += 1
            num_ligne += 1


class Perso:
    """Classe permettant de créer un personnage"""

    def __init__(self, droite, gauche, haut, bas, niveau):
        # Sprites
        self.droite = pygame.image.load(droite).convert_alpha()
        self.gauche = pygame.image.load(gauche).convert_alpha()
        self.haut = pygame.image.load(haut).convert_alpha()
        self.bas = pygame.image.load(bas).convert_alpha()
        # Player position
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        pygame.display.flip()
        # Default direction
        self.direction = self.droite
        # player's level
        self.niveau = niveau

    def deplacer(self, direction):
        """Methode permettant de déplacer le personnage"""
        # Right direction
        if direction == 'droite':
            # the player can't walk after the wall
            if self.case_x < (nombre_sprite_cote - 1):

                if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                    # Mooving
                    self.case_x += 1
                    # Pixel position
                    self.x = self.case_x * taille_sprite
            # image direction
            self.direction = self.droite

        # Left direction
        if direction == 'gauche':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.gauche

        # Top direction
        if direction == 'haut':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.haut

        # Bottom direction
        if direction == 'bas':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bas
