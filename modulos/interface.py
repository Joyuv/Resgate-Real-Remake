import pygame
from modulos.logica import Player

def sprite_leaderboard(tela:pygame.Surface, fonte:pygame.font.Font, img:pygame.Surface) -> None:
    '''Função para renderizar na tela a imagem da tecla L junto com a palavra leaderboard

    Não há nada de complexo nessa função, ela só coloca as informações na tela mesmo. Fizemos essa função
    porque isso aparece em todas as telas de derrota,  de vitória e também na tela inicial, então fica mais fácil caso
    queiramos alterar algo.

    - Parâmetros:
        - tela: É a tela onde serão renderizados os sprites
        - fonte: Fonte que será utilizada no texto
        - img: Imagem da tecla L
    '''
    tela.blit(img,(490, 16))
    tela.blit(fonte.render('LeaderBoard',False, 'cyan'),(560,32))

def sprite_restart(tela:pygame.Surface, fonte:pygame.font.Font, img:pygame.Surface):
    tela.blit(img,(16, 16))
    tela.blit(fonte.render('Restart',False, 'white'),(86,32))

def print_hp(tela: pygame.Surface, player: Player, fonte: pygame.font, vida_inicial: int, x:int, y: int, img: pygame.Surface) -> None:
    '''Função para exibir a barra de vida do player
    
    '''
    tela.blit(img, (x,y-5))
    linhavida = pygame.Rect(x+30,y,200,15)
    pygame.draw.rect(tela,'red',linhavida,border_radius=10,width=1)
    vida = player.get_vida() / vida_inicial
    barravida = pygame.Rect(x+30,y,200*vida,15)
    pygame.draw.rect(tela,'#A70505',barravida,border_radius=10)
    barravida.height = 10
    pygame.draw.rect(tela,'#CD0C0C',barravida,border_radius=10)
    tela.blit(fonte.render(str(player.get_vida()),False,'white'),(x+27+100*vida,y))

def print_vigor(tela: pygame.Surface, player: Player, fonte: pygame.font, vigor_inicial: int, x:int, y: int, img:pygame.Surface):
    '''Função para exibir a barra de stamina do player
    
    '''
    tela.blit(img, (x+3,y-5))
    linhavigor = pygame.Rect(x+30,y,200,15)
    pygame.draw.rect(tela,'cyan',linhavigor,border_radius=10,width=1)
    vigor = player.get_stamina() / vigor_inicial
    barravigor = pygame.Rect(x+30,y,200*vigor,15)
    pygame.draw.rect(tela,'#00D6D0',barravigor,border_radius=10)
    barravigor.height = 10
    pygame.draw.rect(tela,'cyan',barravigor,border_radius=10)
    tela.blit(fonte.render(str(player.get_stamina()),False,'black'),(x+27+100*vigor,y))