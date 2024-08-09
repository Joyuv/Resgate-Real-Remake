import pygame
from random import randint
import time
import sys


pygame.init()
pygame.key.get_focused()
tela = pygame.display.set_mode((700,700))


#region CARREGANDO IMAGENS
knight = pygame.image.load('imagens/Knight.png')
knight = pygame.transform.scale(knight,(48,48),)
olhando = 'Direita'

princesa = pygame.image.load('imagens/Princesa.png')
princesa = pygame.transform.scale(princesa,(48,48))

grama = pygame.image.load('imagens/Grama.png')
grama = pygame.transform.scale(grama,(48,48))

barreira = pygame.image.load('imagens/Preda.png')
barreira = pygame.transform.scale(barreira,(48,48))

grid = pygame.image.load('imagens/Mapa.png')
grid = pygame.transform.scale(grid,(480,480))
#endregion CARREGANDO IMAGENS

charx = 112 + 48*randint(0,9)
chary = 112 + 48*randint(0,9)

#krect = knight.get_rect(topleft=(40,60))

#knight = pygame.transform.flip(knight,) #isso vai ser para virar o personagem ao trocar de lado



#teste = pygame.draw.line(tela,'white',10,18,5)

run = True
while run:
    #region EVENTOS
    
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            
            run = False

        #region Movimento
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                if charx + 48 >= 590:
                    pass
                else:
                    charx += 48
                    if olhando == "Esquerda":
                        knight = pygame.transform.flip(knight, True, False)
                        olhando = "Direita"
            if event.key == pygame.K_a:
                if charx - 48 <= 110:
                    pass
                else:
                    charx -= 48
                    if olhando == "Direita":
                        knight = pygame.transform.flip(knight, True, False)
                        olhando = "Esquerda"

            if event.key == pygame.K_w:
                if chary - 48 <= 110:
                    pass
                else:
                    chary -= 48
            if event.key == pygame.K_s:
                if chary + 48 >= 590:
                    pass
                else:
                    chary += 48
        #endregion Movimento

    #endregion EVENTOS

    tela.fill('gray')

    for a in range(0,10):
        for b in range(0,10):
            tela.blit(grama,(112+48*a,112+48*b))
    
    for a in range(0,12):

        tela.blit(barreira,(64+48*a,64))
        tela.blit(barreira,(64+48*a,592))
        tela.blit(barreira,(592,64+48*a))
        tela.blit(barreira,(64,64+48*a))


    tela.blit(grid,(112,112))

    tela.blit(knight,(charx,chary))
    tela.blit(princesa,(160,160))
    #tela.blit(knight,krect)


    pygame.display.flip()
pygame.quit()
sys.exit()

