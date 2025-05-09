import matplotlib.pyplot as plt
import pygame
from src.utils.loaders import load_png

class Animal(pygame.sprite.Sprite):
    """Class representing a generic animal
    """
    def __init__(self,initial_population_density,sprite_filepath,world=None):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png(sprite_filepath)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.population_density=[initial_population_density]
        if world is not None:
            self.world=world
            self.position=(world.grid_size[0]/2,world.grid_size[1]/2)
            self.rect.center = self.position
        else:
            self.position=(0,0)
            self.rect.center = self.position
        
    def draw(self,show=False):
        self.world.axes.plot(self.position[0],self.position[1],'or')
        if show:
            plt.show()
            
    def move(self,displacement_vector,draw_vector=False):
        old_position=self.position
        x2, y2 = (old_position[0]+displacement_vector[0],old_position[1]+displacement_vector[1])
        self.position=(x2,y2)
        self.rect.center = self.position
        if draw_vector:
            x1, y1 = old_position
            self.world.axes.arrow(x1, y1, x2 - x1, y2 - y1, head_width=0.5, head_length=0.5, fc='k', ec='k')
            self.draw()

            plt.show()
            
    def update(self):
        self.move((0.5,0.5))