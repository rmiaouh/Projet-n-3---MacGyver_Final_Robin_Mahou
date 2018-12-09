"""Classes"""

import pygame
from pygame.locals import *
from Datas import *
from pygame.locals import *


class Level:
    """CLASS LEVEL CREATOR"""

    def __init__(self, filegm):
        self.filegm = filegm
        self.structure = 0

    def generer(self):
        with open(self.filegm, "r") as filegm:  # File opening + reading
            structure_niveau = []
            for ligne in filegm:  # For each line in the file
                ligne_level = []
                # we read all lines and characters in the file
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_level.append(sprite)
                structure_niveau.append(ligne_level)
            self.structure = structure_niveau  # We save the level structure

    def afficher_tot_1(self, window, item_1, item_2, item_3):
        wall = pygame.image.load(IMAGE_MUR).convert()  # images loading
        startgm = pygame.image.load(IMAGE_DEPART).convert()
        endgm = pygame.image.load(IMAGE_ARRIVEE).convert_alpha()
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
                    window.blit(wall, (x, y))
                elif sprite == 'd':  # d = Départ = start
                    window.blit(startgm, (x, y))
                elif sprite == 'a':  # a = Arrivée = end
                    window.blit(endgm, (x, y))
                if sprite == '1' and (item_1 == 1):  # 1 = PVC
                    window.blit(item1_sol, (x, y))
                elif sprite == '1' and (item_1 == 0):  #
                    window.blit(item1, (x, y))
                if sprite == '2' and (item_2 == 1):  # 2 = Seringue
                    window.blit(item2_sol, (x, y))
                elif sprite == '2' and (item_2 == 0):  #
                    window.blit(item2, (x, y))
                if sprite == '3' and (item_3 == 1):  # 1 = Ether
                    window.blit(item3_sol, (x, y))
                elif sprite == '3' and (item_3 == 0):  #
                    window.blit(item3, (x, y))
                num_case += 1
            num_ligne += 1


class Character:

    def __init__(self, right, left, top, bottom, niveau):
        # Sprites
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.top = pygame.image.load(top).convert_alpha()
        self.bottom = pygame.image.load(bottom).convert_alpha()
        # Player position
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        pygame.display.flip()
        # Default direction
        self.direction = self.right
        # player's level
        self.niveau = niveau

    def deplacer(self, direction):

        # Right direction
        if direction == 'right':
            # the player can't walk after the wall
            if self.case_x < (nombre_sprite_cote - 1):

                if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
                    # Mooving
                    self.case_x += 1
                    # Pixel position
                    self.x = self.case_x * taille_sprite
            # image direction
            self.direction = self.right

        # Left direction
        if direction == 'left':
            if self.case_x > 0:
                if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * taille_sprite
            self.direction = self.left

        # Top direction
        if direction == 'top':
            if self.case_y > 0:
                if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.top

        # Bottom direction
        if direction == 'bottom':
            if self.case_y < (nombre_sprite_cote - 1):
                if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * taille_sprite
            self.direction = self.bottom
