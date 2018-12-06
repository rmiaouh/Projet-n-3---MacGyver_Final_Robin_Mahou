import numpy
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import sys
import random
from random import randint

def maze(width=15, height=15, complexity=.75, density=.75):
    # Only odd shapes
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    # number of components
    complexity = int(complexity * (5 * (shape[0] + shape[1])))
    # size of components
    density = int(density * ((shape[0] // 2) * (shape[1] // 2)))
    # Build actual maze
    Z = numpy.zeros(shape, dtype=bool)
    # print(Z)
    # Fill borders
    Z[0, :] = Z[-1, :] = 1
    Z[:, 0] = Z[:, -1] = 1
    # Make aisles
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0,shape[0] // 2) * 2  # pick a random position
        Z[y, x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:
                neighbours.append((y, x - 2))
            if x < shape[1] - 2:
                neighbours.append((y, x + 2))
            if y > 1:
                neighbours.append((y - 2, x))
            if y < shape[0] - 2:
                neighbours.append((y + 2, x))
            if len(neighbours):
                y_, x_ = neighbours[rand(0, len(neighbours) - 1)]
                if Z[y_, x_] == 0:
                    Z[y_, x_] = 1
                    Z[y_ + (y - y_) // 2, x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    Z = Z.tolist()
    j = 0
    for i in range(0, width):
        for j in range(0, height):
            if Z[i][j] == True:
                Z[i][j] = "m"
            else:
                Z[i][j] = "0"
    x = True
    y = True
    counter = 0
    while x == True:
        counter += 1
        y = True
        while y == True:
            rand1 = randint(1, (width)-2)
            rand2 = randint(1, (height)-2)
            if Z[rand1][rand2] == "0":
                if counter == 1:
                    Z[rand1][rand2] = "a"
                    y = False
                if counter == 2:
                    Z[0][0] = "d"
                    Z[0][1] = "0"
                    Z[1][0] = "0"
                    y = False
                if counter == 3:
                    Z[rand1][rand2] = "1"
                    y = False
                if counter == 4:
                    Z[rand1][rand2] = "2"
                    y = False
                if counter == 5:
                    Z[rand1][rand2] = "3"
                    y = False
                    x = False

    with open('mazeFinal.txt', 'w') as f:
        for k in range(0, width):
            text = str(Z[k])
            text = text.replace("[", "")
            text = text.replace("]", "")
            text = text.replace("'", "")
            text = text.replace(",", "")
            text = text.replace(" ", "")
            f.write(text + "\n")
# maze(15,15)
