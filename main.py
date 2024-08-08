import pygame
from random import randint
import time
import sys

def jogar():
    pygame.init()
    pygame.key.get_focused()
    tela = pygame.display.set_mode((700,700))

    #Diminuindo os fps para otimizar o jogo v
    clock = pygame.time.Clock()
    #Diminuindo os fps para otimizar o jogo ^


    #CARREGANDO IMAGENS v
    knight = pygame.image.load('imagens/Knight.png')
    knight = pygame.transform.scale(knight,(48,48),)

    princesa = pygame.image.load('imagens/Princesa.png')
    princesa = pygame.transform.scale(princesa,(48,48))

    grama = pygame.image.load('imagens/Grama.png')
    grama = pygame.transform.scale(grama,(48,48))

    barreira = pygame.image.load('imagens/Preda.png')
    barreira = pygame.transform.scale(barreira,(48,48))

    grid = pygame.image.load('imagens/Mapa.png')
    grid = pygame.transform.scale(grid,(480,480))
    #CARREGANDO IMAGENS ^

    #krect = knight.get_rect(topleft=(40,60))

    #knight = pygame.transform.flip(knight,) #isso vai ser para virar o personagem ao trocar de lado



    #teste = pygame.draw.line(tela,'white',10,18,5)

    run = True
    while run:
        #EVENTOS v
        
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                
                run = False

        #EVENTOS ^

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

        tela.blit(knight,(112,112))
        tela.blit(princesa,(160,160))
        #tela.blit(knight,krect)

        
        
        pygame.display.flip()
        dt = clock.tick(30)
    pygame.quit()
    
if __name__ == '__main__':
    jogar()

