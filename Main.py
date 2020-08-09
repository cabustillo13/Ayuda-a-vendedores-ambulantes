import Coordenadas, Data, Aestrella, Funciones
import cv2

#Definir Grilla
matriz = Coordenadas.crearCuadricula(50,67)
    
#Definir camino
x,y = Data.pathMendoza()
rango = len(x)

for i in range(rango):
    matriz = Coordenadas.camino(x[i],y[i],matriz)

#Definir condiciones
start = (26, 49)    
end = (13, 39)      
    
if ((start[0] in x) and (start[1] in y) and (end[0] in x) and (end[1]in y)):
    path = Aestrella.aEstrella(matriz, start, end)
    print(path)
else:
    print("Los puntos ingresados no son recorrible/caminables")

#Dibujar path, punto inicial y final
imagen=cv2.imread("./Mapas/photo2.png")

rango = len(path)
for i in range(rango):
    imagen = Funciones.dibujarRectangulo(path[i][0],path[i][1],imagen,(0,256,0))

imagen = Funciones.dibujarRectangulo(start[0],start[1],imagen,(256,0,0))
imagen = Funciones.dibujarRectangulo(end[0],end[1],imagen,(0,0,256))

cv2.imwrite("Solucion.png",imagen)
