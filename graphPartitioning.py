import matplotlib.pyplot as plt 
import random
import math
import numpy as np
import time
import copy
       
INF = 10000
alpha = 0.999
threshold = 0.01

# we want to initialize the structure
# i.e. place the k-elements on the N X N grid

def initialize(k):
	v1=[i for i in range(1,int(k/2))]
	v2=[i for i in range(int(k/2),k+1)]
	return v1,v2

# Suppose you are in any state say S, then you can go to 
# some other state S'
def findNeighbourState(v1,v2):
	# We will follow these two protocols, each 50% of time
	# 1. swap positions of any two elements
	# 2. Move any element fom v1/v2 to v2/v1
	l1 = len(v1)
	l2 = len(v2)

	tempv1 = copy.deepcopy(v1)
	tempv2 = copy.deepcopy(v2)
	if(l1==0):
		j = random.randint(0,l2-1)
		temp = tempv2[j]
		tempv2.remove(temp)			
		tempv1.append(temp)
		return tempv1, tempv2
	if(l2 == 0):
		i = random.randint(0,l1-1)
		temp = tempv1[i]
		tempv1.remove(temp)
		tempv2.append(temp)	
		return tempv1, tempv2
	if(np.random.random()<0.5):
		
		i = random.randint(0,l1-1)
		j = random.randint(0,l2-1)
		temp = tempv1[i]
		tempv1[i] = tempv2[j]
		tempv2[j] = temp
	else:

		choose = random.randint(1,2)
		if(choose ==1 ):
			i = random.randint(0,l1-1)
			temp = tempv1[i]
			tempv1.remove(temp)
			tempv2.append(temp)
		else:
			j = random.randint(0,l2-1)
			temp = tempv2[j]
			tempv2.remove(temp)			
			tempv1.append(temp)

	return tempv1, tempv2


# This will return the updated temperature 
# according to some annealing schedule
def updateTemp(T):
	return alpha*T


# This function finds the total wirelength

# V1 and V2 is list

def cost(v1, v2, connections):
	distance = 0
	l1 = len(v1)
	l2 = len(v2)


	for i in v1:
		for j in v2:
			if(i<j):
				if(connections[i,j] == 1):
					distance+=1
					#print i,j
			else:
				if(connections[j,i] == 1):
					distance+=1
					#print i,j
	c = distance + (0.5*(l1-l2)**2)
	print v1, v2, c				
	return (c)


def annealing(k, connections):
	T = INF
	# We initialize the the two partitions
	v1,v2 = initialize(k)
	minCost = cost(v1,v2,connections)

	print "Initial Cost",minCost

	tic = time.clock()

	# No. of interation at each temperature
	# No. of temperature points to try
	while(T > threshold):
		tempv1,tempv2 = findNeighbourState(v1,v2)
		tempCost = cost(tempv1, tempv2, connections)
		delta = tempCost - minCost
		if (delta<0):
			v1 = tempv1
			v2 = tempv2
			minCost = tempCost
		else:
			p = np.exp(-delta / T)
			if(np.random.random()<p):
				v1 = tempv1
				v2 = tempv2
				minCost = tempCost
		T = updateTemp(T)
		

	
	return v1,v2,minCost, tic

def create(k) :
    #we want k nodes to be connected to each other 
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
                
                
                        


def mainrun(auto):
        if auto == 1:
                k = 6
        else :
                k = auto

	# connections = create(k)
	# we can create random connections
	connections = np.zeros([k+1,k+1])
	connections[1,3] = 1
	connections[2,3] = 1
	connections[4,5] = 1
	connections[1,2] = 1
	connections[3,4] = 1
	connections[4,6] = 1
	connections[5,6] = 1
	if auto != 1:
                connections = create(k)
                
	v1,v2,minCost, tic = annealing(k, connections)
	toc = time.clock()
	tim = toc - tic
	print "time taken ", tim

	print "Final Cost", minCost

	print v1
	print v2
