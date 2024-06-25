#Introdución

Se va a describir los métodos de Euler, RK2 (Runge-Kutta de segundo orden) y RK4 ( Runge-Kutta de cuarto orden), y se comenzará a describir en el orden mencionado.

Metodo de Euler

En este metodo, el cual es numérico, se usa un concepto parecido al de Newton-Raphson, en el que se podía aproximar los ceros de una función mediante un x inicial y la división entre la función de interés entre su respectiva derivada evaluada en el mismo punto, y el punto dado se volvía a evaluar, realizando iteraciones deseadas hasta minimizar el error.

Pero, en este método es diferente una parte, y es que este punto en cada iteracion calcula un numero, generando un conjunto de numeros que corresponden a una coordenada, llamese 'y', esto mediante el x inicial, el x final, cierta cantidad de iteraciones y un paso dado por h, que es la diferencia entre x final e x inicial dividida por la cantidad de iteraciones (Se habla de iteraciones por la parte de programación)

Todo lo anterior se resume en la siguiente formula:
* $ y(i) = x0 + hf(x0+ih, y(i-1)$

Metodo de RK2 (Runge-Kutta de segundo orden) El método RK2 es otra herramienta númerica para resolver ODE's, y es una generalización del método de Euler, ya anteriormente visto. Este calcula un k1, que es una parte de una pendiente, en el punto inicial f(x0+i*h, yi), lo cual aproxima la pendiente en un punto. Luego de esto se calcula un k2, que vendria siendo sumarle h a la x y a la y de la funcion, para dar un ajuste a la pendiente, luego estos dos se suman y se multplican por h/2 y se le suma
el yn de la iteración actual. Todo esto se resume en lo siguiente:

* $k1 = hf(x0 + (i-1)h, y(i-1))$
* $k2 = hf(x0 +ih, y(i-1) +k1)$
* $y(i) = y(i-1) +\frac{k1+k2}{2}\


Metodo de RK4 (Runge-Kutta de cuarto orden) 
Este metodo usa una idea similar que en el metodo RK2, definiendo a 4 diferentes k de la siguiente manera, ademas de la ecuacion a seguir en el código para poder realizar el calculo de todos los puntos 
* $k1 = hf(x0+i*h, yn)$,
* $k2 = hf\left(x0 + (i-h)h, y(i-1)+\frac{k1}{2}\right)$,
* $k3 = hf\left(x0 + (i-0.5)h, y(i-1)+\frac{k3}{2}\right)$,
* $k4 = hf\left(x0 + k4, y(i-1) + k3 \right)$,
* $y(i) = y(i-1) + \frac{h}{6}(k1 + 2 k2 + 2k3 + k4)$.
 ::: ode

