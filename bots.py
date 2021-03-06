import pygame
import time
from bombes import Bombe
from constantes import *


class Bot(pygame.sprite.Sprite):
    def __init__(self, game, x, y, NumeroPlayer):
        super().__init__()
        self.game = game
        self.imageliste = [pygame.image.load(
            "assets/players/player1.png"), pygame.image.load("assets/players/deathState.png")]
        self.image = self.imageliste[0]
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def place(self, x, y):
        self.rect.x = self.x * TILESISE
        self.rect.y = self.y * TILESISE
