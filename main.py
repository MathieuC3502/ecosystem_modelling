import pygame
from src.species.rabbit import Rabbit
# import matplotlib.pyplot as plt

def main():

    pygame.init()
    screen=pygame.display.set_mode((1000, 500))
    pygame.display.set_caption('Ecosystem Agent-Based Simulation')
    
    rabbit1=Rabbit(4,"assets/sprites/rabbit.png")

    clock = pygame.time.Clock()
    RunMainLoop=True
    
    #Simulation Loop
    while RunMainLoop is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RunMainLoop = False
                
        rabbit1.update()
        screen.fill((0,0,0))
        screen.blit(rabbit1.image, rabbit1.rect)
        pygame.display.flip()
        clock.tick(60)
        
    pygame.quit()
                
if __name__=="__main__":
    main()
