#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def fprima(x,y):
    """Deriva de una función

    Examples:
        >>> fprima(x,y)
        x+y

    Args:
        x (float): Entrada x de la función
        y (float): Entrada y de la función

    Returns:
        float: Retorna el resultado de la función que se haya defino colocando esos valores

    """
    return x+y

def euler(x0, xf, f, ite):
    """Método numérico para calcular una función

    Example:
        >>> euler(0,2, fprima,40)
        resultado

    Args:
    x0 (float) : Es el x inicial
    xf (float) : Es el x final
    fprima (func) : Es lo que dicta como es la derivada
    ite (integer) : La cantidad de iteraciones del for

    Returns:
        Array: Retorna un arreglo con todos los puntos y calculados en la matriz resultado
    """

    h = (xf-x0)/ite
    resultado = np.zeros(ite)
    resultado[0] = x0
    for i in range(1,ite):
        resultado[i] = resultado[i-1] + h*f(x0 + (i-1)*h,resultado[i-1])
    return resultado

def rk2(x0, xf, f, ite):
    """Método numérico para calcular una función

    Example:
         >>> rk2(0,2, fprima,40)
        resultado1

    Args:
        x0 (float) : Es el x inicial
        xf (float) : Es el x final
        fprima (func) : Es lo que dicta como es la derivada
        ite (integer) : La cantidad de iteraciones del for

    Returns:
        array: Retorna una arreglo con todos los puntos yn calculado en resultado1
    """
    h = (xf-x0)/ite
    resultado1 = np.zeros(ite)
    resultado1[0] =  x0
    for i in range(1, ite):
        k1 = h*f(x0 + (i-h)*h, resultado1[i-1])
        k2 = h*f(x0 + i*h, resultado1[i-1] +k1)
        resultado1[i] = resultado1[i-1] +1/2*(k1+k2)
    return resultado1

def rk4(x0,xf, f, ite):
    """Método numérico para calcular una función

    Example:
        >>> rk4(0,2, fprima,40)
        resultado2

    Args:
    x0 (float) : Es el x inicial
    xf (float) : Es el x final
    fprima (func) : Es lo que dicta como es la derivada
    ite (integer) : La cantidad de iteraciones del for

    Returns:
        array: Retorna una arreglo con todos los puntos yn calculados en resultado2
    """
    h = (xf-x0)/ite
    resultado2 = np.zeros(ite)
    resultado2[0] = x0
    for i in range(1,ite):
        k1 = h*f(x0 + (i-1)*h, resultado2[i-1])
        k2 = h*f(x0 + (i-0.5)*h, resultado2[i-1] +k1/2)
        k3 = h*f(x0 + (i-0.5)*h, resultado2[i-1] +k2/2)
        k4 = h*f(x0 + i*h, resultado2[i-1] +k3)
        resultado2[i] = resultado2[i-1] + 1/6*(k1+2*k2+2*k3+k4)
    return resultado2

x0 = 0
xf = 2
ite = 40
x = np.linspace(x0,xf,ite)
euler = euler(x0, xf, fprima, ite)
rk2 = rk2(x0,xf,fprima, ite)
rk4 = rk4(x0,xf, fprima, ite)

plt.plot(x,euler)
plt.show()
