# Algoritmo A* al servicio de la comunidad
Ayudar a vendedores ambulantes en un parque para llegar a sus clientes de la forma más rápida mediante un Algoritmo A*.

![Vendedor](https://github.com/cabustillo13/Marie/blob/master/Mapas/Vendedor.png)

Somos vendedores a pie, que recorren un parque o una plaza para acercar nuestros productos a nuestros clientes. Es realmente cansado caminar durante ratos largos al rayo del sol en este trabajo. Una manera de lograr llegar de un punto a otro de manera eficiente se puede lograr distintas formas, para este caso se plantea el algoritmo A* o Pathfinder.

## Algoritmo A*

_El algoritmo A* utiliza una función de evaluación **f(n) = g(n) + h′(n)** representa el valor heurístico del nodo a evaluar desde el actual, n, hasta el final, y g(n), el coste real del camino recorrido para llegar a dicho nodo, n, desde el nodo inicial. A* mantiene dos estructuras de datos auxiliares, que podemos denominar abiertos, implementado como una cola de prioridad (ordenada por el valor f(n) de cada nodo), y cerrados, donde se guarda la información de los nodos que ya han sido visitados. En cada paso del algoritmo, se expande el nodo que esté primero en abiertos, y en caso de que no sea un nodo objetivo, calcula la f(n) de todos sus hijos, los inserta en abiertos, y pasa el nodo evaluado a cerrados._

_El algoritmo es una combinación entre búsquedas del tipo primero en anchura con primero en profundidad: mientras que h′(n) tiende a primero en profundidad, g(n) tiende a primero en anchura. De este modo, se cambia de camino de búsqueda cada vez que existen nodos más prometedores._

## ¿Cómo funciona?

Tomé como referencia una imagen aérea de la plaza Independencia ubicada en Ciudad de Mendoza, Argentina. 

![Plaza Independencia](https://github.com/cabustillo13/Marie/blob/master/Mapas/photo0.png)

Con la app para Android "Drawing Grid Maker" realice una cuadrícula sobre la imagen para poder aplicar el algoritmo A* a cada casilla y también para poder visualizarlo gráficamente. 

![Grilla PLaza Independencia](https://github.com/cabustillo13/Marie/blob/master/Mapas/photo2.png)

Uno de los problemas detectados fue que la asignación de las dimensiones de los rectángulos no es constante, así que se tuvo que determinar funciones matemáticas que se adecuaran a cada casilla para posteriormente poder colorearlas adecuadamente y representar el camino adecuado. 

Iniciamos con una matriz que solo contiene "1", ese valor es intepretado en una casilla como un obstáculo. Recordar que la imagen la representamos como una matriz. Posteriormente se definieron los caminos "caminables" dentro de la plaza. Hacer ésto fue un proceso bastante laborioso porque se debe detectar cada casilla donde se puede caminar e ingresar manualmente los valores. Asignamos el valor "0" a cada casilla caminable en la matriz.

![Numeracion Caillas](https://github.com/cabustillo13/Marie/blob/master/Mapas/photo4.png)

![Casillas caminables](https://github.com/cabustillo13/Marie/blob/master/Mapas/photo5.png)

Una vez asignados todos los valores procedemos a marcar el punto inicial y final en el Main.py. Luego al terminar la ejecución mostrará en una imagen: el punto inicial(se representa con una casilla azul), el final(se representa con una casilla roja) y el camino encontrado con el algoritmo A* con casillas verdes.

## Algunas soluciones a distintos puntos de inicio y final.

![Solucion0](https://github.com/cabustillo13/Marie/blob/master/Mapas/Solucion0.png)

![Solucion1](https://github.com/cabustillo13/Marie/blob/master/Mapas/Solucion1.png)

![Solucion2](https://github.com/cabustillo13/Marie/blob/master/Mapas/Solucion2.png)

_**NOTA: Gran parte de la parte derecha de la plaza (prácticamente de la mitad de la imagen) en su momento estaba en reparación y mejora, así que no se podía acceder a esa parte de la plaza. Entonces la ruta aparece en el mapa de forma "caminable" pero para conservar no son considerados en la matriz para conservar la realidad de la reparación. Entonces sí se marca algún punto en esa región el algoritmo A* no encontrará una solución porque no se puede acceder a esos puntos, por más que aparezcan representados en el mapa.**_

## Programas

* **Aestrella.py**

Contiene la función del algoritmo A*.

* **Data.py**

Contiene los datos en crudo de las posiciones caminables en el mapa.

* **Coordenadas.py**

Contiene las funciones para asignar coordenadas en el mapa.

* **Main.py**

Ejecutar este script para correr todo el programa.

## ¿Realmente es aplicable en la vida diaria de un vendedor ambulante?

En el caso ideal que esa persona se mueva constantemente entre esos dos puntos, le puede servir para elegir la ruta más corta y así caminar menos.

En la realidad cuando esta persona se desplace a lo largo de la plaza puede que aparezcan más clientes. Así que habrían distintos puntos inicial y final. Acá lo que se debería hacer es con un algoritmo de Temple Simulado determinar la cantidad de "energía" que hay de recorrer esa lista de puntos. Y con un algoritmo genético determinar cuál sería la mejor forma de ordenar esa lista de puntos en que se encuentran los clientes para poder recorrer una menor distancia y llegar a los clientes. Debido a razones del alto costo temporal de realizar estas implementaciones no lo represente en este programa. 

## ¿Vale la pena aplicar este código a algún parque que tú deseas representar?

No. A menos que realmente lo vayas a utilizar en tu vida diaria, porque es bastante engorroso la forma de cargar los datos de las casillas "caminables". Pero sí estás dispuesto a hacer ésto, bienvenido sea.

**¡Ojalá te sirva este código!**
