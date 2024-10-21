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

def print_hp(tela: pygame.Surface, player: Player, fonte: pygame.font, vida_inicial: int, x:int, y: int) -> None:
    '''Função para exibir a barra de vida do player
    
    '''
    linhavida = pygame.Rect(x,y,200,15)
    pygame.draw.rect(tela,'red',linhavida,border_radius=10,width=1)
    vida = player.get_vida() / vida_inicial
    barravida = pygame.Rect(x,y,200*vida,15)
    pygame.draw.rect(tela,'#A70505',barravida,border_radius=10)
    barravida.height = 10
    pygame.draw.rect(tela,'#CD0C0C',barravida,border_radius=10)
    tela.blit(fonte.render(str(player.get_vida()),False,'white'),(x-3+100*vida,y))