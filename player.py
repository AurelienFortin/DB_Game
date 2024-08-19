import pygame
from projectile import BouledeFeu 

# Création d'une classe joueur
class Joueur(pygame.sprite.Sprite):
    def __init__(self): # Attributs par défaut du joueur
        super().__init__()
        self.sante = 100
        self.max_sante = 100
        self.attaque = 10
        self.vitesse = 3
        self.image = pygame.image.load('Ressources/Persos/Perso_Jules_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 300
        self.all_projectiles = pygame.sprite.Group()

    def boule_de_feu_1(self, orientation):
        self.all_projectiles.add(BouledeFeu(self, orientation))

    def deplacement_droite(self):
        self.rect.x += self.vitesse

    def deplacement_gauche(self):
        self.rect.x -= self.vitesse