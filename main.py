import pygame
from random import randint
import time


pygame.init()

tela = pygame.display.set_mode((600,600))

knight = pygame.image.load('imagens/Knight.png')
knight = pygame.transform.scale(knight,(48,48))

princess = pygame.image.load('imagens/Princesa.png')
princess = pygame.transform.scale(princess,(48,48))
#knight = pygame.transform.flip(knight,) #isso vai ser para virar o personagem ao trocar de lado


#APRENDER A USAR DRAW v
#teste = pygame.draw.line(tela,'white', 10,480,5)
#APRENDER A USAR DRAW ^
run = True
while run:
    tela.blit(knight,(148,148))
    tela.blit(princess,(148+48,148))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()


