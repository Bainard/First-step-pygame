

import pygame
from pygame.locals import * # import des constantes dans le script (pourquoi???)

pygame.init()               #initialisation OBLIGATOIRE AU DEBUT!!!!

#creation fenetre
fenetre = pygame.display.set_mode((1298, 679))          #para de la fenetre tulpe = taille en pixel



#chargement image background

fond = pygame.image.load("background.png").convert()
fenetre.blit(fond, (0,0)) #collage du background ??? SDL a etudier

#chargement perso

perso = pygame.image.load("perso.png").convert_alpha() #alpha pour transparence
fenetre.blit(perso, (222,448))

#rafraichissement de lecran ???

pygame.display.flip()


#boucle
continuer = 1              #boucle infinie pour garder la fenetre ouverte
while continuer:
    continue
