# -*- coding: utf-8 -*- 

class Matrix:
    size_of_matrix = 2
    matrix = [[0 for col in range(size_of_matrix)] for row in range(size_of_matrix)]

    def __init__(a, b, c, d):
        matrix[0][0] = a
        matrix[0][0] = b
        matrix[0][0] = c
        matrix[0][0] = d
    
    def printMatrix(self):
        for i in self.matrix:
            print(i)
