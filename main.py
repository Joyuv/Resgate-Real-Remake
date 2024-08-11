import pygame
from random import randint
import time
import sys

def jogar():
#region PREPARAÇÃO DO AMBIENTE
    pygame.init() #iniciando o módulo pygame
    pygame.key.get_focused() #função para reconhecer eventos do teclado
    
    icone = pygame.image.load('imagens/Icon.png')

    tela = pygame.display.set_mode((700,700)) #setando resolução da tela
    pygame.display.set_caption('Resgate Real') #nome da janela
    pygame.display.set_icon(icone) #icone da janela
    
    clock = pygame.time.Clock() #variável clock para diminuir os FPS em breve
    

#endregion PREPARAÇÃO DO AMBIENTE

#region CARREGANDO IMAGENS
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
    #endregion CARREGANDO IMAGENS

    charx = 112 + 48*randint(0,9)
    chary = 112 + 48*randint(0,9)



    olhando = 'Direita'

    run = True
    while run:
        #region EVENTOS
        
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                
                run = False

            #region Movimento
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if charx + 48 >= 590:
                        pass
                    else:
                        charx += 48
                        if olhando == "Esquerda":
                            knight = pygame.transform.flip(knight, True, False)
                            olhando = "Direita"
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if charx - 48 <= 110:
                        pass
                    else:
                        charx -= 48
                        if olhando == "Direita":
                            knight = pygame.transform.flip(knight, True, False)
                            olhando = "Esquerda"

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if chary - 48 <= 110:
                        pass
                    else:
                        chary -= 48
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
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
        clock.tick(30) #Diminuindo os fps para otimizar o jogo
    pygame.quit()
    
if __name__ == '__main__':
    jogar()

