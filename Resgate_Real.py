import pygame
from random import randint, getrandbits
import os
import sys
import json
import rank
import logica

if not os.path.exists('ranking.json'):
    jason = open('ranking.json','w')
    jason.write(
    """{ 

}""")
    jason.close()

#parei na linha 725

# coisas que planejamos adicionar: 
# 1º Item coletável que você deixa guardado, quando escolher usar aparece uma tela com duas opções, curar stamina ou vida
# 2º Sistema de pontos
# 3º Tela com o nome dos que mais pontuaram

def sprite_leaderboard(tela:pygame.Surface, fonte:pygame.font.Font, img:pygame.Surface):
    tela.blit(img,(490, 16))
    tela.blit(fonte.render('LeaderBoard',False, 'cyan'),(560,32))


def jogar():
    #region PREPARAÇÃO DO AMBIENTE
    pygame.init() #iniciando o módulo pygame
     
    icone = pygame.image.load('imagens/Icon.png')

    tela = pygame.display.set_mode((700,700)) #setando resolução da tela
    pygame.display.set_caption('Resgate Real') #nome da janela
    pygame.display.set_icon(icone) #icone da janela
    
    clock = pygame.time.Clock() #variável clock para diminuir os FPS em breve

    #endregion PREPARAÇÃO DO AMBIENTE

    #region CAVALEIRO
    

    class Player:
        """Classe para checar e manipular os atributos do personagem"""
        def __init__(self, coorx:int, coory:int, vida:int, stamina:int, img:pygame.Surface):
            
            self.__img = img
            self.__olhando = bool(getrandbits(1))
            self.__img = pygame.transform.flip(self.__img,self.__olhando,False)

            self.__coorx = coorx
            self.__coory = coory
            self.__vida = vida
            self.__stamina = stamina

        def get_coorx(self):
            return self.__coorx
        def get_coory(self):
            return self.__coory
        def get_olhando(self):
            return self.__olhando
        def get_img(self):
            return self.__img
        def get_vida(self):
            return self.__vida
        def get_stamina(self):
            return self.__stamina

        
        def set_vida(self,vida:int):
            self.__vida = vida
        def set_stamina(self,stamina:int):
            self.__stamina = stamina

        def mover(self, key:int):
            dist = 48
            if key == pygame.K_d or key == pygame.K_RIGHT:
                if self.__olhando == True:
                        self.__img = pygame.transform.flip(self.__img, True, False)
                        self.__olhando = False
                if self.__coorx + 48 >= 590:
                    pass
                elif any(nextrect(self,x=48).colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                    pass
                else:
                    self.__coorx += dist
                    self.__stamina -= 1
                    return True
                    
            if key == pygame.K_a or key == pygame.K_LEFT:
                if self.__olhando == False:
                        self.__img = pygame.transform.flip(self.__img, True, False)
                        self.__olhando = True
                if self.__coorx - 48 <= 110:
                    pass
                elif any(nextrect(self,x=-48).colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                    pass
                else:
                    self.__coorx -= dist
                    self.__stamina -= 1
                    return True
            if key == pygame.K_w or key == pygame.K_UP:
                if self.__coory - 48 < 110:
                    pass
                elif any(nextrect(self,y=-48).colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                        pass
                else:
                    self.__coory -= dist
                    self.__stamina -= 1
                    return True
            if key == pygame.K_s or key == pygame.K_DOWN:
                if self.__coory + 48 >= 590:
                    pass
                elif any(nextrect(self,y= 48).colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                    pass
                else:
                    self.__coory += dist
                    self.__stamina -= 1
                    return True
    #endregion CAVALEIRO
    #region Ladrões
    class Ladroes:
        def __init__(self,coorx:int, coory:int, img:pygame.Surface):
            
            self.__img = img
            self.__olhando = bool(getrandbits(1))
            self.__img = pygame.transform.flip(self.__img,self.__olhando,False)

            self.__coorx = coorx
            self.__coory = coory
        
        def get_coorx(self):
            return self.__coorx
        def get_coory(self):
            return self.__coory
        def get_img(self):
            return self.__img
        def get_olhando(self):
            return self.__olhando
        def get_rect(self):
            return pygame.Rect(self.__coorx,self.__coory,48,48)
        
        def horizontal(self, charx:int, chary:int):
            if self.__coorx != charx:
                #region Tentando LEFT
                if self.__coorx > charx:#andando pra esquerda(-48)
                    if 'left' in self.__vaicolidir:
                        if self.__coory > chary: 
                            if 'up' in self.__vaicolidir:
                                if 'down' in self.__vaicolidir:
                                    if 'right' in self.__vaicolidir:
                                        pass
                                    else: #direita (+48)
                                        self.__coorx += 48
                                        if self.__olhando == True:
                                            self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), False
                                else: #desce (+48)
                                    self.__coory += 48
                            else: #sobe (-48)
                                self.__coory -= 48
                        else:
                            if 'down' in self.__vaicolidir:
                                if 'up' in self.__vaicolidir:
                                    if 'right' in self.__vaicolidir:
                                        pass
                                    else: #direita (+48)
                                        self.__coorx += 48
                                        if self.__olhando == True:
                                            self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), False
                                else: #sobe (-48)
                                    self.__coory -= 48
                            else: self.__coory += 48 #desce (+48) 
                    else: #Esquerda (-48)
                        self.__coorx -=48
                        if self.__olhando == False:
                            self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), True 
                #endregion Tentando LEFT

                #region Tentando RIGHT
                elif self.__coorx < charx:
                    if 'right' in self.__vaicolidir:
                        if self.__coory > chary: 
                            if 'up' in self.__vaicolidir:
                                if 'down' in self.__vaicolidir:
                                    if 'left' in self.__vaicolidir:
                                        pass
                                    else: #esquerda (-48)
                                        self.__coorx -= 48
                                        if self.__olhando == False:
                                            self.__img = pygame.transform.flip(self.__img,True,False)
                                            self.__olhando = True
                                else: #desce (+48)
                                    self.__coory += 48

                            else: #sobe (-48)
                                self.__coory -= 48
                        else:

                            if 'down' in self.__vaicolidir:
                                if 'up' in self.__vaicolidir:
                                    if 'left' in self.__vaicolidir:
                                        pass
                                    else: #esquerda (-48)
                                        self.__coorx -= 48
                                        if self.__olhando == False:
                                            self.__img = pygame.transform.flip(self.__img,True,False)
                                            self.__olhando = True
                                else: #sobe (-48)
                                    self.__coory -= 48

                            else: #desce (+48)
                                self.__coory += 48
                            
                            
                    
                    else: #Direita (-48)
                        self.__coorx +=48
                        if self.__olhando == True:
                            self.__img = pygame.transform.flip(self.__img,True,False)
                            self.__olhando = False
                #endregion Tentando Right
        def vertical(self, charx:int, chary:int):
            if self.__coory != chary:
                #region Tentando UP
                if self.__coory > chary:#andando pra cima(-48)
                    if 'up' in self.__vaicolidir:
                        if self.__coorx > charx: 
                            if 'right' in self.__vaicolidir:
                                if 'left' in self.__vaicolidir:
                                    if 'down' in self.__vaicolidir:
                                        pass
                                    else: #baixo (+48)
                                        self.__coory += 48
                                        
                                else: #esquerda (-48)
                                    self.__coorx -= 48
                                    if self.__olhando == False:
                                        self.__img = pygame.transform.flip(self.__img,True,False)
                                        self.__olhando = True

                            else: #direita (+48)
                                self.__coorx += 48
                                if self.__olhando == True:
                                    self.__img = pygame.transform.flip(self.__img,True,False)
                                    self.__olhando = False
                        else:

                            if 'left' in self.__vaicolidir:
                                if 'right' in self.__vaicolidir:
                                    if 'down' in self.__vaicolidir:
                                        pass
                                    else: #desce (+48)
                                        self.__coory += 48
                                else: #direita (+48)
                                    self.__coorx += 48
                                    if self.__olhando == True:
                                        self.__img = pygame.transform.flip(self.__img,True,False)
                                        self.__olhando = False

                            else: #esquerda (-48)
                                self.__coorx -= 48
                                if self.__olhando == False:
                                        self.__img = pygame.transform.flip(self.__img,True,False)
                                        self.__olhando = True
                            
                            
                    
                    else: #cima (-48)
                        self.__coory -=48

                #endregion Tentando UP

                #region Tentando DOWN
                elif self.__coory < chary:#andando pra baixo(+48)
                    if 'down' in self.__vaicolidir:
                        if self.__coorx > charx: 
                            if 'right' in self.__vaicolidir:
                                if 'left' in self.__vaicolidir:
                                    if 'up' in self.__vaicolidir:
                                        pass
                                    else: #cima (-48)
                                        self.__coory -= 48
                                        
                                else: #esquerda (-48)
                                    self.__coorx -= 48
                                    if self.__olhando == False:
                                        self.__img = pygame.transform.flip(self.__img,True,False)
                                        self.__olhando = True

                            else: #direita (+48)
                                self.__coorx += 48
                                if self.__olhando == True:
                                    self.__img = pygame.transform.flip(self.__img,True,False)
                                    self.__olhando = False
                        else:

                            if 'left' in self.__vaicolidir:
                                if 'right' in self.__vaicolidir:
                                    if 'up' in self.__vaicolidir:
                                        pass
                                    else: #sobe (-48)
                                        self.__coory -= 48
                                else: #direita (+48)
                                    self.__coorx += 48
                                    if self.__olhando == True:
                                        self.__img = pygame.transform.flip(self.__img,True,False)
                                        self.__olhando = False

                            else: #esquerda (-48)
                                self.__coorx -= 48
                                if self.__olhando == False:
                                        self.__img = pygame.transform.flip(self.__img,True,False)
                                        self.__olhando = True
                            
                            
                    
                    else: #baixo (+48)
                        self.__coory +=48
                #endregion Tentando DOWN
        def andar(self,charx:int, chary:int, thiefs:list):
            self.__vaicolidir = []
            
            if any(nextrect(self,x=48).colliderect(barreira[a]) for barreira in rectwall for a in range(0,len(barreira))) or any(nextrect(self,x=48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
                self.__vaicolidir.append('right')
            if any(nextrect(self,x=-48).colliderect(barreira[a]) for barreira in rectwall for a in range(0,len(barreira))) or any(nextrect(self,x=-48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
                self.__vaicolidir.append('left')
            if any(nextrect(self,y=-48).colliderect(barreira[a]) for barreira in rectwall for a in range(0,len(barreira))) or any(nextrect(self,y=-48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
                self.__vaicolidir.append('up')
            if any(nextrect(self,y=48).colliderect(barreira[a]) for barreira in rectwall for a in range(0,len(barreira))) or any(nextrect(self,y=48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
                self.__vaicolidir.append('down')

            if self.__coorx +48 >= 590 or nextrect(self,x=48).colliderect(prinrect):
                self.__vaicolidir.append('right')
            if self.__coorx -48 <= 110  or nextrect(self,x=-48).colliderect(prinrect):
                self.__vaicolidir.append('left')
            if self.__coory -48 <= 110  or nextrect(self,y=-48).colliderect(prinrect):
                self.__vaicolidir.append('up')
            if self.__coory +48 >= 590  or nextrect(self,y=48).colliderect(prinrect):
                self.__vaicolidir.append('down')
            
            if 'right' in self.__vaicolidir and 'left' in self.__vaicolidir and 'down' in self.__vaicolidir and 'up' in self.__vaicolidir:
                pass
            else:
                
                if self.__coorx != charx and self.__coory != chary:
                    self.__random = bool(getrandbits(1))
                    if self.__random:
                        self.horizontal(charx,chary)
                    else:
                        self.vertical(charx,chary)

                elif self.__coorx != charx and not self.__coory != chary:
                    self.horizontal(charx,chary)
                elif self.__coory != chary and not self.__coorx != charx:
                    self.vertical(charx,chary)
        
    #endregion Ladrões

    def nextrect(objeto:Player | Ladroes, x:int = 0, y:int = 0) -> pygame.Rect: #x = -48 ou 0 ou 48 | y = -48 ou 0 ou 48 
        """Função para retornar o rect que o personagem terá depois de andar, utilizado para chegar futuras colisões"""

        rect = pygame.Rect(objeto.get_coorx()+x, objeto.get_coory()+y, 48,48)
        return rect
    
    #region CARREGANDO IMAGENS   
    knight = pygame.image.load('imagens/gameplay/Knight.png')
    knight = pygame.transform.scale(knight, (48,48))

    princesa = pygame.image.load('imagens/gameplay/Princesa.png')
    princesa = pygame.transform.scale(princesa,(48,48))

    grama = pygame.image.load('imagens/gameplay/Grama.png')
    grama = pygame.transform.scale(grama,(48,48))

    barreira = pygame.image.load('imagens/gameplay/Preda.png')
    barreira = pygame.transform.scale(barreira,(48,48))

    bomba = pygame.image.load('imagens/gameplay/Bomba.png')
    bomba = pygame.transform.scale(bomba,(48,48))
    excentro = pygame.image.load('imagens/gameplay/Excentro.png')
    exlados = pygame.image.load('imagens/gameplay/Exlados.png')
    
    imajenladron = pygame.transform.scale(pygame.image.load('imagens/gameplay/Ladrao.png'), (48,48))
    icone = pygame.transform.scale_by(icone,2)

    sangueimg = [
        pygame.transform.scale(pygame.image.load('imagens/gameplay/Sangue_01.png'),(48,48)),
        pygame.transform.scale(pygame.image.load('imagens/gameplay/Sangue_02.png'),(48,48))
        ]

    lkey = pygame.image.load('imagens/L.png')
    lkey = pygame.transform.scale_by(lkey,4)

    #endregion CARREGANDO IMAGENS

    #region PRINCESA

    prinx = 112 + 48*randint(0,9)
    priny = 112 + 48*randint(0,9)

    jgdr1 = Player(112 + 48*randint(0,9), 112 + 48*randint(0,9),vida=4,stamina=20,img=knight)
    
    charect = pygame.Rect(jgdr1.get_coorx(),jgdr1.get_coory(),48,48)

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

    condicoes = [charect,prinrect]
    #endregion PRINCESA

    #region PAREDES
    class Paredes:
        
        def __init__(self, x, y):
            self.x = x
            self.y = y
            
        def rect(self):
            self.listarect = []
            self.rect0 = pygame.Rect(self.x,self.y,48, 48)
            self.listarect.append(self.rect0)

            for a in range(-1,2,2):
                self.rect1 = pygame.Rect(self.x-48*a,self.y,48, 48)
                self.rect2 = pygame.Rect(self.x,self.y-48*a,48,48)
        
                self.listarect.append(self.rect1)
                self.listarect.append(self.rect2)
     
            return self.listarect
    
    qntwall = 5
    
    rectwall = []
    
    for a in range(0,qntwall):
        x = 112 + 48*randint(0,9)
        y = 112 + 48*randint(0,9)

        rectotal = Paredes(x,y).rect()

        while any(rectotal[b].colliderect(condicoes[a])for b in range(0,5)for a in range(0,len(condicoes))): #or any(rectotal[1].colliderect(condicoes[a])for a in range(0,len(condicoes))):
            x = 112 + 48*randint(0,9)
            y = 112 + 48*randint(0,9)

            rectotal = Paredes(x,y).rect()
            
        rectwall.append(rectotal)

    ladraoqnt = 4
    listaladroes = []
    for a in range(0,ladraoqnt):
        x = 112+48*randint(0,9)
        y = 112+48*randint(0,9)
        ladrao = Ladroes(x,y,imajenladron)
        rect = ladrao.get_rect()

        while any(rect.colliderect(rectwall[b][c])for b in range(0,qntwall) for c in range(0,5)) or any(rect.colliderect(condicoes[d]) for d in range(0,2)):
            x = 112+48*randint(0,9)
            y = 112+48*randint(0,9)
            ladrao = Ladroes(x,y, imajenladron)
            rect = ladrao.get_rect()

        listaladroes.append(ladrao)

    #endregion PAREDES
    
    #region IMAGENS INFO
    fonte = pygame.font.SysFont('fonte/PixelGameFont.ttf',20)
    fonte2 = pygame.font.SysFont('fonte/PixelGameFont.ttf',30)

    wasd = pygame.image.load('imagens/info/wasd.png')
    wasd = pygame.transform.scale_by(wasd,4)

    setinhas = pygame.image.load('imagens/info/setinhas.png')
    setinhas = pygame.transform.scale_by(setinhas,4)

    espaco = pygame.image.load('imagens/info/espaco.png')
    espaco = pygame.transform.scale_by(espaco,3)

    espaco2 = pygame.image.load('imagens/info/espaco2.png')
    espaco2 = pygame.transform.scale_by(espaco2,3)
    #endregion IMAGENS INFO

    frames = 60

    info = True
    telanome = True
    run = True
    ganhou = False
    perdeu = False
    decapitado = False
    leader = False

    #region TELA INFO
    while info:
        tela.blit(fonte.render('TODAS AS POSIÇÕES DE PERSONAGENS, BARREIRAS E MONSTROS SÃO GERADAS ALEATORIAMENTE',False,'red'),(8,688))
    
        tela.blit(fonte2.render('PRESSIONE QUALQUER TECLA PARA INICIAR',False,'white'),(120,260))
        tela.blit(wasd,(420,300))
        tela.blit(setinhas,(100,300))
        tela.blit(espaco,(270, 440))
        tela.blit(fonte2.render('= BOMBA',False,'white'),(440,460))
        tela.blit(espaco2,(270, 520))
        tela.blit(fonte2.render('= KABOOM',False,'white'),(440,540))
        sprite_leaderboard(tela,fonte2,lkey)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    leader = True
                    run = False
                    telanome = False
                info = False

        pygame.display.flip()
        clock.tick(frames)
    #endregion TELA INFO
    
    alfabeto = tuple('abcdefghijklmnopqrstuvwxyz')
    name = ''
    while telanome:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                
                if pygame.key.name(event.key) in alfabeto and not len(name)+1 == 5:
                    name += pygame.key.name(event.key)
                elif event.key == pygame.K_KP_ENTER or event.key == 13: #13 é o código da tecla enter
                    telanome = False
                    break
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                
        tela.fill('black')
        textonick = fonte2.render('Digite seu nick e pressione enter',False,'white')
        tela.blit(textonick,(tela.get_width()/2-textonick.get_width()/2,tela.get_height()/2-25))
        
        rectgrande = pygame.Rect(tela.get_width()/2-125, tela.get_height()/2, 250, 70)

        rect1 = pygame.Rect(rectgrande.x+10,rectgrande.y+10,50,50)
        rect2 = pygame.Rect(rectgrande.x+70,rectgrande.y+10,50,50)
        rect3 = pygame.Rect(rectgrande.x+130,rectgrande.y+10,50,50)
        rect4 = pygame.Rect(rectgrande.x+190,rectgrande.y+10,50,50)

        rects = [rect1,rect2,rect3,rect4]
        # pygame.draw.rect(tela,'white',rectgrande)

        pygame.draw.rect(tela,'gray',(rect1.x-3,rect1.y-3,53,53))
        pygame.draw.rect(tela,'gray',(rect2.x-3,rect2.y-3,53,53))
        pygame.draw.rect(tela,'gray',(rect3.x-3,rect3.y-3,53,53))
        pygame.draw.rect(tela,'gray',(rect4.x-3,rect4.y-3,53,53))
        
        for rect in rects:
            pygame.draw.rect(tela,'white',rect)
        
        for letra in range(0,len(name)):
            match letra:
                case 0:
                    tela.blit(fonte2.render(name[0],False,'black'),(rect1.x+18, rect1.y+13))
                case 1:
                    tela.blit(fonte2.render(name[1],False,'black'),(rect2.x+18, rect2.y+13))
                case 2:
                    tela.blit(fonte2.render(name[2],False,'black'),(rect3.x+18, rect3.y+13))
                case 3:
                    tela.blit(fonte2.render(name[3],False,'black'),(rect4.x+18, rect4.y+13))

        
        pygame.display.flip()
        clock.tick(frames)



    bombanatela = False
    explosao = False
    tomou = False
    exdelay = 0

    vida_inicial = jgdr1.get_vida()
    
    vigorinicial = jgdr1.get_stamina()
    
    charect = pygame.Rect(jgdr1.get_coorx(),jgdr1.get_coory(),48,48)
    #region TELA GAME

    
    pontos = 0
    sanguelist = []
    while run:
        #region EVENTOS
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:
                    jgdr1.set_stamina(1000000)
                    vigorinicial = 1000000
                if event.key == pygame.K_v:
                    jgdr1.set_vida(1000000)
                    vida_inicial = 1000000

                if jgdr1.mover(event.key):
                    for thief in listaladroes:
                        thief.andar(jgdr1.get_coorx(), jgdr1.get_coory(),listaladroes)

                if event.key == pygame.K_SPACE:
                    if not bombanatela and exdelay == 0:
                        bombanatela = True
                        posbomba = (charect.x, charect.y)
                    else:
                        exrects = [pygame.Rect(posbomba[0],posbomba[1],48,48)]
                        for a in range(-1,2,2):
                            recty = pygame.Rect(posbomba[0],posbomba[1]-48*a,48,48)
                            rectx = pygame.Rect(posbomba[0]-48*a,posbomba[1],48,48)
                            
                            exrects.append(recty)
                            exrects.append(rectx)
                        
                        
                        bombanatela = False
                        explosao = True
        #endregion EVENTOS
        charect = pygame.Rect(jgdr1.get_coorx(),jgdr1.get_coory(),48,48)
        
        if charect.colliderect(prinrect):
            run = False
            ganhou = True
            pontos += 1000
            break
            
        elif jgdr1.get_vida() <= 0 or jgdr1.get_stamina() <= 0:
            run = False
            perdeu = True
            break
            
        
        
        tela.fill('black')

        for a in range(0,10):
            for b in range(0,10):
                tela.blit(grama,(112+48*a,112+48*b))
                pygame.draw.rect(tela,'black', (pygame.Rect(112+48*a,112+48*b,48,48)),width=1,border_radius= 4)
            
        
        for a in range(0,12):
            tela.blit(barreira,(64+48*a,64))
            tela.blit(barreira,(64+48*a,592))
            tela.blit(barreira,(592,64+48*a))
            tela.blit(barreira,(64,64+48*a))

        for a in range(0,len(rectwall)):
            for b in range(0,len(rectwall[a])):
                tela.blit(barreira,rectwall[a][b])
                
        for a in range(0,10):
            for b in range(0,10):
                pygame.draw.rect(tela,'black', (pygame.Rect(112+48*a,112+48*b,48,48)),width=1)
        
        tela.blit(fonte2.render('Score:'+str(pontos),0,'white'),(590,8))

        linhavida = pygame.Rect(15,15,200,15)
        pygame.draw.rect(tela,'red',linhavida,border_radius=10,width=1)
        vida = jgdr1.get_vida() / vida_inicial
        barravida = pygame.Rect(15,15,200*vida,15)
        pygame.draw.rect(tela,'#A70505',barravida,border_radius=10)
        barravida.height = 10
        pygame.draw.rect(tela,'#CD0C0C',barravida,border_radius=10)
        tela.blit(fonte.render(str(jgdr1.get_vida()),False,'white'),(12+100*vida,15))
        
        linhavigor = pygame.Rect(15,35,200,15)
        pygame.draw.rect(tela,'cyan',linhavigor,border_radius=10,width=1)
        vigor = jgdr1.get_stamina() / vigorinicial
        barravigor = pygame.Rect(15,35,200*vigor,15)
        pygame.draw.rect(tela,'#00D6D0',barravigor,border_radius=10)
        barravigor.height = 10
        pygame.draw.rect(tela,'cyan',barravigor,border_radius=10)
        tela.blit(fonte.render(str(jgdr1.get_stamina()),False,'black'),(12+100*vigor,35))
        
        for sangue in sanguelist:
            tela.blit(sangue.get_img(),sangue.get_pos())

        tela.blit(jgdr1.get_img(),charect)
        tela.blit(princesa,prinrect)
        
        for thief in listaladroes:
            tela.blit(thief.get_img(),thief.get_rect())
            if thief.get_rect().colliderect(charect):
                jgdr1.set_vida(jgdr1.get_vida()-1)
                listaladroes.remove(thief)
                sanguelist.append(logica.Sangue(jgdr1.get_coorx(), jgdr1.get_coory(), sangueimg))
                pontos -= 250
        

        if bombanatela:
            tela.blit(bomba,(posbomba))
        elif explosao:
            
            for a in range(0,5):

                match a:
                    case 0:
                        tela.blit(excentro,exrects[0])
                    case 1:
                        flipvert = pygame.transform.flip(exlados,False,True)
                        tela.blit(flipvert,(exrects[a]))
                    case 2:
                        fliphor = pygame.transform.rotate(exlados,-90)
                        tela.blit(fliphor,(exrects[a]))
                    case 3:
                        tela.blit(exlados,(exrects[a]))
                    case 4:
                        fliphor =pygame.transform.rotate(exlados,90)
                        tela.blit(fliphor,(exrects[a]))

                if exrects[a].colliderect(prinrect):      
                    run = False 
                    decapitado = True
                    break

                elif exrects[a].colliderect(charect) and tomou == False:
                    jgdr1.set_vida(jgdr1.get_vida()-1)
                    sanguelist.append(logica.Sangue(jgdr1.get_coorx(), jgdr1.get_coory(), sangueimg))
                    tomou = True
                    pontos -= 250
                for thief in listaladroes:
                    if thief.get_rect().colliderect(exrects[a]):
                        listaladroes.remove(thief)
                        pontos += 500

            new_wall_rect = []
            for parede in range(0,len(rectwall)):
                new_wall_rect.append(rectwall[parede])
                for square in rectwall[parede]:
                    for a in range(0,5):
                        
                        if exrects[a].colliderect(square):
                            new_wall_rect[parede].remove(square)
                            pontos += 100
                        
            rectwall = new_wall_rect
                        
            exdelay += 1/frames

            if exdelay >= 1:
                
                explosao = False
                exdelay = 0
                tomou = False
                
        pygame.display.flip() #atualizar os frames a cada vez que roda o while
        clock.tick(frames) #Diminuindo os fps para não usar tanto o processador
    #endregion TELA GAME
    #region TELAS FINAIS
    if ganhou:
        newpontos = int((pontos * jgdr1.get_vida()) + pontos * (jgdr1.get_stamina()/10))
        # print(pontos)
        # print(newpontos)

        with open('ranking.json','r') as filer:
            davyjsones = json.load(filer)
        
        alphanames = rank.get_alphalist(davyjsones)

        namelist = rank.get_ocorrencias(name,davyjsones)
        # print(alphanames)
        # print(namelist)

        name = rank.formatname(name,alphanames,namelist)

        # print(name)

        rank.addranking(name,newpontos,davyjsones)

    while ganhou:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    leader = True
                    ganhou = False

        tela.fill('black')
        tela.blit(icone,(320,230))
        tela.blit(fonte2.render('Parabéns! Você salvou a princesa',False,'cyan'),(190,300))
        score = fonte2.render('Score:'+str(newpontos),False,'white')
        tela.blit(score,((tela.get_width()/2)-score.get_width()/2,(tela.get_height()/2)-20))
        sprite_leaderboard(tela,fonte2,lkey)
        
        pygame.display.flip()
        clock.tick(frames)
    if perdeu or decapitado:
        iconerotate = pygame.transform.rotate(icone,65)
    while decapitado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    leader = True
                    decapitado = False
        tela.fill('black')
        tela.blit(iconerotate,(305,220))
        tela.blit(fonte2.render('Você assassinou a princesa e foi decapitado',False,'red'),(150,300))
        sprite_leaderboard(tela,fonte2,lkey)

        pygame.display.flip()
        clock.tick(frames)
    if perdeu:
        iconegray = pygame.transform.grayscale(iconerotate)
    while perdeu:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    leader = True
                    perdeu = False
            

        tela.fill('black')
        
        tela.blit(iconegray,(305,220))
        tela.blit(fonte2.render('A princesa foi capturada pelos criminosos :C',False,'gray'),(140,300))
        sprite_leaderboard(tela,fonte2,lkey)
        
        pygame.display.flip()
        clock.tick(frames)

    
    with open('ranking.json','r') as filer:
        davyjsones = json.load(filer)
    rankordenado = rank.get_rankdecrescente(davyjsones)
    while leader:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill('black')
        leadertxt = fonte2.render('~~~~~~~LEADERBOARD~~~~~~~',False,'yellow')
        tela.blit(leadertxt,(tela.get_width()/2-(leadertxt.get_width()/2),180))
        tela.blit(leadertxt,(tela.get_width()/2-(leadertxt.get_width()/2),500))
        tela.blit(icone,(tela.get_width()/2-(icone.get_width()/2),120))
        
        for a in range(0,len(rankordenado['jogadores'])):
            tela.blit(fonte2.render(f'{a+1}° '+rankordenado['jogadores'][a]+':'+rankordenado['pontos'][a],False,'cyan'),(tela.get_width()/2-(140/2),200+25*(a+1)))
        
        pygame.display.flip()
        clock.tick(frames)

    #endregion TELASFINAIS
    
if __name__ == '__main__':
    jogar()