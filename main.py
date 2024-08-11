import pygame
from random import randint, getrandbits
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

#region Personagens/Objetos
    class player():

        def __init__(self, coorx, coory):
            self.__img = pygame.transform.scale(pygame.image.load('imagens/Knight.png'), (48,48),)
            self.__olhando = True
            self.__coorx = coorx
            self.__coory = coory
        
        def get_coorx(self):
            return self.__coorx
        def get_coory(self):
            return self.__coory
        def get_olhando(self):
            return self.__olhando
        def get_img(self):
            return self.__img

        def set_coorx(self, coorx):
            self.__coorx = coorx
        def set_coory(self, coory):
            self.__coory = coory
        def set__olhando(self, olhando):
            self.__olhando = olhando
        def set_img(self, img):
            self.__img = img
        
        def mover(self, key):
            dist = 48
            if key == pygame.K_d or key == pygame.K_RIGHT:
                if self.__coorx + 48 >= 590:
                    pass
                elif any(nextrect(x='right').colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,2)):
                    pass
                else:
                    self.__coorx += dist
                    if self.__olhando == False:
                        self.__img = pygame.transform.flip(self.__img, True, False)
                        self.__olhando = True
            if key == pygame.K_a or key == pygame.K_LEFT:
                if self.__coorx - 48 <= 110:
                    pass
                elif any(nextrect(x='left').colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,2)):
                    pass
                else:
                    self.__coorx -= dist
                    if self.__olhando == True:
                        self.__img = pygame.transform.flip(self.__img, True, False)
                        self.__olhando = False
            if key == pygame.K_w or key == pygame.K_UP:
                if self.__coory - 48 < 110:
                    pass
                elif any(nextrect(y='up').colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,2)):
                        pass
                else:
                    self.__coory -= dist
            if key == pygame.K_s or key == pygame.K_DOWN:
                if self.__coory + 48 >= 590:
                    pass
                elif any(nextrect(y='down').colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,2)):
                    pass
                else:
                    self.__coory += dist

#endregion

#region CARREGANDO IMAGENS   

    princesa = pygame.image.load('imagens/Princesa.png')
    princesa = pygame.transform.scale(princesa,(48,48))

    grama = pygame.image.load('imagens/Grama.png')
    grama = pygame.transform.scale(grama,(48,48))

    barreira = pygame.image.load('imagens/Preda.png')
    barreira = pygame.transform.scale(barreira,(48,48))

    grid = pygame.image.load('imagens/Mapa.png')
    grid = pygame.transform.scale(grid,(480,480))
    #endregion CARREGANDO IMAGENS
    #region RECTS

    prinx = 112 + 48*randint(0,9)
    priny = 112 + 48*randint(0,9)

    jgdr1 = player(112 + 48*randint(0,9), 112 + 48*randint(0,9))
    
    charect = pygame.Rect(jgdr1.get_coorx(),jgdr1.get_coory(),48,48)

    prinx = 112 + 48*randint(0,9)
    priny = 112 + 48*randint(0,9)
    
    while prinx == jgdr1.get_coorx():
        random = randint(0,1)
        if random == 0:
            priny = 112 + 48*randint(0,9)
        else:
            prinx = 112 + 48*randint(0,9)

    while priny == jgdr1.get_coory():
        random = randint(0,1)
        if random == 0:
            priny = 112 + 48*randint(0,9)
        else:
            prinx = 112 + 48*randint(0,9)
    prinrect = pygame.Rect(prinx,priny,48,48)

    class Paredes:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            
        def rect(self):
            self.rectx = pygame.Rect(self.x-48,self.y,48*3, 48)
            self.recty = pygame.Rect(self.x,self.y-48,48,48*3)
            self.listarect = [self.rectx,self.recty]

            return self.listarect
        def getcord(self):
            self.listacord = [self.x,self.y]
            return self.listacord
    
    qntwall = 3

    
    rectwall = []
    cordwall = []
    for a in range(0,qntwall):
        x = 112 + 48*randint(0,9)
        y = 112 + 48*randint(0,9)



        
        rectwall.append(Paredes(x,y).rect())

        
        cordwall.append(Paredes(x,y).getcord())
    
    

    def nextrect(x=0,y=0): #x = left, right | y= up, down
        match x:
            case 'left':
                x = -48
            case 'right':
                x = 48

        match y:
            case 'up':
                y = -48
            case 'down':
                y = 48
        rect = pygame.Rect(jgdr1.get_coorx()+x, jgdr1.get_coory()+y, 48,48)
        return rect
    #endregion RECTS

    run = True
    while run:
        charect = pygame.Rect(jgdr1.get_coorx(),jgdr1.get_coory(),48,48)
        #region EVENTOS
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                
                run = False

            #region MOVIMENTO
            if event.type == pygame.KEYDOWN:

                jgdr1.mover(event.key)

                # if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    
                #     if jgdr1.get_coorx() + 48 >= 590:
                #         pass
                        

                #     else:
                #         jgdr1.get_coorx() += 48
                #     if olhando == "Esquerda":
                #             knight = pygame.transform.flip(knight, True, False)
                #             olhando = "Direita"
                        
                # if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    
                #     if jgdr1.get_coorx() - 48 <= 110:
                #         pass

                #     else:
                #         jgdr1.get_coorx() -= 48
                #     if olhando == "Direita":
                #             knight = pygame.transform.flip(knight, True, False)
                #             olhando = "Esquerda"
                        

                # if event.key == pygame.K_w or event.key == pygame.K_UP:
                #     if jgdr1.get_coory() - 48 <= 110:
                #         pass

                #     else:
                #         jgdr1.get_coory() -= 48
                # if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                #     if jgdr1.get_coory() + 48 >= 590:
                #         pass

                #     else:
                #         jgdr1.get_coory() += 48
            #endregion MOVIMENTO

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

        

        for a in range(0,len(cordwall)):
            for b in range(-1,2):
                tela.blit(barreira,(cordwall[a][0]+48*b, cordwall[a][1]))
                tela.blit(barreira,(cordwall[a][0], cordwall[a][1]+48*b))
            
            

        tela.blit(grid,(112,112))

        tela.blit(jgdr1.get_img(),charect)
        tela.blit(princesa,prinrect)
        
        
    
        pygame.display.flip()
        clock.tick(30) #Diminuindo os fps para otimizar o jogo
    pygame.quit()
    
if __name__ == '__main__':
    jogar()

