from typing import Any
import pygame
from constantes import *
from auxiliar import Auxiliar
from enemigo import *

class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y, direccion, player, p_scale=1):
        super().__init__()
        self.player = player
        self.disparo_d = Auxiliar.getSurfaceFromSeparateFiles("C:/Users/rarug/Desktop/Rarug Francisco- Juego-python/Juego/images/Object/{0}.png", 1, 5, flip=False, scale=p_scale)
        self.disparo_i = Auxiliar.getSurfaceFromSeparateFiles("C:/Users/rarug/Desktop/Rarug Francisco- Juego-python/Juego/images/Object/{0}.png", 1, 5, flip=True, scale=p_scale)
        self.direccion = direccion
        self.velocidad = 5  # Velocidad de movimiento del objeto
        self.frame = 0
        if direccion == DIRECTION_R:
            self.animaciones = self.disparo_d
        elif direccion == DIRECTION_L:
            self.animaciones = self.disparo_i
            self.velocidad *= -1  # Invierte la velocidad para moverse hacia la izquierda
        else:
            self.animaciones = None
        self.image = self.animaciones[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.rect.x += self.velocidad
        self.frame += 1
        if self.frame >= len(self.animaciones):
            self.frame = 0
        self.image = self.animaciones[self.frame]
        # Si el objeto sale de la ventana, se elimina
        if self.rect.right < 0 or self.rect.left > ANCHO_VENTANA:
            self.player.attack_launched = False
            self.kill()

class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, path, scale=1):
        super().__init__()
        self.scale = scale
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.angle=0

    def update(self, delta_ms) -> None:
        self.angle+=1
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Trampa(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, scale=1):
        super().__init__()
        self.scale = scale
        self.image = pygame.image.load(image_path)
        #self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale), int(self.image.get_height() * self.scale)))
        self.image = pygame.transform.rotozoom(self.image, 0, self.scale )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)


