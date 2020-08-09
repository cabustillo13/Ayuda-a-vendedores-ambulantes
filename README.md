# Marie
Ayudar a vendedores ambulantes en un parque para llegar a sus clientes de la forma más rápida mediante un Algoritmo A*.

![Vendedor](https://github.com/cabustillo13/Marie/blob/master/Mapas/Vendedor.png)

Somos vendedores a pie, que recorren un parque o una plaza para acercar nuestros productos a nuestros clientes. Es realmente cansado caminar durante ratos largos al rayo del sol en este trabajo. Una manera de lograr llegar de un punto a otro de manera eficiente se puede lograr distintas formas, para este caso se plantea el algoritmo A* o Pathfinder.

# Algoritmo A*

_El algoritmo A* utiliza una función de evaluación **f(n) = g(n) + h′(n)** representa el valor heurístico del nodo a evaluar desde el actual, n, hasta el final, y g(n), el coste real del camino recorrido para llegar a dicho nodo, n, desde el nodo inicial. A* mantiene dos estructuras de datos auxiliares, que podemos denominar abiertos, implementado como una cola de prioridad (ordenada por el valor f(n) de cada nodo), y cerrados, donde se guarda la información de los nodos que ya han sido visitados. En cada paso del algoritmo, se expande el nodo que esté primero en abiertos, y en caso de que no sea un nodo objetivo, calcula la f(n) de todos sus hijos, los inserta en abiertos, y pasa el nodo evaluado a cerrados._

_El algoritmo es una combinación entre búsquedas del tipo primero en anchura con primero en profundidad: mientras que h′(n) tiende a primero en profundidad, g(n) tiende a primero en anchura. De este modo, se cambia de camino de búsqueda cada vez que existen nodos más prometedores._
