import pygame

# Définition de la classe de la boule de feu

class BouledeFeu(pygame.sprite.Sprite):
    # Constructeur de la classe (i.e. valeurs par défaut quand on crée un objet de la classe)
    def __init__(self, joueur, orientation):
        super().__init__()
        self.vitesse = 2
        self.player = joueur
        self.image = pygame.image.load('Ressources/Projectiles/projectile.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.orientation = orientation # On gère l'orientation du projectile
        if self.orientation == "droite":
            self.rect.x = joueur.rect.x + 120
            self.rect.y = joueur.rect.y + 120
        elif self.orientation == "gauche":
            self.rect.x = joueur.rect.x - 30
            self.rect.y = joueur.rect.y + 120
        self.origin_image = self.image
        self.angle = 0

    def deplacement_droite(self):
        self.rect.x += self.vitesse
        self.rotation_projectile()
        # On vérifie si la boule de feu n'est plus sur l'écran
        if self.rect.x > 1080:
            self.supprimer_projectile()

    def deplacement_gauche(self):
        self.rect.x -= self.vitesse
        self.rotation_projectile()
        # On vérifie si la boule de feu n'est plus sur l'écran
        if self.rect.x < 0:
            self.supprimer_projectile()

    def supprimer_projectile(self):
        self.player.all_projectiles.remove(self)

    def rotation_projectile(self):
        # On fait tourner le projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

