import pygame
from random import randint
import time


pygame.init()
pygame.key.get_focused()
tela = pygame.display.set_mode((700,700))


#CARREGANDO IMAGENS v
knight = pygame.image.load('imagens/Knight.png')
knight = pygame.transform.scale(knight,(48,48),)

princesa = pygame.image.load('imagens/Princesa.png')
princesa = pygame.transform.scale(princesa,(48,48))

grama = pygame.image.load('imagens/grama64x64.png')
grama = pygame.transform.scale(grama,(48,48))

barreira = pygame.image.load('imagens/preda.png.png')
barreira = pygame.transform.scale(barreira,(48,48))

grid = pygame.image.load('imagens/Mapa.png')
grid = pygame.transform.scale(grid,(480,480))
#CARREGANDO IMAGENS ^

#krect = knight.get_rect(topleft=(40,60))

#knight = pygame.transform.flip(knight,) #isso vai ser para virar o personagem ao trocar de lado



#teste = pygame.draw.line(tela,'white',10,18,5)

run = True
while run:

    for a in range(0,10):
        for b in range(0,10):
            tela.blit(grama,(110+48*a,110+48*b))
    
    for a in range(0,12):

        tela.blit(barreira,(64+48*a,64))
        tela.blit(barreira,(64+48*a,592))
        tela.blit(barreira,(592,64+48*a))
        tela.blit(barreira,(64,64+48*a))


    tela.blit(grid,(110,110))

    # tela.blit(knight,(110,110))
    tela.blit(princesa,(156,156))
    #tela.blit(knight,krect)

    #EVENTOS v
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if event.type == pygame.K_w:
        #     pass
        
    #EVENTOS ^
    
    pygame.display.flip()
pygame.quit()


