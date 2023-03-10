# Libreria - CNYT
Libreria de funciones para vectores y matrices.

### Instalaci贸n 馃敡

_Para la instalaci贸n y ejecuci贸n del entorno de desarrollo se necesita una consola que maneje codigo Python 3_

_Para ello se pueden descargar los siguientes programas_

```
[Python Idle](https://www.python.org/downloads/) - IDLE de Python
[Pycharm](https://www.jetbrains.com/es-es/pycharm/) - IDE de Python
```

_Despu茅s, se pueden ejecutar los archivos del repositorio llamando a la funci贸n e ingresando los datos._

## Funcionalidad 鈿欙笍

_El programa cuenta con 18 funciones que realizan las siguientes operaciones con vectores y matrices:_

## 1.Adici贸n de vectores complejos.
## 2.Inverso (aditivo) de un vector complejos.
## 3.Multiplicaci贸n de un escalar por un vector complejo.
## 4.Adici贸n de matrices complejas.
## 5.Inversa (aditiva) de una matriz compleja.
## 6.Multiplicaci贸n de un escalar por una matriz compleja.
## 7.Transpuesta de una matriz/vector
## 8.Conjugada de una matriz/vector
## 9.Adjunta (daga) de una matriz/vector
## 10.Producto de dos matrices (de tama帽os compatibles)
## 11.Funci贸n para calcular la "acci贸n" de una matriz sobre un vector.
## 12.Producto interno de dos vectores
## 13.Norma de un vector
## 14.Distancia entre dos vectores
## 15.Valores  y vectores propios de una matriz
## 16.Revisar si una matriz es unitaria
## 17.Revisar si una matriz es Hermitiana
## 18.Producto tensor de dos matrices/vectores
 
## Ejemplo:

    def suma(a, b):
    "Adici贸n de vectores complejos"
    size = len(a)
    suma = [ 0+0j for i in range(size)]
    k = 0
    while k < size:
        suma[k] = a[k] + b[k]
        k = k+1
    return suma

```
La funci贸n adici贸n de numeros complejos: cuenta con dos parametros(a, b), una descripci贸n y una operaci贸n.
```

### Las pruebas se pueden encontrar en el archivo **pruebas** 鈱笍

## Autores 鉁掞笍

* **Jonathan Yesid Suarez Bernal** - *Trabajo y documentaci贸n* 
