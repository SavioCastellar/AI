from definitions import Agent
import numpy as np
from scipy.spatial import distance
import random

class RandAgent(Agent):
    """
    This class implements an agent that explores the environmente randomly
    until it reaches the target
    """

    def __init__(self, env, bound=100):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        
        
        # Visit the last node in the path
        action = {'visit_position': path[-1], 'path': path} 
        # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
        self.percepts = self.env.signal(action)

        # Add visited node
        self.visited.append(path[-1])

        # From the list of viable neighbors given by the environment
        # Select a random neighbor that has not been visited yet
            
        viable_neighbors =  self.percepts['neighbors']

        # If the agent is not stuck
        if viable_neighbors:              
            random.shuffle(viable_neighbors)
            for n in viable_neighbors:
                # Append neighbor to the path and add it to the frontier
                self.frontier = [path + [n]] + self.frontier

    def run(self):
        """Keeps the agent acting until it finds the target
        """
        # Run agent
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])


class BBAgent(Agent):
    """
    This class implements an agent that finds the minimum distance path using branch and bound

    """

    def __init__(self, env, bound=100):
        """Connects to the next available port.

        Args:
            env: A reference to an environment.

        """

        # Make a connection to the environment using the superclass constructor
        Agent.__init__(self,env)
        
        # Get initial percepts
        self.percepts = env.initial_percepts()
        
        # Initializes the frontier with the initial postion 
        self.frontier = [[self.percepts['current_position']]]
        self.cost = [0]
        self.bound = bound
        self.path_path = []
        
        # Initializes list of visited nodes for multiple path prunning
        self.visited = []

    def act(self):
        """Implements the agent action
        """

        # Select a path from the frontier
        path = self.frontier.pop(0)
        cost = self.cost.pop(0)
        
        if cost + distance.euclidean(path[-1],self.percepts['target']) < self.bound:
            # Visit the last node in the path
            action = {'visit_position': path[-1], 'path': path} 
            # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
            self.percepts = self.env.signal(action)

            # Add visited node
            self.visited.append(path[-1])

            if (self.percepts['current_position'] == self.percepts['target']).all():
                self.best_path = path
                self.bound = cost
                print(self.bound)

            # From the list of viable neighbors given by the environment
            # Select a random neighbor that has not been visited yet
            
            viable_neighbors =  self.percepts['neighbors']

            # If the agent is not stuck
            if viable_neighbors:              
                for n in viable_neighbors:
                    # Append neighbor to the path and add it to the frontier
                    self.frontier = [path + [n]] + self.frontier
                    self.cost = [cost + distance.euclidean(path[-1],n)] + self.cost 

    def run(self):
        """Keeps the agent acting until it finds the target
        """
        # Run agent
        while self.frontier:
            self.act()
        print(self.percepts['current_position'])

        for i in range(1000):
            action = {'visit_position': self.best_path[-1], 'path': self.best_path} 
            # The agente sends a position and the full path to the environment, the environment can plot the path in the room 
            self.percepts = self.env.signal(action)

class DFSAgent(Agent):
    def __init__(self,env,bound=100):
        RandAgent.__init__(self,env,bound)

    def act(self):
        path = self.frontier.pop(0)
        action = {'visit_position': path[-1], 'path':path}
        self.percepts = self.env.signal(action)
        self.visited.append(path[-1])
        viable_neighbors = self.percepts['neighbors']
        if viable_neighbors:
            for n in viable_neighbors:
                cycle = False
                for e in path:
                    if (n == e).all():
                        cycle = True
                        break
            if not cycle:
                self.frontier = [path + [n]] + self.frontier

    def run(self):
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])

class BFSAgent(Agent):
    def __init__(self,env,bound=100):
        RandAgent.__init__(self,env,bound)

    def act(self):
        path = self.frontier.pop(0)
        action = {'visit_position': path[-1], 'path':path}
        self.percepts = self.env.signal(action)
        self.visited.append(path[-1])
        viable_neighbors = self.percepts['neighbors']
        if viable_neighbors:
            for n in viable_neighbors:
                cycle = False
                for e in path:
                    if (n == e).all():
                        cycle = True
                        break
            if not cycle:
                self.frontier = self.frontier + [path + [n]]

    def run(self):
        while (self.percepts['current_position'] != self.percepts['target']).any() and self.frontier:
            self.act()
        print(self.percepts['current_position'])

# GreedyAgent
# Objetivo:	
#   Selecionar o vizinho com menor custo
# 	Peguei a distância entre cada nó que está na vizinhança e o ponto atual
#       for n in range (len(neighbors)):
# 		    distance.euclidean(self.percepts[‘current_position’], path[n])
#   Salvei esses valores em uma lista e peguei o menor valor da lista (min(list))
#   Nesse ponto, tinha armazenado o valor dessa menor distância	
#   Porém, não consegui estabelecer uma relação entre essa variável e a posição 
#   que esse nó ocupa na lista de fronteiras
# Tentativa:
#   Fazer um dicionário, atribuindo um nome aleatório para cada valor de 
#   distância, e enviar ao ‘path’ o nome que tivesse a menor distância

# AStarAgent
# Objetivo:
#   Criar um algoritmo parecido com Branch-and-Bound
#   Remover o limite (bound)
#   Menor distância entre o nó atual e o próximo + menor valor da estimativa da heurística
