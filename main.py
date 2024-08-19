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

    # On gère l'ensemble des projectiles
    for projectile in Game.joueur.all_projectiles:
        if projectile.orientation == "gauche":
            projectile.deplacement_gauche()
        elif projectile.orientation == "droite":
            projectile.deplacement_droite()

    # On applique l'ensemble des images du groupe de projectiles
    Game.joueur.all_projectiles.draw(ecran_principal)

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
            # Si on appuie sur Espace, on lance une boule de feu qui va se déplacer à droite
            # Si on appuie sur K, on lance une boule de feu qui va se déplacer à gauche
            if event.key == pygame.K_z: # Si on appuie sur Z, on lance une boule de feu vers la droite
                Game.joueur.boule_de_feu_1(orientation = "droite")
            if event.key == pygame.K_a: # Si on appuie sur A, on lance une boule de feu vers la gauche
                Game.joueur.boule_de_feu_1(orientation = "gauche")
        elif event.type == pygame.KEYUP:
            Game.pressed[event.key] = False
