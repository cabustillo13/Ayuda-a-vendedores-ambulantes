import Data

#Esta variable global determinara que rectangulos tendran una altura distinta a las demas
columnas = list()
for x in range(17):
    valor = 3*x - 1
    if (x==0): valor = 0
    columnas.append(valor)

#Esta variable global determinara que rectangulos tendran un ancho distinto a las demas
filas = list()
cont=3

for x in range(10):
    x=x+1
    filas.append(7*x)
    filas.append(cont)
    cont=cont+7

#Obtener la cantidad de rectangulos que hay en una grilla de imagenes
def crearCuadricula(filas,columnas):
    
    #Generalmente filas, columnas = 50,50
    matriz = [[1] * filas for i in range(columnas)]
    
    return matriz

#Representar los obstaculos en la matriz
def camino(fila,columna,matriz):
    
    matriz[fila][columna]=0
    
    return matriz

def coordenadaInicial(fila,columna):
        
    filas = Data.filas1()
    columnas = Data.columnas1()
    
    y1 = columnas[columna]
    x1 = filas[fila]
    
    return x1,y1

#Determinar alto de la columna
def hColumna(columna,columnas):
    
    #Devuelve True si la columna se encuentra en columnas
    return (columna in columnas)

#Determinar ancho de la columna
def wFilas(fila,filas):
    
    #Devuelve True si la columna se encuentra en columnas
    return (fila in filas)

#Determinar coordenadas finales de cada rectangulo
def coordenadaFinal(x1,y1,fila,columna):
    
    #Dimensiones de cada rectangulo
    w,h = 13,12
    
    #Los rectangulos pares son mas delgados que los impares
    if (hColumna(columna,columnas) == True): h=11
    
    #Cada 4 rectangulos, ese rectngulo aumenta una unidad su ancho
    if (wFilas(fila,filas) == True): w=14
    
    #Definir coordenadas finales
    x2 = x1 + w
    y2 = y1 + h
    
    return x2, y2

#Definir coordenadas del camino sencillamente marcando un inicio y fin entre dos puntos    
def lineaHorizontal(inicio,fin,x,y,fila):
    
    distancia = (fin - inicio)+1
    
    for i in range(distancia):
        x.append(inicio+i)
        y.append(fila)
        
    return x,y

#Definir coordenadas del camino sencillamente marcando un inicio y fin entre dos puntos    
def lineaVertical(inicio,fin,x,y,columna):
    
    distancia = (fin - inicio)+1
    
    for i in range(distancia):
        x.append(columna)
        y.append(inicio+i)
        
    return x,y

#Definir coordenas a cada fila a partir de una lista de columnas
def asignarValores(x,y,fila,valores):

    for i in range(len(valores)):
        x.append(valores[i])
        y.append(fila)
    
    return x,y

