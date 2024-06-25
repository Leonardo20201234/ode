# Introducción

Se van a describir los métodos de Euler, RK2 (Runge-Kutta de segundo orden) y RK4 (Runge-Kutta de cuarto orden), y se comenzará a describir en el orden mencionado.

## Método de Euler

En este método, el cual es numérico, se usa un concepto parecido al de Newton-Raphson, en el que se podían aproximar los ceros de una función mediante un \( x \) inicial y la división entre la función de interés y su respectiva derivada evaluada en el mismo punto. Luego, el punto dado se volvía a evaluar, realizando las iteraciones deseadas hasta minimizar el error.

Sin embargo, en este método hay una diferencia, y es que en cada iteración se calcula un número, generando un conjunto de números que corresponden a una coordenada, llamada 'y'. Esto se hace mediante el \( x \) inicial, el \( x \) final, cierta cantidad de iteraciones y un paso dado por \( h \), que es la diferencia entre \( x \) final e \( x \) inicial dividida por la cantidad de iteraciones (Se habla de iteraciones desde la perspectiva de la programación).

Todo lo anterior se resume en la siguiente fórmula:
\[ y(i) = y(i-1) + hf(x_0 + ih, y(i-1)) \]

## Método de RK2 (Runge-Kutta de segundo orden)

El método RK2 es otra herramienta numérica para resolver ecuaciones diferenciales ordinarias (ODEs), y es una generalización del método de Euler. Este calcula un \( k_1 \), que es una parte de una pendiente, en el punto inicial \( f(x_0 + i*h, y_i) \), lo cual aproxima la pendiente en un punto. Luego de esto se calcula un \( k_2 \), que consiste en sumar \( h \) a la \( x \) y a la \( y \) de la función, para dar un ajuste a la pendiente. Luego estos dos se suman, se multiplican por \( h/2 \) y se le suma al \( y_n \) de la iteración actual. Todo esto se resume en lo siguiente:

\[ k_1 = h f(x_0 + (i-1)h, y(i-1)) \]
\[ k_2 = h f(x_0 + ih, y(i-1) + k_1) \]
\[ y(i) = y(i-1) + \frac{k_1 + k_2}{2} \]

## Método de RK4 (Runge-Kutta de cuarto orden)

Este método usa una idea similar al método RK2, definiendo 4 diferentes \( k \) de la siguiente manera, además de la ecuación a seguir en el código para poder realizar el cálculo de todos los puntos:

\[ k_1 = h f(x_0 + i*h, y_n) \]
\[ k_2 = h f \left(x_0 + (i - \frac{1}{2})h, y(i-1) + \frac{k_1}{2} \right) \]
\[ k_3 = h f \left(x_0 + (i - \frac{1}{2})h, y(i-1) + \frac{k_2}{2} \right) \]
\[ k_4 = h f \left(x_0 + ih, y(i-1) + k_3 \right) \]
\[ y(i) = y(i-1) + \frac{h}{6} (k_1 + 2k_2 + 2k_3 + k_4) \]
