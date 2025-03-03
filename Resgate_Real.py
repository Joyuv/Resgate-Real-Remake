import pygame
from random import randint
import os
import sys
import json

# importa todos os módulos dentro do container (interface, logica, rank)
from modulos import * 

# LEMBRAR DE TIRAR OS CHEATS NA VERSÃO FINAL

#region CARREGANDO IMAGENS   
icone = pygame.image.load('./imagens/Icon.png')

knight = pygame.image.load('./imagens/gameplay/Knight.png')
knight = pygame.transform.scale(knight, (48,48))

princesa_img = pygame.image.load('./imagens/gameplay/Princesa.png')
princesa_img = pygame.transform.scale(princesa_img,(48,48))

grama = pygame.image.load('./imagens/gameplay/Grama.png')
grama = pygame.transform.scale(grama,(48,48))

barreira_img = pygame.image.load('./imagens/gameplay/Preda.png')
barreira_img = pygame.transform.scale(barreira_img,(48,48))

bomba = pygame.image.load('./imagens/gameplay/Bomba.png')
bomba = pygame.transform.scale(bomba,(48,48))
excentro = pygame.image.load('./imagens/gameplay/Excentro.png')
exlados = pygame.image.load('./imagens/gameplay/Exlados.png')

tenis = pygame.image.load('./imagens/gameplay/Tenis.png')
tenis = pygame.transform.scale_by(tenis,3)
heart = pygame.image.load('./imagens/gameplay/Heart.png')
heart = pygame.transform.scale_by(heart,3)

imajenladron = pygame.transform.scale(pygame.image.load('./imagens/gameplay/Ladrao.png'), (48,48))
icone = pygame.transform.scale_by(icone,2)

wasd = pygame.image.load('./imagens/info/wasd.png')
wasd = pygame.transform.scale_by(wasd,4)

setinhas = pygame.image.load('./imagens/info/setinhas.png')
setinhas = pygame.transform.scale_by(setinhas,4)

espaco = pygame.image.load('./imagens/info/espaco.png')
espaco = pygame.transform.scale_by(espaco,3)

espaco2 = pygame.image.load('./imagens/info/espaco2.png')
espaco2 = pygame.transform.scale_by(espaco2,3)

sangueimg = [
    pygame.transform.scale(pygame.image.load('./imagens/gameplay/Sangue_01.png'),(48,48)),
    pygame.transform.scale(pygame.image.load('./imagens/gameplay/Sangue_02.png'),(48,48))
    ]

lkey = pygame.image.load('./imagens/L.png')
lkey = pygame.transform.scale_by(lkey,4)

rkey = pygame.image.load('./imagens/R.png')
rkey = pygame.transform.scale_by(rkey,4)
#endregion CARREGANDO IMAGENS

def jogar():
    '''Função que inicializa o jogo e a interface gráfica'''

    #region PREPARAÇÃO DO AMBIENTE
    if not os.path.exists('ranking.json'):
        jason = open('ranking.json','w')
        jason.write(
        """{ 

    }""")
        jason.close()

    pygame.init() #iniciando o módulo pygame
    
    fonte = pygame.font.SysFont('./fonte/PixelGameFont.ttf', 20)
    fonte2 = pygame.font.SysFont('./fonte/PixelGameFont.ttf', 30)
    

    tela = pygame.display.set_mode((700,700)) #setando resolução da tela
    pygame.display.set_caption('Resgate Real') #nome da janela
    pygame.display.set_icon(icone) #icone da janela
    
    clock = pygame.time.Clock() #variável clock para diminuir os FPS em breve

    #endregion PREPARAÇÃO DO AMBIENTE

    #region PRINCESA
    while True:
        aux = 112 + 48*randint(0,9)

        princesa = Entidade(aux, 112 + 48*randint(0,9), princesa_img)

        aux = 112 + 48*randint(0,9)

        player = Player(aux, 112 + 48*randint(0,9), vida=4, stamina=20, img=knight)
        
        while princesa.x == player.x:
            random = randint(0,1)
            if random == 0:
                princesa.y = 112 + 48*randint(0,9)
            else:
                princesa.x = 112 + 48*randint(0,9)

        while princesa.y == player.y:
            random = randint(0,1)
            if random == 0:
                princesa.y = 112 + 48*randint(0,9)
            else:
                princesa.x = 112 + 48*randint(0,9)
        
        CONDICOES = [player.get_rect(),princesa.get_rect()]
        #endregion PRINCESA

        #region PAREDES
        
        QNT_WALL = 5
        barreiras:list[Barreira] = []
        
        for i in range(0, QNT_WALL):
            barreira = Barreira(barreira_img)
            
            while any(barreira.get_rect()[rect].colliderect(CONDICOES[condicao])for rect in range(0,5) for condicao in range(0, len(CONDICOES))): #or any(barreira[1].colliderect(condicoes[a])for a in range(0,len(condicoes))):
                barreira.new_rect()
                
            barreiras.append(barreira)

        QNT_LADRAO = 4

        listaladroes: list[Ladrao]
        listaladroes = []
        for a in range(0, QNT_LADRAO):
            x = 112+48*randint(0,9)
            y = 112+48*randint(0,9)
            ladrao = Ladrao(x,y,imajenladron)
            thiefrect = ladrao.get_rect()

            while any(thiefrect.colliderect(barreiras[b].get_rect()[c])for b in range(0,QNT_WALL) for c in range(0,5)) or any(thiefrect.colliderect(CONDICOES[condicao]) for condicao in range(0,len(CONDICOES))):
                x = 112+48*randint(0,9)
                y = 112+48*randint(0,9)
                
                ladrao = Ladrao(x,y, imajenladron)
                thiefrect = ladrao.get_rect()

            listaladroes.append(ladrao)

        #endregion PAREDES
        
        #region IMAGENS INFO
        
        #endregion IMAGENS INFO

        frames = 60
        info = True
        telanome = True

        run = True

        ganhou = False
        perdeu = False
        decapitado = False
        listaTelas = [ganhou, perdeu, decapitado]

        leader = False

        vida_inicial = player.vida
        
        vigor_inicial = player.stamina

        #region TELA INFO
        PRESSINICIARTXT = fonte2.render('PRESSIONE QUALQUER TECLA PARA INICIAR',False,'yellow')
        OBJETIVOTXT = fonte2.render('Você é o cavaleiro e o seu objetivo é salvar a princesa',False,'white')
        while info:
            sprite_leaderboard(tela,fonte2,lkey)
            tela.fill('black')
            tela.blit(fonte.render('TODAS AS POSIÇÕES DE PERSONAGENS, BARREIRAS E MONSTROS SÃO GERADAS ALEATORIAMENTE',False,'red'),(8,680))
            
            
            tela.blit(PRESSINICIARTXT,(tela.get_width()/2-PRESSINICIARTXT.get_width()/2,130))

            tela.blit(wasd,(420,170))
            tela.blit(setinhas,(100,170))

            tela.blit(espaco,(100, 310))
            tela.blit(fonte2.render('POSICIONA A BOMBA',False,'white'),(270,335))
            tela.blit(bomba, (500, 315))

            tela.blit(espaco2,(100, 390))
            tela.blit(fonte2.render('EXPLODE A BOMBA',False,'white'),(270,415))

            cordBombaInfo = [530, 410]
            tela.blit(excentro,(cordBombaInfo[0], cordBombaInfo[1])) #centro
            flipVertInfo = pygame.transform.flip(exlados,False,True)
            tela.blit(flipVertInfo,(cordBombaInfo[0], cordBombaInfo[1]+48))
            flipHorInfo = pygame.transform.rotate(exlados,-90)
            tela.blit(flipHorInfo,(cordBombaInfo[0]+48, cordBombaInfo[1])) #direita
            tela.blit(exlados,(cordBombaInfo[0], cordBombaInfo[1]-48)) #cima
            flipHorInfo = pygame.transform.rotate(exlados,90)
            tela.blit(flipHorInfo,(cordBombaInfo[0]-48, cordBombaInfo[1])) #esquerda
            
            tela.blit(fonte2.render("A bomba pode explodir inimigos e pedras",False,"orange"),(100, 470))
            tela.blit(fonte2.render("MAS TAMBÉM PODE EXPLODIR VOCÊ E A PRINCESA!!!",False,"red"),(100, 500))

            print_hp(tela, player, fonte, vida_inicial, 100, 550,heart)
            tela.blit(fonte2.render('Pontos de vida',False,'red'),(335,550))

            print_vigor(tela, player, fonte, vigor_inicial, 100, 580,tenis)
            tela.blit(fonte2.render('Quantidade de passos restantes',False,'cyan'),(335,580))

            tela.blit(OBJETIVOTXT,(tela.get_width()/2 - OBJETIVOTXT.get_width()/2,630))
            tela.blit(knight, (30,620))
            tela.blit(princesa_img,(670-princesa_img.get_width(), 620))
            

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
                    elif (event.key == pygame.K_KP_ENTER or event.key == 13) and len(name): #13 é o código da tecla enter
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

        #region TELA GAME

        
        pontos = 0

        sanguelist: list[Entidade]
        sanguelist = []

        killEnemy = 0
        danoTomado = 0
        breakWall = 0

        while run:
            #region EVENTOS
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.KEYDOWN and not explosao and all(listaTelas[a] == False for a in range(len(listaTelas))):
                    
                    #region Cheats
                    if event.key == pygame.K_j:
                        player.stamina = 1000000
                        vigor_inicial = 1000000
                    if event.key == pygame.K_v:
                        player.vida = 1000000
                        vida_inicial = 1000000
                    #endregion Cheats

                    if event.key == pygame.K_r:
                        ganhou = False
                        perdeu = False
                        decapitado = False
                        leader = False
                        run = False

                    if player.mover(event.key, barreiras):
                        for thief in listaladroes:
                            thief.andar(player.x, player.y, listaladroes, barreiras, princesa.get_rect())

                    if event.key == pygame.K_SPACE:
                        if not bombanatela and exdelay == 0:
                            bombanatela = True
                            posbomba = (player.x, player.y)
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
            
            if player.get_rect().colliderect(princesa.get_rect()):
                run = False
                ganhou = True
                pontos += 1500
                break
                
            elif player.vida <= 0 or player.stamina <= 0:
                run = False
                perdeu = True
                break
            
            
            
            tela.fill('black')

            for a in range(0,10):
                for b in range(0,10):
                    tela.blit(grama,(112+48*a,112+48*b))
                    pygame.draw.rect(tela,'black', (pygame.Rect(112+48*a,112+48*b,48,48)),width=1,border_radius= 4)
                
            
            for a in range(0,12):
                tela.blit(barreira_img, (64+48*a,64))
                tela.blit(barreira_img, (64+48*a,592))
                tela.blit(barreira_img, (592,64+48*a))
                tela.blit(barreira_img, (64,64+48*a))

            for bar in barreiras:
                # print(bar.get_rect())
                # print(range(0,len(bar.get_rect())))
                
                for b in range(0, len(bar.get_rect())):
                    tela.blit(bar.img, bar.get_rect()[b])
                
                    
            for a in range(0,10):
                for b in range(0,10):
                    pygame.draw.rect(tela,'black', (pygame.Rect(112+48*a,112+48*b,48,48)),width=1)

            tela.blit(fonte2.render('Score:'+str(int(pontos)),0,'white'),(590,8))

            print_hp(tela, player, fonte, vida_inicial,15,15,heart)
            
            print_vigor(tela,player,fonte,vigor_inicial,15,35,tenis)
        
            for sangue in sanguelist:
                tela.blit(sangue.img, sangue.get_rect())

            tela.blit(player.img, player.get_rect())
            tela.blit(princesa.img, princesa.get_rect())
            
            for thief in listaladroes:
                tela.blit(thief.img, thief.get_rect())
                if thief.get_rect().colliderect(player.get_rect()):
                    player.vida =  player.vida - 1
                    listaladroes.remove(thief)

                    aux_sangue = random_blood_sprite(sangueimg)
                    sanguelist.append(Entidade(player.x, player.y, aux_sangue))
                    pontos -= 250

                    danoTomado += 250
            

            if bombanatela:
                tela.blit(bomba, posbomba)
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

                    if exrects[a].colliderect(princesa.get_rect()):      
                        run = False 
                        decapitado = True
                        break

                    elif exrects[a].colliderect(player.get_rect()) and tomou == False:
                        player.vida = player.vida - 1
                        sanguelist.append(Entidade(player.x, player.y, random_blood_sprite(sangueimg)))
                        tomou = True
                        pontos -= 250
                        danoTomado += 250
                    for thief in listaladroes:
                        if thief.get_rect().colliderect(exrects[a]):
                            listaladroes.remove(thief)
                            pontos += 500
                            killEnemy += 500

                new_barreiras:list[Barreira] = []
                for parede in range(0,len(barreiras)):
                    new_barreiras.append(barreiras[parede])
                    for square in barreiras[parede].get_rect():
                        for a in range(0,5):
                            
                            if exrects[a].colliderect(square):
                                new_barreiras[parede].get_rect().remove(square)
                                pontos += 250
                                breakWall += 250
                            
                barreiras = new_barreiras
                            
                exdelay += 1/frames

                if exdelay >= 1:
                    
                    explosao = False
                    exdelay = 0
                    tomou = False
            tela.set_colorkey("blue")
            pygame.display.flip() #atualizar os frames a cada vez que roda o while
            clock.tick(frames) #Diminuindo os fps para não usar tanto o processador
        #endregion TELA GAME
        #region TELAS FINAIS
        if ganhou:
            newpontos = int((pontos)+pontos/2 * player.vida + pontos * (player.stamina/10))
            # print(pontos)
            # print(newpontos)

            with open('ranking.json','r') as filer:
                davyjsones = json.load(filer)
            
            alphanames = get_alphalist(davyjsones)

            namelist = get_ocorrencias(name,davyjsones)
            # print(alphanames)
            # print(namelist)

            name = formatname(name,alphanames,namelist)

            # print(name)

            addranking(name,newpontos,davyjsones)

        while ganhou:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        leader = True
                        ganhou = False
                    if event.key == pygame.K_r:
                        ganhou = False
                        run = False
                        decapitado = False
                        perdeu = False
                        leader = False

            tela.fill('black')
            tela.blit(icone,(320,230))
            tela.blit(fonte2.render('Parabéns! Você salvou a princesa',False,'cyan'),(190,300))
            score = fonte2.render('Score:'+str(newpontos),False,'white')
            tela.blit(score,((tela.get_width()/2)-score.get_width()/2,(tela.get_height()/2)-20))
            sprite_leaderboard(tela,fonte2,lkey)
            sprite_restart(tela,fonte2,rkey)

            

            stats = fonte2.render("Estatísticas", False, "white")
            tela.blit(stats,(tela.get_width()/2-stats.get_width()/2, 400))

            rVida = fonte2.render(('Vida restante: '+str(player.vida)),False,'cyan')
            tela.blit(rVida,(tela.get_width()/2-rVida.get_width()/2,440))
            rStamina = fonte2.render(('Stamina restante: '+str(player.stamina)),False,'cyan')
            tela.blit(rStamina,(tela.get_width()/2-rStamina.get_width()/2,460))

            pPrincesa = fonte2.render('Pontuação por salvar a princesa: 1500',False,'white')
            tela.blit(pPrincesa,(tela.get_width()/2-pPrincesa.get_width()/2,500))
            pKill = fonte2.render(('Pontuação por derrotar ladrões: '+str(killEnemy)),False,'white')
            tela.blit(pKill,(tela.get_width()/2-pKill.get_width()/2,520))
            pPedra = fonte2.render(('Pontuação por explodir pedras: '+str(breakWall)),False,'white')
            tela.blit(pPedra,(tela.get_width()/2-pPedra.get_width()/2,540))
            pPerdidos = fonte2.render('Pontos perdidos por tomar dano: '+str(danoTomado),False,'red')
            tela.blit(pPerdidos,(tela.get_width()/2-pPerdidos.get_width()/2,560))
            
            bVida = fonte2.render(('Bônus de pontos por quantidade de vida: '+str(int(pontos/2*player.vida))),False,'yellow')
            tela.blit(bVida,(tela.get_width()/2-bVida.get_width()/2,600))
            bStamina = fonte2.render(('Bônus de pontos por quantidade de stamina: '+str(int(pontos * player.stamina/10))),False,'yellow')
            tela.blit(bStamina,(tela.get_width()/2-bStamina.get_width()/2,620))
            
        
            pygame.draw.rect(tela, 'white', (10,
                                             400+stats.get_height()/2,
                                             tela.get_width()/2-stats.get_width()/2 -15,
                                             3
                                             ),border_radius=3)
            pygame.draw.rect(tela, 'white', (tela.get_width()/2+stats.get_width()/2+ 5,
                                             400+stats.get_height()/2,
                                             tela.get_width()/2-stats.get_width()/2 -15,
                                             3
                                             ),border_radius=3)
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
                    if event.key == pygame.K_r:
                        ganhou = False
                        perdeu = False
                        decapitado = False
                        leader = False
                        run = False
            tela.fill('black')
            tela.blit(iconerotate,(305,220))
            tela.blit(fonte2.render('Você assassinou a princesa e foi decapitado',False,'red'),(150,300))
            sprite_leaderboard(tela,fonte2,lkey)
            sprite_restart(tela,fonte2,rkey)

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
                    if event.key == pygame.K_r:
                        ganhou = False
                        perdeu = False
                        run = False
                        decapitado = False
                        leader = False
                

            tela.fill('black')
            
            tela.blit(iconegray,(305,220))
            tela.blit(fonte2.render('A princesa foi capturada pelos criminosos :C',False,'gray'),(140,300))
            sprite_leaderboard(tela,fonte2,lkey)
            sprite_restart(tela,fonte2,rkey)
            
            pygame.display.flip()
            clock.tick(frames)

        
        with open('ranking.json','r') as filer:
            davyjsones = json.load(filer)
        rankordenado = get_rankdecrescente(davyjsones)
        while leader:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        ganhou = False
                        perdeu = False
                        decapitado = False
                        run = False
                        leader = False

            
            tela.fill('black')

            sprite_restart(tela,fonte2,rkey)
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
