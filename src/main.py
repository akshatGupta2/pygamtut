import pygame
import sys


def main():
        pygame.display.init()
        pygame.font.init()
        
        DISPLAY=pygame.display.set_mode((800,400))
        CLOCK=pygame.time.Clock()
        pygame.display.set_caption("Hello")
        
        # creating the Sky
        Sky=pygame.image.load("res\\img\\Sky.png").convert()
        # blitting image on the surface
        DISPLAY.blit(Sky,(0,0))
        
        # creating the ground
        Ground=pygame.image.load("res\\img\\ground.png").convert()
        # blitting the ground on dispay just below the sky
        DISPLAY.blit(Ground,(0,300))
        
        # loading font
        Ptext=pygame.font.Font("res\\fonts\\Pixeltype.ttf",50)
        
        # creating the surface for the font
        helloT=Ptext.render("Hello World", False, pygame.Color(125,125,125))
        # blitting onto the Sky
        DISPLAY.blit(helloT, (50,50))
        
        # importing the snail image
        snail_surf=pygame.image.load("res\\img\\snail1.png")

        # this is the game loop
        while True:
                CLOCK.tick(60)
                DISPLAY.blit(snail_surf,(600,250))
                
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                pygame.display.update()

if __name__=="__main__":
        main()