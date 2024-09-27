import pygame
from random import randint

class Sangue:
    def __init__(self, x:int, y:int, img:list[pygame.Surface]):
        self.__x = x
        self.__y = y

        self.__rand1 = randint(0,1)
        self.__rand2 = randint(0,1)

        self.__img = img[randint(0,1)]
        self.__img = pygame.transform.flip(self.__img,self.__rand1,self.__rand2)
        
    def get_img(self):
        return self.__img
    
    def get_pos(self):
        self.__pos = (self.__x,self.__y)
        return self.__pos