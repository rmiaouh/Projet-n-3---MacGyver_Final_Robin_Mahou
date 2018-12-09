#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""
Main program
"""
import pygame
import MazeGenerator_0
import random
from random import randint
from pygame.locals import *
from Display import *
from Datas import *

pygame.init()

# fenêtre Pygame // Pygame Window
window = pygame.display.set_mode((cote_window, cote_window))
icone = pygame.image.load(IMAGE_ICONE)  # Icone // Icon
pygame.display.set_icon(icone)  # Titre du jeu // Game Title
pygame.display.set_caption(TITRE_FENETRE)

# BOUCLE PRINCIPALE // MAIN LOOP
continuer = 1
main_itemtot = 0
main_item1 = 0
main_item2 = 0
main_item3 = 0
lumiere = 0
main_case_x = 0
main_case_y = 0
# Variables liées au timer // Timer variables
timer = pygame.time.Clock()
frameRate = 60
frameCount = 1
# Musiques & sons utilisés // Sound variables
sound_item = pygame.mixer.Sound(DATA_SOUND_ITEM)
sound_sword = pygame.mixer.Sound(DATA_SOUND_SWORD)
sound_musique_0 = pygame.mixer.Sound(DATA_SOUND_MUSIQUE_0)
sound_gameover = pygame.mixer.Sound(DATA_SOUND_GAMEOVER)
sound_win = pygame.mixer.Sound(DATA_SOUND_WIN)

while continuer:
    # home loading
    accueil = pygame.image.load(IMAGE_ACCUEIL).convert()
    window.blit(accueil, (0, 0))
    pygame.display.flip()  # Refreshing
    # each loop we put variables to 0
    continue_game = 1
    continue_menu = 1
    choice_niveau = 0
    # We put some sound for the home page
    sound_background = pygame.mixer.Sound(sound_musique_0)
    sound_background.set_volume(0.2)
    sound_background.play(-1)
    # HOME LOOP
    while continue_menu:
        # Limitation de vitesse de la boucle // Clock Speed
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # If the user quit, we reset loop variables
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continue_menu = 0
                continue_game = 0
                continuer = 0
                choice = 0  # level variable

            elif event.type == KEYDOWN:
                if event.key == K_F1:  # easy mode
                    continue_menu = 0
                    # Maze generator programs
                    MazeGenerator_0.maze(15, 15)
                    choice = 'mazeFinal.txt'
                    choice_niveau = 1  # Level number variable

    if choice != 0:
        # Chargement du fond // background loading
        fond = pygame.image.load(IMAGE_FOND).convert()
        levelgm = Level(choice)  # level generation
        levelgm.generer()
        levelgm.afficher_tot_1(window, main_item1, main_item2, main_item3)
        mc = Character("Images/MacGyver2.png", "Images/MacGyver2.png",
                   "Images/MacGyver2.png", "Images/MacGyver2.png", levelgm)

    if choice_niveau == 1:

        while continue_game:  # BOUCLE DE JEU // LOOP GAME
            pygame.time.Clock().tick(60)     # Clock game variable
            totalSeconds = frameCount // frameRate
            seconds = totalSeconds % 31
            time = "00:{}".format(seconds)
            for event in pygame.event.get():
                if event.type == QUIT:
                    continue_game = 0
                    continuer = 0
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        continue_game = 0
                        main_item1 = 0  # Items variable
                        main_item2 = 0
                        main_item3 = 0
                        main_itemtot = 0  # Count how many items got the user
                        choice_niveau = 0
                        frameCount = 0  # init timer
                        rire_son = False
                        sound_background.stop()
                    elif event.key == K_RIGHT:  # Moving keys
                        mc.deplacer('right')
                    elif event.key == K_LEFT:
                        mc.deplacer('left')
                    elif event.key == K_UP:
                        mc.deplacer('top')
                    elif event.key == K_DOWN:
                        mc.deplacer('bottom')
                    elif event.key == K_RETURN:
                        sound_background.stop()
            window.blit(fond, (0, 0))  # Position refreshing
            levelgm.afficher_tot_1(window, main_item1, main_item2, main_item3)
            myfont = pygame.font.Font("Images/font.ttf", 19)  # Font variables

            if main_itemtot != 3:  # Different message
                label = myfont.render(
                    "You have {}/3 items".format(main_itemtot), 1, (255, 255, 255))
            else:
                label = myfont.render(
                    "You have {}/3 items - You can now kill the Boss".format(main_itemtot), 1, (120, 255, 120))
            window.blit(label, (10, 425))
            if seconds < 11:  # Time counter
                timeOutput = myfont.render(time, True, (250, 85, 45))
            elif seconds < 21 and seconds > 10:
                timeOutput = myfont.render(time, True, (250, 165, 45))
            else:
                timeOutput = myfont.render(time, True, (250, 250, 250))

            if seconds == 1:
                continue_game = 0
                main_item1 = 0
                main_item2 = 0
                main_item3 = 0
                main_itemtot = 0
                choice_niveau = 0
                frameCount = 0  # init timer
                sound_gameover.set_volume(0.3)
                sound_gameover.play()
                sound_background.stop()
            window.blit(timeOutput, (395, 0))
            frameCount -= 1
            timer.tick(frameRate)
            window.blit(mc.direction, (mc.x, mc.y))
            pygame.display.flip()

            # If victory -> Home page
            if levelgm.structure[mc.case_y][mc.case_x] == 'a' and main_item1 == 1 and main_item2 == 1 and main_item3 == 1:
                sound_sword.set_volume(0.7)
                sound_sword.play()
                sound_win.set_volume(0.4)
                sound_win.play()
                continue_game = 0
                main_item1 = 0
                main_item2 = 0
                main_item3 = 0
                main_itemtot = 0
                choice_niveau = 0
                frameCount = 0  # init timer
                sound_background.stop()

            # depending on the number of objects the player has
            if levelgm.structure[mc.case_y][mc.case_x] == '1':
                if main_item1 == 0:
                    sound_item.set_volume(0.15)
                    sound_item.play()
                main_item1 = 1
                levelgm.afficher_tot_1(
                    window, main_item1, main_item2, main_item3)
            if levelgm.structure[mc.case_y][mc.case_x] == '2':
                if main_item2 == 0:
                    sound_item.set_volume(0.15)
                    sound_item.play()
                main_item2 = 1
                levelgm.afficher_tot_1(
                    window, main_item1, main_item2, main_item3)
            if levelgm.structure[mc.case_y][mc.case_x] == '3':
                if main_item3 == 0:
                    sound_item.set_volume(0.15)
                    sound_item.play()
                main_item3 = 1
                levelgm.afficher_tot_1(
                    window, main_item1, main_item2, main_item3)
            main_itemtot = main_item1 + main_item2 + \
                main_item3 # Total item number
