from src.species.animal import Animal

class Rabbit(Animal):
    """Class representing the Rabbit species

    Args:
        Species (Species Class): Parent class representing a generic species
    """
    
    def __init__(self,initial_population_density,world):
        super().__init__(initial_population_density,world)
        
    def __str__(self):
        return f"Rabbit species with initial density of {self.population_density[0]} individuals per squared km at time t=0"
    
if __name__=="__main__" :
    rabbit1=Rabbit(4,"assets/sprites/rabbit.png")
    print(rabbit1)