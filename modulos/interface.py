import pygame

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
