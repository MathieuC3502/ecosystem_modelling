import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

class World_Environnement:
    """Class to model the world/environment of the simulation
    """
    def __init__(self,grid_size=(10,10)):
        self.grid_size=grid_size
        grid_ratio=self.grid_size[1]/self.grid_size[0]
        fig, ax = plt.subplots(figsize=(10, grid_ratio*10))
        plt.ion()
        self.axes=ax
        
    def set_empty_grid(self,show_plot=False,draw_grid=True):
        
        self.axes.set_xlim(0, self.grid_size[0])
        self.axes.set_ylim(0, self.grid_size[1])
        
        self.axes.xaxis.set_major_locator(MultipleLocator(1))
        self.axes.yaxis.set_major_locator(MultipleLocator(1))
        
        if draw_grid:
            plt.grid()
        if show_plot:
            plt.show()
        
if __name__=="__main__":
    world=World_Environnement((20,20))
    world.set_empty_grid(show_plot=True,draw_grid=False)