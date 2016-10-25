import numpy as np
import simulatedAnnealing
import matplotlib.pyplot as plt
# For simplicty, assume that the element to be paced is point sized.
# And we have to place these k-point sized element on N X N grid.

N = 5
k = 5

# We will store the positions of the elements in the N X N grid
grid = np.zeros([N,N])
connections = np.zeros([k+1,k+1])

# Assuming that each element can have two input and one output.
# Initially we only know who is connected with whome. We use 2-d
# array 1 will represent there is connection between i and j,
# 0 otherwise
#filling the values in only upper triangular matrix
connections[1,3] = 1
connections[2,3] = 1
connections[4,5] = 1
connections[3,5] = 1

# connections[3,1] = 1
# connections[3,2] = 1

finalGrid, cost, storedCost = simulatedAnnealing.annealing(N, k, grid, connections)

print "Final Cost", cost
print "Final Grid"
print finalGrid

plt.plot(storedCost)
plt.title("Cost vs interation")
plt.xlabel('interation')
plt.ylabel('Cost')
plt.show()
