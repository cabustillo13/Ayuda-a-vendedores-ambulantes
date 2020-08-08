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
    
def columnas1():
    columnas1 = [1,14,28,41,55,69,82,96,110,123,137,151,164,178,192,205,219,233,246,260,274,287,301,315,328,342,356,369,383,  397,410,424,438,451,465,479,492,506,520,533,547,561,574,588,602,615,629,643,656,670]
    return columnas1

def filas1():
    filas1 = [1,16,31,46,62,77,92,107,123,138,153,169,184,199,214,230,245,260,276,291,306,321,337,352,367,383,398,413,428,444,459,474, 490,505,520,535, 551,566,581,597,612,627,642,658,673,688,704,719,734,749,765,780,795,811,826,841,856,872,887,902,918,933,948,963,979,994,1009]
    return filas1

#Obtener la cantidad de rectangulos que hay en una grilla de imagenes
def crearCuadricula(filas,columnas):
    
    #Generalmente filas, columnas = 50,50
    matriz = [[0] * filas for i in range(columnas)]
    
    return matriz

#Representar los obstaculos en la matriz
def obstaculo(fila,columna,matriz):
    
    matriz[fila][columna]=1
    
    return matriz

def coordenadaInicial(fila,columna):
        
    filas = filas1()
    columnas = columnas1()
    
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
    
