import pygame
from pygame.locals import *
import sys

class Animation(object) :
    card = []
    root = "../images/cards/"
    screen = pygame.display.set_mode((840, 630))
    pygame.display.set_caption('test')
    i = 0
    clock = pygame.time.Clock()
    while(i < 10):
        card.append(pygame.image.load("%scardback.png" % (root)).convert_alpha())
        i += 1
    cards = 0
    while(1) :
        clock.tick(1)
        i = 0
        j = 0
        while(cards < 10) :
            screen.fill((0, 0, 0))            
            screen.blit(card[j], (i-100, 100))
            screen.blit(card[j], (i-100, 300))            
            screen.blit(card[j], (i-100, 500))
            pygame.display.update()
            i += 1
            if i == 1000 :
                cards += 1
                i, j = 0, 0
            for eve in pygame.event.get() :
                if eve.type == QUIT :
                    sys.exit()
                if eve.type == KEYDOWN :
                    if eve.key == K_ESCAPE :
                        sys.exit()
                
        
        for eve in pygame.event.get() :
                if eve.type == QUIT :
                    sys.exit()
                if eve.type == KEYDOWN :
                    if eve.key == K_ESCAPE :
                        sys.exit()
        cards = 0
if __name__ == "__main__" :
    MY_GAME = Animation()
