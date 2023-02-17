import cmath
import math
import numpy
import numpy as np
from numpy import linalg as LA

def suma(a, b):
    "Adición de vectores complejos"
    size = len(a)
    suma = [ 0+0j for i in range(size)]
    k = 0
    while k < size:
        suma[k] = a[k] + b[k]
        k = k+1
    return suma

def resta(a, b):
    "Sustracción de vectores complejos"
    size = len(a)
    resta = [ 0+0 for i in range(size)]
    k = 0
    while k < size:
        resta[k] = a[k] - b[k]
        k = k+1
    return resta

def inverso(a):
    "Inverso (aditivo) de un vector complejos."
    size = len(a)
    inverso = [ 0+0j for i in range(size)]
    k = 0
    while k < size:
        inverso[k] = -a[k]
        k = k+1
    return inverso

def multEscalar(c, a):
    "Multiplicación de un escalar por un vector complejo."
    size = len(a)
    mult = [ 0+0j for i in range(size)]
    k = 0
    while k < size:
        mult[k] = c*a[k]
        k = k+1
    return mult

def sumaMat(a, b):
    "Adición de matrices complejas."
    filas = len(a)
    columnas = len(b[0])
    suma = [[0+0j for columnas in range(columnas)]for fila in range(filas)]
    for i in range (0,filas):
        for j in range (0,columnas):
            suma[i][j] = a[i][j] + b[i][j]
    return suma

def inversaMat(a):
    "Inversa (aditiva) de una matriz compleja."
    filas = len(a)
    columnas = len(a[0])
    inverso = [[0+0j for columnas in range(columnas)]for fila in range(filas)]
    for i in range (0,filas):
        for j in range (0,columnas):
            inverso[i][j] = -a[i][j]
    return inverso

def multMat(c, a):
    "Multiplicación de un escalar por una matriz compleja."
    filas = len(a)
    columnas = len(a[0])
    mult = [[0+0j for columnas in range(columnas)]for fila in range(filas)]
    for i in range(0, filas):
        for j in range(0, columnas):
            mult[i][j] = c*a[i][j]
    return mult

def transpuestaMat(a):
    "Transpuesta de una matriz"
    filas = len(a)
    columnas = len(a[0])
    transpuesta = [[0 + 0j for columnas in range(columnas)] for fila in range(filas)]
    for i in range(0, filas):
        for j in range(0, columnas):
            transpuesta[i][j] = a[j][i]
    return transpuesta

def conjugadaMat(a):
    "Conjugada de una matriz"
    filas = len(a)
    columnas = len(a[0])
    conjugada = [[0 + 0j for columnas in range(columnas)] for fila in range(filas)]
    for i in range(0, filas):
        for j in range(0, columnas):
            conjugada[i][j] = a[i][j].conjugate()
    return conjugada

def adjuntaMat(a):
    "Adjunta (daga) de una matriz"
    a = transpuestaMat(a)
    a = conjugadaMat(a)
    return a

def productoMat(a, b):
    "Producto de dos matrices (de tamaños compatibles)"
    filas_a = len(a)
    filas_b = len(b)
    columnas_a = len(a[0])
    columnas_b = len(b[0])
    if columnas_a != filas_b:
        return None
    producto = []
    for i in range(filas_b):
        producto.append([])
        for j in range(columnas_b):
            producto[i].append(None)
    for c in range(columnas_b):
        for i in range(filas_a):
            suma = 0
            for j in range(columnas_a):
                suma += a[i][j]*b[j][c]
            producto[i][c] = suma
    return producto

def internoVec(a, b):
    "Producto interno de dos vectores"
    interno = 0
    for i in range(0, len(a)):
        interno = interno + (a[i] * b[i])
    return interno

def normaVec(a):
    "Norma de un vector"
    norma = 0
    for i in range(0, len(a)):
        norma = norma + (a[i]**2)
    norma = math.sqrt(norma)
    return norma

def distanciaVec(a, b):
    "Distancia entre dos vectores"
    distancia = resta(a, b)
    distancia = normaVec(distancia)
    return distancia

def propios(a):
    "Valores  y vectores propios de una matriz"
    return LA.eig(a)

def unitaria(a):
    "Revisa si una matriz es unitaria"
    adjunta = adjuntaMat(a)
    if productoMat(a, adjunta) == productoMat(adjunta,a):
        return True
    else:
        return False

def hermitiana(a):
    "Revisa si una matriz es Hermitiana"
    adjunta = adjuntaMat(a)
    if a == adjunta:
        return True
    else:
        return False

def productoTensor(a, b):
    "Producto tensor de dos matrices"
    m1 = len(a)
    n1 = len(b)
    m2 = len(a[0])
    n2 = len(b[0])
    filas = m1*n1
    columnas = m2*n2
    respuesta = [[0 for columnas in range(columnas)] for filas in range(filas)]
    for j in range (0, filas):
        for k in range (0, columnas):
            respuesta[j][k] = a[(j//n1)][k//n2] * b[j%n1][k%n2]
