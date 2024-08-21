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
    

    class player():
        """Classe para checar e manipular os atributos do personagem"""
        def __init__(self, coorx:int, coory:int, vida:int, stamina:int):
            
            self.__img = pygame.transform.scale(pygame.image.load('imagens/gameplay/Knight.png'), (48,48))
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

        def mover(self, key):
            dist = 48
            if key == pygame.K_d or key == pygame.K_RIGHT:
                if self.__olhando == True:
                        self.__img = pygame.transform.flip(self.__img, True, False)
                        self.__olhando = False
                if self.__coorx + 48 >= 590:
                    pass
                elif any(nextrect(jgdr1,x=48).colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
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
                elif any(nextrect(jgdr1,x=-48).colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                    pass
                else:
                    self.__coorx -= dist
                    self.__stamina -= 1
                    return True
            if key == pygame.K_w or key == pygame.K_UP:
                if self.__coory - 48 < 110:
                    pass
                elif any(nextrect(jgdr1,y=-48).colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                        pass
                else:
                    self.__coory -= dist
                    self.__stamina -= 1
                    return True
            if key == pygame.K_s or key == pygame.K_DOWN:
                if self.__coory + 48 >= 590:
                    pass
                elif any(nextrect(jgdr1,y= 48).colliderect(rectwall[a][b])for a in range(0,len(rectwall)) for b in range(0,len(rectwall[a]))):
                    pass
                else:
                    self.__coory += dist
                    self.__stamina -= 1
                    return True
    class Ladroes:
        def __init__(self,coorx:int, coory:int):
            self.__img = pygame.transform.scale(pygame.image.load('imagens/gameplay/Ladrao.png'), (48,48))
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
        

        def andar(self,charx, chary):
            
            if self.__coorx != charx and self.__coory != chary:
                
                self.random = bool(getrandbits(1))
                if self.random:
                    if self.__coorx < charx:
                        self.__coorx += 48
                        if self.__olhando == True:
                            self.__img = pygame.transform.flip(self.__img,True,False)
                            self.__olhando = False
                    elif self.__coorx > charx:
                        self.__coorx -= 48
                        if self.__olhando == False:
                            self.__img = pygame.transform.flip(self.__img,True,False)
                            self.__olhando = True

                else:
                    if self.__coory < chary:
                        self.__coory += 48
                    elif self.__coory > chary:
                        self.__coory -= 48
            
            elif self.__coorx != charx:
                if self.__coorx < charx:
                    self.__coorx += 48
                    if self.__olhando == True:
                            self.__olhando = False
                            self.__img = pygame.transform.flip(self.__img,True,False)
                elif self.__coorx > charx:
                    self.__coorx -= 48
                    if self.__olhando == False:
                            self.__olhando = True
                            self.__img = pygame.transform.flip(self.__img,True,False)

            elif self.__coory != chary:
                if self.__coory < chary :
                    self.__coory += 48
                elif self.__coory > chary:
                    self.__coory -= 48

    def nextrect(objeto:player | Ladroes, x:int = 0, y:int = 0): #x = -48 ou 0 ou 48 | y = -48 ou 0 ou 48 
        #obs para givanilson, objeto é o bicho, por exemplo, o jgdr1 ou algum dos ladrões, se vira aí na tipagem
        
        #outra coisa, eu acho que tem como colocar a tipagem pra ser uma tupla que tu escolhe um dos valores, por exemplo (-48,0,48) descobre aí como faz
        """Função para retornar o rect do personagem depois de andar"""

        rect = pygame.Rect(objeto.get_coorx()+x, objeto.get_coory()+y, 48,48)
        return rect



#endregion
    
#region CARREGANDO IMAGENS   

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
    
    
    icone = pygame.transform.scale_by(icone,2)
    #endregion CARREGANDO IMAGENS

    #region PRINCESA

    prinx = 112 + 48*randint(0,9)
    priny = 112 + 48*randint(0,9)

    jgdr1 = player(112 + 48*randint(0,9), 112 + 48*randint(0,9),vida=4,stamina=20)
    
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

    ladraoqnt = 5
    listaladroes = []
    for a in range(0,ladraoqnt):
        x = 112+48*randint(0,9)
        y = 112+48*randint(0,9)
        ladrao = Ladroes(x,y)
        rect = ladrao.get_rect()

        while any(rect.colliderect(rectwall[b][c])for b in range(0,qntwall) for c in range(0,5)) or any(rect.colliderect(condicoes[d]) for d in range(0,2)):
            x = 112+48*randint(0,9)
            y = 112+48*randint(0,9)
            ladrao = Ladroes(x,y)
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
    tomou = False
    exdelay = 0

    vida_inicial = jgdr1.get_vida()
    
    vigorinicial = jgdr1.get_stamina()
    
    charect = pygame.Rect(jgdr1.get_coorx(),jgdr1.get_coory(),48,48)
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
                        thief.andar(jgdr1.get_coorx(), jgdr1.get_coory())

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
                
        charect = pygame.Rect(jgdr1.get_coorx(),jgdr1.get_coory(),48,48)
        #endregion EVENTOS
        if charect.colliderect(prinrect):
            run = False
            ganhou = True
            
            

        elif jgdr1.get_vida() <= 0 or jgdr1.get_stamina() <= 0:
            run = False
            perdeu = True
            
        

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
        
        tela.blit(jgdr1.get_img(),charect)
        tela.blit(princesa,prinrect)
        
        for thief in listaladroes:
            tela.blit(thief.get_img(),thief.get_rect())
            if thief.get_rect().colliderect(charect):
                jgdr1.set_vida(jgdr1.get_vida()-1)
                listaladroes.remove(thief)
        

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
                    decapitado = True
                    run = False

                elif exrects[a].colliderect(charect) and tomou == False:
                    jgdr1.set_vida(jgdr1.get_vida()-1)
                    tomou = True
                for thief in listaladroes:
                    if thief.get_rect().colliderect(exrects[a]):
                        listaladroes.remove(thief)

            new_wall_rect = []
            for parede in range(0,len(rectwall)):
                new_wall_rect.append(rectwall[parede])
                for square in rectwall[parede]:
                    for a in range(0,5):
                        
                        if exrects[a].colliderect(square):
                            new_wall_rect[parede].remove(square)
                        
            rectwall = new_wall_rect
                        
            exdelay += 1/frames

            if exdelay >= 1:
                
                explosao = False
                exdelay = 0
                tomou = False
                
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