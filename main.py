import pygame
from random import randint
import time


pygame.init()

tela = pygame.display.set_mode((700,700))


#CARREGANDO IMAGENS v
knight = pygame.image.load('imagens/Knight.png')
knight = pygame.transform.scale(knight,(48,48))

princesa = pygame.image.load('imagens/Princesa.png')
princesa = pygame.transform.scale(princesa,(48,48))

grama = pygame.image.load('imagens/grama64x64.png')
grama = pygame.transform.scale(grama,(48,48))
#CARREGANDO IMAGENS ^

#knight = pygame.transform.flip(knight,) #isso vai ser para virar o personagem ao trocar de lado



#teste = pygame.draw.line(tela,'white',10,148,5)

run = True
while run:
    for a in range(0,10):
        for b in range(0,10):
            tela.blit(grama,(148+48*a,148+48*b))
    tela.blit(knight,(148,148))
    tela.blit(princesa,(148+48,148))

    #EVENTOS v
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    #EVENTOS ^



    pygame.display.flip()
pygame.quit()


