import matplotlib.pyplot as plt 
import random
import math
import numpy as np
import time

       
INF = 10000
alpha = 0.999
threshold = 0.01

# we want to initialize the structure
# i.e. place the k-elements on the N X N grid
def initialize(k, N, grid):

	for element in xrange(1,k+1):
		assigned = False
		while(not assigned):
			i = np.random.randint(N)
			j = np.random.randint(N)
			if(grid[i,j]==0):
				grid[i,j] = element
				assigned = True
	return grid

# Suppose you are in any state say S, then you can go to 
# some other state S'
def findNeighbourState(N, k, grid):
	# We will follow these two protocols, each 50% of time
	# 1. swap positions of any two elements
	# 2. Move any element to a new position in the grid

	tempGrid = np.array(grid)
	if(np.random.random()<0.5):
		element1 = np.random.randint(1, k+1)
		element2 = np.random.randint(1, k+1)
                # to ensure element2 != element1 
		while(element2==element1):
			element2 = np.random.randint(1, k+1)
		(x1,y1) = zip(*np.where(tempGrid == element1))[0]
		(x2,y2) = zip(*np.where(tempGrid == element2))[0]
		tempGrid[x1, y1] = element2
		tempGrid[x2, y2] = element1
	else:
		element1 = np.random.randint(1, k+1)
		(x1,y1) = zip(*np.where(tempGrid == element1))[0]
		# find an empty place
		temp = zip(*np.where(tempGrid == 0))
		(x2,y2) = temp[np.random.randint(len(temp))]
		tempGrid[x1, y1] = 0
		tempGrid[x2, y2] = element1		

	return tempGrid


# This will return the updated temperature 
# according to some annealing schedule
def updateTemp(T):
	return alpha*T


# This function finds the total wirelength
def cost(k, grid, connections):
	distance = 0
	for element in xrange(1,k+1):
		(x1,y1) = zip(*np.where(grid == element))[0]
		for nextElement in range(element+1,k+1):
			if(connections[element,nextElement]):
				(x2,y2) = zip(*np.where(grid == nextElement))[0]
				distance += np.absolute(x2-x1) + np.absolute(y2-y1)
	return distance


def annealing(N, k, grid, connections):
	T = INF
	# We initialize the grid
	grid = initialize(k, N, grid)
	minCost = cost(k, grid, connections)

	print "Initial Cost",minCost
	print "Initial Grid"
	print grid
	printgrid(grid)
	tic = time.clock()

	# No. of interation at each temperature
	# No. of temperature points to try
	while(T > threshold):
		tempGrid = findNeighbourState(N, k, grid)
		tempCost = cost(k, tempGrid, connections)
		delta = tempCost - minCost
		if (delta<0):
			grid = tempGrid
			minCost = tempCost
		else:
			p = np.exp(-delta / T)
			if(np.random.random()<p):
				grid = tempGrid
				minCost = tempCost
		T = updateTemp(T)

	return grid,minCost, tic

def printgrid(grid):
        plt.imshow(grid,interpolation='None', aspect = "auto")
        for (j,i),label in np.ndenumerate(grid):
                plt.text(i,j,label,ha='center',va='center')
        plt.show() 

def create(k) :
        # Assuming that each element can have two input and one output.
	# Initially we only know who is connected with whom. We use 2-d
	# array 1 will represent there is connection between i and j,
	# 0 otherwise
	#filling the values in only upper triangular matrix
  
        connections = np.zeros([k+1,k+1])
        ii = 0
        while ii < k+1:
                i = int(random.randint(1,k))
                j = int(random.randint(1,k))
                if (i > j )& (connections[j,i] ==0):
                        connections[j,i] = 1
                        ii = ii+1
                        print (j,i)
                if (i < j) & (connections[i,j] ==0):
                        connections[i,j] = 1
                        ii = ii+1
                        print (i,j)
                        
        return connections
                
                
                        


def mainrun(N,k):

	# For simplicty, assume that the element to be paced is point sized.
	# And we have to place these k-point sized element on N X N grid.
        
	#N = 10
	#k = 12

	# We will store the positions of the elements in the N X N grid
	grid = np.zeros([N,N])
	connections = create(k)               

	finalGrid,cost,tic = annealing(N, k, grid, connections)
	toc = time.clock()
	tim = toc - tic
	print "time taken ", tim

	print "Final Cost", cost
	print "Final Grid"
	print finalGrid
	printgrid(finalGrid) 
        
