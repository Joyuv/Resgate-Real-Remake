import pygame
from random import randint, getrandbits

from abc import ABC, abstractmethod

class Entidade(ABC):
    def __init__(self, x: int, y: int, img: pygame.Surface):        
        self.__x = x
        self.__y = y
        self.__img = img

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x: int):
        if type(x) == int:
            self.__x = x
        else:
            print('ERRO NA ENTIDADE: X não é inteiro')

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y: int):
        if type(y) == int:
            self.__y = y
        else:
            print("ERRO NA ENTIDADE: Y não é inteiro")

    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, img: pygame.Surface):
        if type(img) == pygame.Surface:
            self.__img = img
        else:
            print('ERRO NA ENTIDADE: A imagem não é uma Surface')

    def get_rect(self):
        return pygame.Rect(self.__x, self.y, 48, 48)

class Barreira(Entidade):
    '''Classe para criar as paredes que ficam no mapa para atrapalhar o jogador.

    - Parâmetros:
        - x: Coordenada X que a parede ficará.
        - y: Coordenada Y que a parede ficará.
    '''
    def __init__(self, img:pygame.Surface, x:int = -1, y:int = -1) -> None:
        super().__init__(x, y, img)

        self.__listarect = []
        self.new_rect()
        
    def get_rect(self) -> list[pygame.Rect]:
        return self.__listarect

    def new_rect(self) -> list[pygame.Rect]:
        '''Cria os rect das paredes com posições aleatórias.

        Cada parede inteira tem 5 rects, que é o de cada quadrado que faz parte dela, assim ela pode
        ser quebrada pela bomba.
        '''
        self.__listarect = []

        x = 112 + 48*randint(0,9)
        y = 112 + 48*randint(0,9)
        self.x = x
        self.y = y

        self.__listarect.append(pygame.Rect(self.x, self.y, 48, 48)) #rect central

        for multiplier in range(-1,2,2):
            self.__listarect.append(pygame.Rect(self.x-48*multiplier, self.y, 48, 48))
            self.__listarect.append(pygame.Rect(self.x, self.y-48*multiplier, 48, 48))

class Player(Entidade):
    '''Classe para checar e manipular os atributos do personagem.
    
    - Parâmetros:
        - x: É a coordenada X do personagem na tela.
        - y: É a coordenada Y do personagem na tela.
        - vida: Quantidade de vida que o jogador terá.
        - stamina: Quantidade de stamina que o jogador terá.
        - img: Sprite do personagem.
    '''
    def __init__(self, x:int, y:int, img:pygame.Surface, vida:int, stamina:int):
        super().__init__(x, y, img)

        self.__flipado = bool(getrandbits(1))
        self.img = pygame.transform.flip(self.img, self.__flipado, False)

        self.__vida = vida
        self.__stamina = stamina

    @property
    def vida(self):
        return self.__vida
    @vida.setter
    def vida(self, quantidade: int):
        if quantidade < 0:
            quantidade = 0
        self.__vida = quantidade

    @property
    def stamina(self):
        return self.__stamina
    @stamina.setter
    def stamina(self, quantidade: int):
        if quantidade < 0:
            quantidade = 0
        self.__stamina = quantidade


    def mover(self, key:int, paredes:list[Barreira]):
        '''Função que move o personagem.

        Checa a tecla que foi pressionada, se essa tecla estiver entre as teclas que movem o personagem
        então soma ou subtrai 48 pixeis na coordenada e retira 1 de stamina.

        - Parâmetros:
            - key: A tecla pressionada.
            - paredes: A lista com os rect das barreiras.
        - Retorna:
            Um valor booleano que dá partida ao movimento do ladrão.
        '''
        DISTANCIA = 48
        if key == pygame.K_d or key == pygame.K_RIGHT:
            if self.__flipado == True:
                    self.img = pygame.transform.flip(self.img, True, False)
                    self.__flipado = False
            if self.x + 48 >= 590:
                pass
            elif any(nextrect(self,x=48).colliderect(paredes[a].get_rect()[b])for a in range(0, len(paredes)) for b in range(0,len(paredes[a].get_rect()))): 
                pass
            else:
                self.x = self.x + DISTANCIA
                self.__stamina =  self.__stamina - 1

                return True
        if key == pygame.K_a or key == pygame.K_LEFT:
            if self.__flipado == False:
                    self.img = pygame.transform.flip(self.img, True, False)
                    self.__flipado = True
            if self.x - 48 <= 110: 
                pass
            elif any(nextrect(self,x=-48).colliderect(paredes[a].get_rect()[b])for a in range(0, len(paredes)) for b in range(0,len(paredes[a].get_rect()))): 
                pass
            else: 
                self.x = self.x - DISTANCIA
                self.__stamina = self.__stamina - 1
                
                return True
        if key == pygame.K_w or key == pygame.K_UP:
            if self.y - 48 < 110: pass
            elif any(nextrect(self,y=-48).colliderect(paredes[a].get_rect()[b])for a in range(0, len(paredes)) for b in range(0,len(paredes[a].get_rect()))): 
                pass
            else: 
                self.y = self.y - DISTANCIA
                self.__stamina =  self.__stamina - 1

                return True
        if key == pygame.K_s or key == pygame.K_DOWN:
            if self.y + 48 >= 590:
                pass
            elif any(nextrect(self,y= 48).colliderect(paredes[a].get_rect()[b])for a in range(0, len(paredes)) for b in range(0,len(paredes[a].get_rect()))):
                pass
            else:
                self.y += DISTANCIA
                self.__stamina -= 1

                return True
class Ladrao(Entidade):
    '''Classe para checar e manipular atributos dos ladrões.
    
    - Parâmetros:
        - x: Coordenada X do ladrão.
        - y: Coordenada Y do ladrão.
        - img: Sprite do ladrão.
    '''
    def __init__(self, x:int, y:int, img:pygame.Surface) -> None:
        super().__init__(x, y, img)

        self.__flipado = bool(getrandbits(1))
        self.img = pygame.transform.flip(self.img, self.__flipado, False)
    
    def get_rect(self) -> pygame.Rect:
        '''Pega o rect do ladrão.

        - Retorna:
            O rect do ladrão.
        '''
        return pygame.Rect(self.x, self.y, 48, 48)
    
    def h_left(self, chary: int):
        '''Parte do movimento horizontal do ladrão.

        - Parâmetro:
            - chary: A coordenada Y do cavaleiro.
        '''
        if 'left' in self.__vaicolidir:
            if self.y > chary: 
                if 'up' in self.__vaicolidir:
                    if 'down' in self.__vaicolidir:
                        if 'right' in self.__vaicolidir: pass
                        else: #direita (+48)
                            self.x += 48
                            if self.__flipado == True:
                                self.img, self.__flipado = pygame.transform.flip(self.img,True,False), False
                    else: self.y += 48 #desce (+48)
                else: self.y -= 48 #sobe (-48)
            else:
                if 'down' in self.__vaicolidir:
                    if 'up' in self.__vaicolidir:
                        if 'right' in self.__vaicolidir: pass
                        else: #direita (+48)
                            self.x += 48
                            if self.__flipado == True:
                                self.img, self.__flipado = pygame.transform.flip(self.img,True,False), False
                    else: self.y -= 48 #sobe (-48)
                else: self.y += 48 #desce (+48)                    
        else: #Esquerda (-48)
            self.x -=48
            if self.__flipado == False:
                self.img, self.__flipado = pygame.transform.flip(self.img,True,False), True
    def h_right(self, chary: int):
        '''Parte do movimento horizontal do ladrão.

        - Parâmetro:
            - chary: A coordenada Y do cavaleiro.
        '''
        if 'right' in self.__vaicolidir:
            if self.y > chary: 
                if 'up' in self.__vaicolidir:
                    if 'down' in self.__vaicolidir:
                        if 'left' in self.__vaicolidir: pass
                        else: #esquerda (-48)
                            self.x -= 48
                            if self.__flipado == False:
                                self.img, self.__flipado = pygame.transform.flip(self.img,True,False), True
                    else: self.y += 48 #desce (+48)
                else: self.y -= 48 #sobe (-48)                       
            else:
                if 'down' in self.__vaicolidir:
                    if 'up' in self.__vaicolidir:
                        if 'left' in self.__vaicolidir: pass
                        else: #esquerda (-48)
                            self.x -= 48
                            if self.__flipado == False:
                                self.img, self.__flipado = pygame.transform.flip(self.img,True,False), True
                    else: self.y -= 48 #sobe (-48)
                else: self.y += 48 #desce (+48)
        else: #Direita (-48)
            self.x +=48
            if self.__flipado == True:
                self.img, self.__flipado = pygame.transform.flip(self.img,True,False), False
    def v_up(self, charx: int):
        '''Parte do movimento vertical do ladrão.

        - Parâmetro:
            - charx: A coordenada X do cavaleiro.
        '''
        if 'up' in self.__vaicolidir:
            if self.x > charx: 
                if 'right' in self.__vaicolidir:
                    if 'left' in self.__vaicolidir:
                        if 'down' in self.__vaicolidir: pass
                        else: self.y += 48 #baixo (+48)
                    else: #esquerda (-48)
                        self.x -= 48
                        if self.__flipado == False:
                            self.img, self.__flipado = pygame.transform.flip(self.img,True,False), True
                else: #direita (+48)
                    self.x += 48
                    if self.__flipado == True:
                        self.img, self.__flipado = pygame.transform.flip(self.img,True,False), False     
            else:
                if 'left' in self.__vaicolidir:
                    if 'right' in self.__vaicolidir:
                        if 'down' in self.__vaicolidir: pass
                        else: self.y += 48 #desce (+48)
                    else: #direita (+48)
                        self.x += 48
                        if self.__flipado == True:
                            self.img, self.__flipado = pygame.transform.flip(self.img,True,False), False
                else: #esquerda (-48)
                    self.x -= 48
                    if self.__flipado == False:
                        self.img, self.__flipado = pygame.transform.flip(self.img,True,False), True
        else: self.y -=48 #cima (-48)
    def v_down(self, charx: int):
        '''Parte do movimento vertical do ladrão.

        - Parâmetro:
            - charx: A coordenada X do cavaleiro.
        '''
        if 'down' in self.__vaicolidir:
            if self.x > charx: 
                if 'right' in self.__vaicolidir:
                    if 'left' in self.__vaicolidir:
                        if 'up' in self.__vaicolidir: pass
                        else: self.y -= 48 #cima (-48)
                    else: #esquerda (-48)
                        self.x -= 48
                        if self.__flipado == False:
                            self.img, self.__flipado = pygame.transform.flip(self.img,True,False), True
                else: #direita (+48)
                    self.x += 48
                    if self.__flipado == True:
                        self.img, self.__flipado = pygame.transform.flip(self.img,True,False), False
            else:
                if 'left' in self.__vaicolidir:
                    if 'right' in self.__vaicolidir:
                        if 'up' in self.__vaicolidir: pass
                        else: self.y -= 48 #sobe (-48)                                      
                    else: #direita (+48)
                        self.x += 48
                        if self.__flipado == True:
                            self.img, self.__flipado = pygame.transform.flip(self.img,True,False), False                                       
                else: #esquerda (-48)
                    self.x -= 48
                    if self.__flipado == False:
                            self.img, self.__flipado = pygame.transform.flip(self.img,True,False), True                                                                                 
        else: self.y +=48 #baixo (+48)
    def horizontal(self, charx:int, chary:int):
        '''Função que junta os movimentos horizontais.
        
        Checa se o X do ladrão é diferente do X do cavaleiro, se for, 
        então checa se é mais favorável pro ladrão andar para a esquerda ou para a direita.

        - Parâmetros:
            - charx: Coordenada X do cavaleiro.
            - chary: Coordenada Y do cavaleiro.
        '''
        if self.x != charx:
            if self.x > charx:#andando pra esquerda(-48)
                self.h_left(chary)
            elif self.x < charx:
                self.h_right(chary)
    def vertical(self, charx:int, chary:int):
        '''Função que junta os movimentos verticais.
        
        Checa se o Y do ladrão é diferente do Y do cavaleiro, se for, 
        então checa se é mais favorável pro ladrão andar para cima ou para baixo.

        - Parâmetros:
            - charx: Coordenada X do cavaleiro.
            - chary: Coordenada Y do cavaleiro.
        '''
        if self.y != chary:
            if self.y > chary:#andando pra cima(-48)
                self.v_up(charx)
            elif self.y < chary:#andando pra baixo(+48)
                self.v_down(charx)
    def andar(self,charx:int, chary:int, thiefs:list, paredes:list[Barreira], princesa:pygame.Rect) -> None:
        '''Função que move o ladrão, 
        
        Se utiliza de uma variável chamada "vaicolidir" que é uma lista das direções que o ladrão 
        não pode andar, excluindo as direções que ele não pode andar podemos evitar 
        com que ele acabe dentro de uma parede.
        
        - Parâmetros:
            - charx: Coordenada X do cavaleiro.
            - chary: Coordenada Y do cavaleiro.
            - thiefs: Lista dos outros ladrões.
            - paredes: Lista dos rect das paredes.
            - princesa: Rect da princesa.
        '''
        self.__vaicolidir = []

        if any(nextrect(self,x=48).colliderect(barreira.get_rect()[a]) for barreira in paredes for a in range(0,len(barreira.get_rect()))) or any(nextrect(self,x=48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
            self.__vaicolidir.append('right')
        if any(nextrect(self,x=-48).colliderect(barreira.get_rect()[a]) for barreira in paredes for a in range(0,len(barreira.get_rect()))) or any(nextrect(self,x=-48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
            self.__vaicolidir.append('left')
        if any(nextrect(self,y=-48).colliderect(barreira.get_rect()[a]) for barreira in paredes for a in range(0,len(barreira.get_rect()))) or any(nextrect(self,y=-48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
            self.__vaicolidir.append('up')
        if any(nextrect(self,y=48).colliderect(barreira.get_rect()[a]) for barreira in paredes for a in range(0,len(barreira.get_rect()))) or any(nextrect(self,y=48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
            self.__vaicolidir.append('down')
        if self.x +48 >= 590 or nextrect(self,x=48).colliderect(princesa):
            self.__vaicolidir.append('right')
        if self.x -48 <= 110  or nextrect(self,x=-48).colliderect(princesa):
            self.__vaicolidir.append('left')
        if self.y -48 <= 110  or nextrect(self,y=-48).colliderect(princesa):
            self.__vaicolidir.append('up')
        if self.y +48 >= 590  or nextrect(self,y=48).colliderect(princesa):
            self.__vaicolidir.append('down')
        if 'right' in self.__vaicolidir and 'left' in self.__vaicolidir and 'down' in self.__vaicolidir and 'up' in self.__vaicolidir:
            pass
        else:
            if self.x != charx and self.y != chary:
                self.__random = bool(getrandbits(1))
                if self.__random:
                    self.horizontal(charx,chary)
                else:
                    self.vertical(charx,chary)
            elif self.x != charx and not self.y != chary:
                self.horizontal(charx,chary)
            elif self.y != chary and not self.x != charx:
                self.vertical(charx,chary)           

def nextrect(objeto:Entidade, x:int = 0, y:int = 0) -> pygame.Rect: #x = -48 ou 0 ou 48 | y = -48 ou 0 ou 48 
    '''Função utilizada para checar futuras colisões.
    
    Cria um rect futuro para o objeto com os parâmetros fornecidos.

    - Parâmetros:
        - objeto: É o objeto que será posto em uma posição futura para a checagem, sendo esses os objetos
        que possuem sistema de movimento, como ladrões e players.
        - x: Pode ser -48, 0, ou 48, que são as possíveis próximas posições de Y, podendo subtrair ou adicionar na coordenada X original.
        - y: Pode ser -48, 0, ou 48, que são as possíveis próximas posições de Y, podendo subtrair ou adicionar na coordenada Y original.
    
    - Retorna:
        O rect com os valores alterados para a futura posição do objeto.
    '''
    rect = pygame.Rect(objeto.x+x, objeto.y+y, 48,48)
    return rect

def check_colision_list(entidade: Entidade, objetos: list[pygame.Rect] | list[list[pygame.Rect]], matriz: bool = False, x: int = 0, y: int = 0):
    '''Checa se haverá alguma colisão futura com uma lista de rects'''
    if matriz:
        for objeto in objetos:
            for rect in objeto:
                if nextrect(entidade, x ,y).colliderect(rect):
                    return True
    else:
        for rect in objetos:
            if nextrect(entidade, x, y).colliderect(rect):
                return True
    return False

def random_blood_sprite(sprites: list[pygame.Surface]) -> pygame.Surface:
    rand1 = bool(getrandbits(1))
    rand2 = bool(getrandbits(1))
    
    imagem = sprites[randint(0,len(sprites)-1)]
    imagem = pygame.transform.flip(imagem, rand1, rand2)
    
    return imagem
