import pygame
from random import randint, getrandbits
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

#region CAVALEIRO
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

    class player():

        def __init__(self, coorx, coory, vida):
            self.__img = pygame.transform.scale(pygame.image.load('imagens/Knight.png'), (48,48))
            self.__olhando = True
            self.__coorx = coorx
            self.__coory = coory
            self.__vida = vida
        
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

        def set_vida(self,vida):
            self.__vida = vida
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
                if self.__olhando == False:
                        self.__img = pygame.transform.flip(self.__img, True, False)
                        self.__olhando = True
                if self.__coorx + 48 >= 590:
                    pass
                elif any(nextrect(x='right').colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                    pass
                else:
                    self.__coorx += dist
                    
            if key == pygame.K_a or key == pygame.K_LEFT:
                if self.__olhando == True:
                        self.__img = pygame.transform.flip(self.__img, True, False)
                        self.__olhando = False
                if self.__coorx - 48 <= 110:
                    pass
                elif any(nextrect(x='left').colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                    pass
                else:
                    self.__coorx -= dist
                    
            if key == pygame.K_w or key == pygame.K_UP:
                if self.__coory - 48 < 110:
                    pass
                elif any(nextrect(y='up').colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                        pass
                else:
                    self.__coory -= dist
            if key == pygame.K_s or key == pygame.K_DOWN:
                if self.__coory + 48 >= 590:
                    pass
                elif any(nextrect(y='down').colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
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

    bomba = pygame.image.load('imagens/Princesa.png')
    bomba = pygame.transform.scale(princesa,(48,48))

    icone = pygame.transform.scale_by(icone,2)
    #endregion CARREGANDO IMAGENS

    #region PRINCESA

    prinx = 112 + 48*randint(0,9)
    priny = 112 + 48*randint(0,9)

    jgdr1 = player(112 + 48*randint(0,9), 112 + 48*randint(0,9),vida=3)
    
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
        
    qntwall = 3
    
    rectwall = []
    
    for a in range(0,qntwall):
        x = 112 + 48*randint(0,9)
        y = 112 + 48*randint(0,9)

        rectotal = Paredes(x,y).rect()

        #podia fazer isso do while dentro da classe paredes 
        #mas ciro não deixou usar variável global então vai assim mesmo
        while any(rectotal[b].colliderect(condicoes[a])for b in range(0,5)for a in range(0,len(condicoes))): #or any(rectotal[1].colliderect(condicoes[a])for a in range(0,len(condicoes))):
            x = 112 + 48*randint(0,9)
            y = 112 + 48*randint(0,9)

            rectotal = Paredes(x,y).rect()
            
        rectwall.append(rectotal)
        
#endregion PAREDES
    
#region IMAGENS INFO
    fonte = pygame.font.SysFont('fonte/PixelGameFont.ttf',20)
    fonte2 = pygame.font.SysFont('fonte/PixelGameFont.ttf',30)

    wasd = pygame.image.load('imagens/wasd.png')
    wasd = pygame.transform.scale_by(wasd,4)

    setinhas = pygame.image.load('imagens/setinhas.png')
    setinhas = pygame.transform.scale_by(setinhas,4)

    espaco = pygame.image.load('imagens/espaco.png')
    espaco = pygame.transform.scale_by(espaco,3)

    espaco2 = pygame.image.load('imagens/espaco2.png')
    espaco2 = pygame.transform.scale_by(espaco2,3)
#endregion IMAGENS INFO

    frames = 60
    info = True

    while info:
        tela.blit(fonte.render('TODAS AS POSIÇÕES DE PERSONAGENS, BARREIRAS E MONSTROS SÃO GERADAS ALEATORIAMENTE',False,'white'),(8,8))
    
        tela.blit(fonte2.render('PRESSIONE QUALQUER TECLA PARA INICIAR',False,'white'),(120,260))
        tela.blit(wasd,(420,300))
        tela.blit(setinhas,(100,300))
        tela.blit(espaco,(270, 440))
        tela.blit(fonte2.render('= BOMBA',False,'white'),(440,460))
        tela.blit(espaco2,(270, 520))
        tela.blit(fonte2.render('= KABOOM',False,'white'),(440,540))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                info = False

        pygame.display.flip()
        clock.tick(frames)
   
    #endregion RECTS

    ganhou = False
    perdeu = False
    run = True
    decapitado = False

    bombanatela = False
    explosao = False
    exdelay = 0
    while run:
        
        vida = jgdr1.get_vida()
        
        charect = pygame.Rect(jgdr1.get_coorx(),jgdr1.get_coory(),48,48)
        #region EVENTOS
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
           
            if event.type == pygame.KEYDOWN:

                jgdr1.mover(event.key)

                if event.key == pygame.K_SPACE:
                    if not bombanatela and exdelay == 0:
                        bombanatela = True
                        posbomba = (charect.x, charect.y)
                    else:
                        explosaox = pygame.Rect(posbomba[0]-48,posbomba[1],48*3,48)
                        explosaoy = pygame.Rect(posbomba[0],posbomba[1]-48,48,48*3)
                        exrects = [explosaox,explosaoy]
                        bombanatela = False
                        explosao = True
                
        #endregion EVENTOS
        if charect.colliderect(prinrect):
            run = False
            ganhou = True

        if vida == 0:
            run = False
            perdeu = True

        tela.fill('gray')

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

        for a in range(0,jgdr1.get_vida()):
            rectheart = pygame.Rect(8+20*a,8,20,20)
            pygame.draw.rect(tela,'red',rectheart,border_radius=1,width=1)
        
        #tela.blit(grid,(112,112))

        tela.blit(jgdr1.get_img(),charect)
        tela.blit(princesa,prinrect)

        if bombanatela:
            
            tela.blit(bomba,(posbomba))
        elif explosao:
            
            for a in range(0,2):
                pygame.draw.rect(tela,'yellow',exrects[a])
                if exrects[a].colliderect(prinrect):       
                    decapitado = True
                    run = False

                elif exrects[a].colliderect(charect) and exdelay == 0:
                    jgdr1.set_vida(vida-1)
                    
            new_wall_rect = []
            for parede in range(0,len(rectwall)):
                new_wall_rect.append(rectwall[parede])
                for square in rectwall[parede]:
                    for a in range(0,2):
                        
                        if exrects[a].colliderect(square):
                            new_wall_rect[parede].remove(square)
                        
            rectwall = new_wall_rect
                        
            exdelay += 1/frames

            if exdelay >= 1:
                
                explosao = False
                exdelay = 0
                
        pygame.display.flip() #atualizar os frames a cada vez que roda o while
        clock.tick(frames) #Diminuindo os fps para otimizar o jogo
    
    while ganhou:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.fill('black')
        tela.blit(icone,(320,230))
        tela.blit(fonte2.render('Parabéns! Você salvou a princesa',False,'white'),(190,300))

        pygame.display.flip()
        clock.tick(frames)
    icone = pygame.transform.rotate(icone,65)
    while decapitado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tela.fill('black')
        tela.blit(icone,(305,220))
        tela.blit(fonte2.render('Você assassinou a princesa e foi decapitado',False,'red'),(150,300))

        pygame.display.flip()
        clock.tick(frames)
    
    icone = pygame.transform.grayscale(icone)
    while perdeu:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tela.fill('black')
        
        tela.blit(icone,(305,220))
        tela.blit(fonte2.render('A princesa foi capturada pelos monstros :C',False,'gray'),(140,300))

        pygame.display.flip()
        clock.tick(frames)
    
if __name__ == '__main__':
    jogar()