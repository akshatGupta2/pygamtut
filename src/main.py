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
    siz=pygame.display.get_window_size()
    l=[siz[0]/2-100,siz[1]/2-50]
    while True:
        FPS.tick(60)
        DISPLAY.fill('black')
        DISPLAY.blit(SURFACE,tuple(l))
        for event in pygame.event.get():
            if event.type==pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.locals.KEYDOWN:
                if event.key == pygame.K_UP:
                    DISPLAY.fill('black')
                    DISPLAY.blit(SURFACE,tuple(l))
                    l[1]-=10
                elif event.key == pygame.K_DOWN:
                    DISPLAY.fill('black')
                    DISPLAY.blit(SURFACE,tuple(l))
                    l[1]+=10
                elif event.key == pygame.K_LEFT:
                    DISPLAY.fill('black')
                    DISPLAY.blit(SURFACE,tuple(l))
                    l[0]-=10
                elif event.key == pygame.K_RIGHT:
                    DISPLAY.fill('black')
                    DISPLAY.blit(SURFACE,tuple(l))
                    l[0]+=10
        pygame.display.update()


if __name__=="__main__":
    main()