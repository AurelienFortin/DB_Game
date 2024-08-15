import pygame
from jeu import Jeu

pygame.init()

pygame.display.set_caption(title = "Notre jeu Dragon Ball")
ecran_principal = pygame.display.set_mode((1080, 720))

fond_ecran = pygame.image.load('Ressources/Fond/fond_1.jpg')

# Chargement du jeu
Game = Jeu()

running = True

while running:

    # On rajoute le fond d'écran sur la fenêtre principale
    ecran_principal.blit(fond_ecran, (20, 10))
    # On applique l'image du joueur
    ecran_principal.blit(Game.joueur.image, Game.joueur.rect)
    # On vérifie l'appui sur des touches
    if Game.pressed.get(pygame.K_RIGHT) and Game.joueur.rect.x < ecran_principal.get_width()-120:
        Game.joueur.deplacement_droite()
    elif Game.pressed.get(pygame.K_LEFT) and Game.joueur.rect.x > 0:
        Game.joueur.deplacement_gauche()


    # On met à jour la fenêtre pour qu'elle affiche le fond d'écran
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            Game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False
