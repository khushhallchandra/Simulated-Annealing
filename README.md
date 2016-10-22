# EE-677 VLSI CAD Course Project
####  VLSI placement usning Simulated Annealing minimizing the wirelength
#### PseudoCode:
```python
function annealing():
    Temperature = INFINITE
    # generate random configuration
	grid = initialize()
	minCost = cost(grid)
	while(Temperature > threshold):
    	tempGrid = findNeighbourState(grid)
        tempCost = cost(tempGrid)
		delta = tempCost - minCost
		if (delta<0):
			grid = tempGrid
			minCost = tempCost
		else:
			probabilty = exp(-delta / Temperature)
			if(random(0,1)<probabilty):
			    grid = tempGrid
				minCost = tempCost
		Temperature = updateTemp(Temperature)
	return grid
```	

```python
function findNeighbourState(grid):
	# We will follow these two protocols, each 50% of time
	# 1. swap positions of any two elements
	# 2. Move any element to an empty position in the grid
	tempGrid = copy(grid)
	if(random(0,1)<0.5):
		element1 = select any element
		element2 = select another element
        swap element1 and element2 in tempGrid
	else:
		element1 = select any element
		# find an empty position in the tempGrid
		Move element1 to the empty position	
	return tempGrid
```	

#### Group Members:
##### Khushhall Chandra Mahajan
##### Charvi Rastogi