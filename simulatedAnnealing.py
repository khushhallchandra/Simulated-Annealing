import random
import math
import numpy as np

INF = 10000
alpha = 0.9
k = 10
# let's say we are given a set of points in one dimension and we 
# want to initialize the structure
def initialize(connections):
	N = connections.shape[0]
	# Here we have one-dimension
	placement = {}
	for i in xrange(N):
		x = np.random.randint(1,100)
		

# Suppose you are any state say S, then there can be say k possible neighbourhoods
# In that case, call this function k times. This set of neighbourhood will form set of S'
def findNeighbour(positions):
	# given a placement find new placement
	# In one-dim, we may simply flip x-coordinates
	node1 = np.random.randint(1,10)
	node2 = np.random.randint(1,10)
	# Now flip the position of these nodes
	temp = position[str(node1)]
	position[str(node1)] = position[str(node2)]
	position[str(node2)] = temp
	
	# simialrly we can flip some m positions, if required
	return positions

# This will return the updated temperature 
# according to some schedule
def updateTemp(T):
	return alpha*T

def annealing(positions,T):
	# No. of interation at each temperature
	# No. of temperature points to try
    while (T > threshold):        
		nextOrder = nextArrangement(currentOrder);
            deltaDistance = GetTotalDistance(nextOrder) - distance;
                if ():
                    for i in range(len(nextOrder):
                        currentOrder[i] = nextOrder[i];

                    distance = deltaDistance + distance;
                temperature *= coolingRate;

                iteration++;

# This function finds the cost of any state S'
def cost():


def main():
	# Lets say size of each block is one unit
	# i.e. if a,b,c are connected serially, the min wirelength would be 2
	# Initially we only know who is connected with whome
	# We will use 2-d numpy array
	# one will represent there is connection between i and j, 0 otherwise
	connections = np.empty([3,3])
	connections[0,1] = 1
	#---------Input done---------

	init = initialize(connections)
	
	T = INF
	

	
