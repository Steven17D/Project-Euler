""" #28 Number spiral diagonals"""

import numpy

size = 1001
Nx=size; Ny=size
matrix= numpy.zeros((Nx,Ny)).tolist()
x, y = size/2, size/2
v = 'r'

def update():
    global x, y, v
    if v == 'r':
        if matrix[x][y+1] != 0:
            x += 1
        else:
            y += 1
            v = 'd'
    elif v == 'd':
        if matrix[x-1][y] != 0:
            y += 1
        else:
            x -= 1
            v = 'l'
    elif v == 'l':
        if matrix[x][y-1] != 0:
            x -= 1
        else:
            y -= 1
            v = 'u'
    elif v == 'u':
        if matrix[x+1][y] != 0:
            y -= 1
        else:
            x += 1
            v = 'r'

for d in range(1,size**2+1):
    matrix[x][y] = d
    update()

sum = 0

for i in range(size):
    sum += matrix[i][i] + matrix[i][size-i -1]

print sum - 1

