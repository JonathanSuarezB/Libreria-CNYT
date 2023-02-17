# Libreria-CNYT
Libreria de funciones para vectores y matrices.

### Instalación 🔧

_Para la instalación y ejecución del entorno de desarrollo se necesita una consola que maneje codigo Python 3_

_Para ello se pueden descargar los siguientes programas_

```
[Python Idle](https://www.python.org/downloads/) - IDLE de Python
[Pycharm](https://www.jetbrains.com/es-es/pycharm/) - IDE de Python
```

_Después, se pueden ejecutar los archivos del repositorio llamando a la función e ingresando los datos._

## Funcionalidad ⚙️

_El programa cuenta con 18 funciones que realizan las siguientes operaciones con vectores y matrices, ademas de un archivo de pruebas:_

##1.Adición de vectores complejos.
##2.Inverso (aditivo) de un vector complejos.
##3.Multiplicación de un escalar por un vector complejo.
##4.Adición de matrices complejas.
##5.Inversa (aditiva) de una matriz compleja.
##6.Multiplicación de un escalar por una matriz compleja.
##7.Transpuesta de una matriz/vector
##8.Conjugada de una matriz/vector
##9.Adjunta (daga) de una matriz/vector
##10.Producto de dos matrices (de tamaños compatibles)
##11.Función para calcular la "acción" de una matriz sobre un vector.
##12.Producto interno de dos vectores
##13.Norma de un vector
##14.Distancia entre dos vectores
##15.Valores  y vectores propios de una matriz
##16.Revisar si una matriz es unitaria
##17.Revisar si una matriz es Hermitiana
##18Producto tensor de dos matrices/vectores
 
##Ejemplo:

    def suma(a, b):
    "Adición de vectores complejos"
    size = len(a)
    suma = [ 0+0j for i in range(size)]
    k = 0
    while k < size:
        suma[k] = a[k] + b[k]
        k = k+1
    return suma

```
La función de adición de numeros complejos: cuenta con dos parametros (a, b), una descripción y una operación.
```

### Las pruebas se pueden encontrar en el archivo **pruebas** ⌨️

## Autores ✒️

* **Jonathan Yesid Suarez Bernal** - *Trabajo y documentacion* 
