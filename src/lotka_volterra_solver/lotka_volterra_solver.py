import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

class Lotka_Volterra_Solver:
    """Class to calculate the results of a Lotka-Volterra system of equations based on initial parameters
    """
    
    def __init__(self,x0,y0,alpha=1,beta=0.2,delta=0.5,gamma=0.2):
        """Constructor of the class

        Args:
            alpha (int, optional): Prey growth rate when no predators. Defaults to 1.
            beta (int, optional): Effect of predation on preys. Large value means predators are very efficient at reducing prey population. Defaults to 1.
            delta (int, optional): Rate at which the predators' population grows when they have more prey to eat. Defaults to 1.
            gamma (int, optional): Predator death rate when no prey. Defaults to 1.
        """
        self.alpha=alpha
        self.beta=beta
        self.delta=delta
        self.gamma=gamma
        self.x0=x0
        self.y0=y0
        
    def derivative(self, X, t):
        x, y = X
        dotx = x * (self.alpha - self.beta * y)
        doty = y * (-self.delta + self.gamma * x)
        return np.array([dotx, doty])
    
    def solve(self, max_time_in_days, number_of_time_steps):
        t = np.linspace(0.,max_time_in_days, number_of_time_steps)
        X0 = [self.x0, self.y0]
        res = integrate.odeint(self.derivative, X0, t)
        x, y = res.T
        self.results=[x,y,t]
        
    def plot_results(self,show=True):
        plt.figure()
        plt.grid()
        plt.title("odeint method")
        plt.plot(self.results[2], self.results[0], '-b', label = 'Rabbits')
        plt.plot(self.results[2], self.results[1], '-r', label = "Wolves")
        plt.xlabel('Time t, [days]')
        plt.ylabel('Population (per km^2)')
        plt.legend()
        if show:
            plt.show()
        
if __name__=="__main__":
    solver=Lotka_Volterra_Solver(10,10,1,0.2,0.5,0.2)
    solver.solve(50,1000)
    solver.plot_results()