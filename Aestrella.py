import Coordenadas, Data

class Node():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        #g -> Es la distancia entre el nodo actual y el nodo de inicio.
        self.g = 0
        #h -> Es la heuristica: Distancia estimada desde el nodo actual hasta el nodo final.
        self.h = 0
        #f -> Es el costo total del nodo
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def aEstrella(maze, start, end):

    #Crear un nodo inicial y final
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    #Inicializar ambas listas
    open_list = []
    closed_list = []

    #Agregar el nodo inicial
    open_list.append(start_node)

    #Realizar un Loop hasta alcanzar el nodo final
    while len(open_list) > 0:

        #Obtener el nodo actual
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        #Quitar nodo de la lista abierta y pasa a la lista cerrada
        open_list.pop(current_index)
        closed_list.append(current_node)

        #Encontrar el objetivo
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] #Devuelve el path inverso

        #Generar los hijos
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: #Cuadrados Adyacentes

            #Obtener la posicion del nodo
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            #Asegurarse que esta dentro del rango
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            #Asegurse que esta en un lugar donde pueda caminar (osea que sean ceros en la matriz)
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            #Crear un nuevo nodo
            new_node = Node(current_node, node_position)

            #Append
            children.append(new_node)

        # Loop a traves de los nodos hijo
        for child in children:

            #El nodo hijo esta en la lista closed
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            #Definir los valores de f, g, y h 
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            #El nodo hijo ya esta en la lista open
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            #Agregar el nodo hijo a la lista open
            open_list.append(child)


#Bibliografia: https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
