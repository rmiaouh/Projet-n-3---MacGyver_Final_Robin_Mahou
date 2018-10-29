import numpy
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import sys

#Cette définition de Maze provient du site internet Wikipedia
def maze(width=15, height=15, complexity=.75, density=.75):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1]))) # number of components
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2))) # size of components
    # Build actual maze
    Z = numpy.zeros(shape, dtype=bool)
    #print(Z)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2 # pick a random position
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:            
                neighbours.append((y, x - 2)) 
                
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    X=str(Z)
    orig_stdout = sys.stdout
    f = open('config.txt', 'w')
    sys.stdout = f

    for line in Z:
        for col in line:
            if col == True:
                print('m',end='')
            else:
                print('0',end='')
    
    f.close()    


    with open('config.txt', 'r') as infile:
        s = infile.read()
        s= '\n'.join(s[i:i+width] for i in range(0, len(s), width))
    
    # Write the file out again
    with open('maze.txt', 'w') as file:
        file.write(s)
        file.close()

    return Z

#maze(15,15)


