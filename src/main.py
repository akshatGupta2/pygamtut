import pygame
import pygame.locals
import sys

def main():
    pygame.init()
    DISPLAY=pygame.display.set_mode((800,600))
    DISPLAY.set_alpha(5)
    pygame.display.set_caption("Hello Window 2")
    SURFACE=pygame.Surface((200,100))
    SURFACE.fill('red')
    FPS=pygame.time.Clock()
    # siz=pygame.display.get_window_size()
    l=[0,0]
    while True:
        FPS.tick(60)
        DISPLAY.fill('black')
        DISPLAY.blit(SURFACE,tuple(l))
        l[1]+=1
        l[0]+=1
        for event in pygame.event.get():
            if event.type==pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__=="__main__":
    main()