import pygame
from pygame.locals import * # import des constantes dans le script (pourquoi???)

pygame.init()               #initialisation OBLIGATOIRE AU DEBUT!!!!

fenetre = pygame.display.set_mode((640, 480))          #para de la fenetre tulpe = taille en pixel

fond = pygame.image.load("background.png").convert() #chargement image background
fenetre.blit(fond, (0,0)) #collage du background ??? SDL a etudier

pygame.display.flip() #rafraichissement de lecran ???

continuer = 1              #boucle infinie pour garder la fenetre ouverte
while continuer:
    continue
