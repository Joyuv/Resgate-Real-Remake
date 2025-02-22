
import pygame
from random import randint, getrandbits

from abc import ABC, abstractmethod

class Entidade(ABC):
    def __init__(self, x: int, y: int, img: pygame.Surface):        
        self.__x = x
        self.__y = y
        self.__img = img

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y

    def get_img(self):
        '''Função para pegar o sprite personagem.
        
        - Retorna:
            O sprite do personagem.
        '''
        print(self.__img)
        return self.__img

class Player:
    '''Classe para checar e manipular os atributos do personagem.
    
    - Parâmetros:
        - coorx: É a coordenada X do personagem na tela.
        - coory: É a coordenada Y do personagem na tela.
        - vida: Quantidade de vida que o jogador terá.
        - stamina: Quantidade de stamina que o jogador terá.
        - img: Sprite do personagem.
    '''
    def __init__(self, coorx:int, coory:int, vida:int, stamina:int, img:pygame.Surface):
        self.__img = img
        self.__olhando = bool(getrandbits(1))
        self.__img = pygame.transform.flip(self.__img,self.__olhando,False)

        self.__coorx = coorx
        self.__coory = coory
        self.__vida = vida
        self.__stamina = stamina

    def get_coorx(self) -> int:
        '''Função para pegar a coordenada X do personagem.
        
        - Retorna:
            O valor da coordenada X.
        '''
        return self.__coorx
    def get_coory(self) -> int:
        '''Função para pegar a coordenada Y do personagem.
        
        - Retorna:
            O valor da coordenada Y.
        '''
        return self.__coory
    def get_olhando(self) -> bool:
        '''Função para pegar o lado que o personagem está virado.
        
        - Retorna:
            Um valor booleano.
        '''
        return self.__olhando
    def get_img(self) -> pygame.Surface:
        '''Função para pegar o sprite personagem.
        
        - Retorna:
            O sprite do personagem.
        '''
        return self.__img
    def get_vida(self) -> int:
        '''Função para pegar a quantidade de vida do jogador.
        
        - Retorna:
            A quantidade de vida restante do jogador.
        '''
        return self.__vida
    def get_stamina(self) -> int:
        '''Função para pegar a quantidade de stamina do jogador.
        
        - Retorna:
            A quantidade de stamina restante do jogador.
        '''
        return self.__stamina

    
    def set_vida(self,vida:int) -> None:
        '''Função para definir a quantidade de vida do jogador.

        - Parâmetro: 
            - vida: A quantidade de vida que o jogador terá após tomar algum dano.
        '''
        self.__vida = vida
    def set_stamina(self,stamina:int) -> None:
        '''Função para definir a quantidade de stamina do jogador.

        - Parâmetro: 
            - stamina: A quantidade de vida que o jogador terá após andar.
        '''
        self.__stamina = stamina

    def mover(self, key:int, paredes:list[list[pygame.Rect]]):
        '''Função que move o personagem.

        Checa a tecla que foi pressionada, se essa tecla estiver entre as teclas que movem o personagem
        então soma ou subtrai 48 pixeis na coordenada e retira 1 de stamina.

        - Parâmetros:
            - key: A tecla pressionada.
            - paredes: A lista com os rect das barreiras.
        - Retorna:
            Um valor booleano que dá partida ao movimento do ladrão.
        '''
        self.__DIST = 48
        if key == pygame.K_d or key == pygame.K_RIGHT:
            if self.__olhando == True:
                    self.__img, self.__olhando = pygame.transform.flip(self.__img, True, False), False
            if self.__coorx + 48 >= 590: pass
            elif any(nextrect(self,x=48).colliderect(paredes[a][b])for a in range(0,len(paredes)) for b in range(0,len(paredes[a]))): pass

            else:
                self.__coorx, self.__stamina = self.__coorx + self.__DIST, self.__stamina - 1; return True
        if key == pygame.K_a or key == pygame.K_LEFT:
            if self.__olhando == False:
                    self.__img, self.__olhando = pygame.transform.flip(self.__img, True, False), True
            if self.__coorx - 48 <= 110: pass
            elif any(nextrect(self,x=-48).colliderect(paredes[a][b])for a in range(0,len(paredes)) for b in range(0,len(paredes[a]))): pass

            else: self.__coorx, self.__stamina = self.__coorx - self.__DIST, self.__stamina - 1; return True
        if key == pygame.K_w or key == pygame.K_UP:
            if self.__coory - 48 < 110: pass
            elif any(nextrect(self,y=-48).colliderect(paredes[a][b])for a in range(0,len(paredes)) for b in range(0,len(paredes[a]))): pass

            else: self.__coory, self.__stamina = self.__coory - self.__DIST, self.__stamina - 1; return True
        if key == pygame.K_s or key == pygame.K_DOWN:
            if self.__coory + 48 >= 590:
                pass
            elif any(nextrect(self,y= 48).colliderect(paredes[a][b])for a in range(0,len(paredes)) for b in range(0,len(paredes[a]))):
                pass
            else:
                self.__coory += self.__DIST
                self.__stamina -= 1
                return True
class Ladroes:
    '''Classe para checar e manipular atributos dos ladrões.
    
    - Parâmetros:
        - coorx: Coordenada X do ladrão.
        - coory: Coordenada Y do ladrão.
        - img: Sprite do ladrão.
    '''
    def __init__(self,coorx:int, coory:int, img:pygame.Surface) -> None:
        self.__img = img
        self.__olhando = bool(getrandbits(1))
        self.__img = pygame.transform.flip(self.__img,self.__olhando,False)

        self.__coorx = coorx
        self.__coory = coory
    
    def get_coorx(self) -> int:
        '''Pega a coordenada X do ladrão.

        - Retorna:
            Um valor inteiro que é a coordenada X.
        '''
        return self.__coorx
    def get_coory(self) -> int:
        '''Pega a coordenada Y do ladrão.

        - Retorna:
            Um valor inteiro que é a coordenada Y.
        '''
        return self.__coory
    def get_img(self) -> pygame.Surface:
        '''Pega o sprite do ladrão.

        - Retorna:
            O sprite do ladrão.
        '''
        return self.__img
    def get_olhando(self) -> bool:
        '''O lado que o sprite do ladrão está virado.

        - Retorna:
            Um valor booleano.
        '''
        return self.__olhando
    def get_rect(self) -> pygame.Rect:
        '''Pega o rect do ladrão.

        - Retorna:
            O rect do ladrão.
        '''
        return pygame.Rect(self.__coorx,self.__coory,48,48)
    
    def h_left(self, chary: int):
        '''Parte do movimento horizontal do ladrão.

        - Parâmetro:
            - chary: A coordenada Y do cavaleiro.
        '''
        if 'left' in self.__vaicolidir:
            if self.__coory > chary: 
                if 'up' in self.__vaicolidir:
                    if 'down' in self.__vaicolidir:
                        if 'right' in self.__vaicolidir: pass
                        else: #direita (+48)
                            self.__coorx += 48
                            if self.__olhando == True:
                                self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), False
                    else: self.__coory += 48 #desce (+48)
                else: self.__coory -= 48 #sobe (-48)
            else:
                if 'down' in self.__vaicolidir:
                    if 'up' in self.__vaicolidir:
                        if 'right' in self.__vaicolidir: pass
                        else: #direita (+48)
                            self.__coorx += 48
                            if self.__olhando == True:
                                self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), False
                    else: self.__coory -= 48 #sobe (-48)
                else: self.__coory += 48 #desce (+48)                    
        else: #Esquerda (-48)
            self.__coorx -=48
            if self.__olhando == False:
                self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), True
    def h_right(self, chary: int):
        '''Parte do movimento horizontal do ladrão.

        - Parâmetro:
            - chary: A coordenada Y do cavaleiro.
        '''
        if 'right' in self.__vaicolidir:
            if self.__coory > chary: 
                if 'up' in self.__vaicolidir:
                    if 'down' in self.__vaicolidir:
                        if 'left' in self.__vaicolidir: pass
                        else: #esquerda (-48)
                            self.__coorx -= 48
                            if self.__olhando == False:
                                self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), True
                    else: self.__coory += 48 #desce (+48)
                else: self.__coory -= 48 #sobe (-48)                       
            else:
                if 'down' in self.__vaicolidir:
                    if 'up' in self.__vaicolidir:
                        if 'left' in self.__vaicolidir: pass
                        else: #esquerda (-48)
                            self.__coorx -= 48
                            if self.__olhando == False:
                                self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), True
                    else: self.__coory -= 48 #sobe (-48)
                else: self.__coory += 48 #desce (+48)
        else: #Direita (-48)
            self.__coorx +=48
            if self.__olhando == True:
                self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), False
    def v_up(self, charx: int):
        '''Parte do movimento vertical do ladrão.

        - Parâmetro:
            - charx: A coordenada X do cavaleiro.
        '''
        if 'up' in self.__vaicolidir:
            if self.__coorx > charx: 
                if 'right' in self.__vaicolidir:
                    if 'left' in self.__vaicolidir:
                        if 'down' in self.__vaicolidir: pass
                        else: self.__coory += 48 #baixo (+48)
                    else: #esquerda (-48)
                        self.__coorx -= 48
                        if self.__olhando == False:
                            self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), True
                else: #direita (+48)
                    self.__coorx += 48
                    if self.__olhando == True:
                        self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), False     
            else:
                if 'left' in self.__vaicolidir:
                    if 'right' in self.__vaicolidir:
                        if 'down' in self.__vaicolidir: pass
                        else: self.__coory += 48 #desce (+48)
                    else: #direita (+48)
                        self.__coorx += 48
                        if self.__olhando == True:
                            self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), False
                else: #esquerda (-48)
                    self.__coorx -= 48
                    if self.__olhando == False:
                        self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), True
        else: self.__coory -=48 #cima (-48)
    def v_down(self, charx: int):
        '''Parte do movimento vertical do ladrão.

        - Parâmetro:
            - charx: A coordenada X do cavaleiro.
        '''
        if 'down' in self.__vaicolidir:
            if self.__coorx > charx: 
                if 'right' in self.__vaicolidir:
                    if 'left' in self.__vaicolidir:
                        if 'up' in self.__vaicolidir: pass
                        else: self.__coory -= 48 #cima (-48)
                    else: #esquerda (-48)
                        self.__coorx -= 48
                        if self.__olhando == False:
                            self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), True
                else: #direita (+48)
                    self.__coorx += 48
                    if self.__olhando == True:
                        self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), False
            else:
                if 'left' in self.__vaicolidir:
                    if 'right' in self.__vaicolidir:
                        if 'up' in self.__vaicolidir: pass
                        else: self.__coory -= 48 #sobe (-48)                                      
                    else: #direita (+48)
                        self.__coorx += 48
                        if self.__olhando == True:
                            self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), False                                       
                else: #esquerda (-48)
                    self.__coorx -= 48
                    if self.__olhando == False:
                            self.__img, self.__olhando = pygame.transform.flip(self.__img,True,False), True                                                                                 
        else: self.__coory +=48 #baixo (+48)
    def horizontal(self, charx:int, chary:int):
        '''Função que junta os movimentos horizontais.
        
        Checa se o X do ladrão é diferente do X do cavaleiro, se for, 
        então checa se é mais favorável pro ladrão andar para a esquerda ou para a direita.

        - Parâmetros:
            - charx: Coordenada X do cavaleiro.
            - chary: Coordenada Y do cavaleiro.
        '''
        if self.__coorx != charx:
            if self.__coorx > charx:#andando pra esquerda(-48)
                self.h_left(chary)
            elif self.__coorx < charx:
                self.h_right(chary)
    def vertical(self, charx:int, chary:int):
        '''Função que junta os movimentos verticais.
        
        Checa se o Y do ladrão é diferente do Y do cavaleiro, se for, 
        então checa se é mais favorável pro ladrão andar para cima ou para baixo.

        - Parâmetros:
            - charx: Coordenada X do cavaleiro.
            - chary: Coordenada Y do cavaleiro.
        '''
        if self.__coory != chary:
            if self.__coory > chary:#andando pra cima(-48)
                self.v_up(charx)
            elif self.__coory < chary:#andando pra baixo(+48)
                self.v_down(charx)
    def andar(self,charx:int, chary:int, thiefs:list, paredes:list[list[pygame.Rect]], princesa:pygame.Rect) -> None:
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
        if any(nextrect(self,x=48).colliderect(barreira[a]) for barreira in paredes for a in range(0,len(barreira))) or any(nextrect(self,x=48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
            self.__vaicolidir.append('right')
        if any(nextrect(self,x=-48).colliderect(barreira[a]) for barreira in paredes for a in range(0,len(barreira))) or any(nextrect(self,x=-48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
            self.__vaicolidir.append('left')
        if any(nextrect(self,y=-48).colliderect(barreira[a]) for barreira in paredes for a in range(0,len(barreira))) or any(nextrect(self,y=-48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
            self.__vaicolidir.append('up')
        if any(nextrect(self,y=48).colliderect(barreira[a]) for barreira in paredes for a in range(0,len(barreira))) or any(nextrect(self,y=48).colliderect(thiefs[t].get_rect())for t in range(0,len(thiefs))):
            self.__vaicolidir.append('down')
        if self.__coorx +48 >= 590 or nextrect(self,x=48).colliderect(princesa):
            self.__vaicolidir.append('right')
        if self.__coorx -48 <= 110  or nextrect(self,x=-48).colliderect(princesa):
            self.__vaicolidir.append('left')
        if self.__coory -48 <= 110  or nextrect(self,y=-48).colliderect(princesa):
            self.__vaicolidir.append('up')
        if self.__coory +48 >= 590  or nextrect(self,y=48).colliderect(princesa):
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
class Paredes(Entidade):
    '''Classe para criar as paredes que ficam no mapa para atrapalhar o jogador.

    - Parâmetros:
        - x: Coordenada X que a parede ficará.
        - y: Coordenada Y que a parede ficará.
    '''
    def __init__(self, x:int, y:int, img = pygame.Surface) -> None:
        super().__init__(x, y, img)
        
    def get_rect(self):
        return self.__listarect
    
    def new_rect(self) -> list[pygame.Rect]:
        '''Cria os rect das paredes com os parâmetros dados inicialmente.

        Cada parede inteira tem 5 rects, que é o de cada quadrado que faz parte dela, assim ela pode
        ser quebrada pela bomba.
        
        - Retorna:
            A lista com os rect da parede.
        '''
        self.__listarect = []
        self.__rect0 = pygame.Rect(self.get_x(),self.get_y(),48, 48)
        self.__listarect.append(self.__rect0)

        for multiplier in range(-1,2,2):
            self.__rect1 = pygame.Rect(self.get_x()-48*multiplier, self.get_y(), 48, 48)
            self.__rect2 = pygame.Rect(self.get_x(), self.get_y()-48*multiplier, 48,48)
    
            self.__listarect.append(self.__rect1)
            self.__listarect.append(self.__rect2)
    
        return self.__listarect
    
def nextrect(objeto:Player | Ladroes, x:int = 0, y:int = 0) -> pygame.Rect: #x = -48 ou 0 ou 48 | y = -48 ou 0 ou 48 
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
    rect = pygame.Rect(objeto.get_coorx()+x, objeto.get_coory()+y, 48,48)
    return rect

def random_blood_sprite(sprites: list[pygame.Surface]) -> pygame.Surface:
    rand1 = bool(getrandbits(1))
    rand2 = bool(getrandbits(1))
    
    imagem = sprites[randint(0,len(sprites)-1)]
    imagem = pygame.transform.flip(imagem, rand1, rand2)
    
    return imagem
