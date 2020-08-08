import Coordenadas
import cv2

#Representar el path encontrado con Aestrella
def dibujarRectangulo(fila,columna,image):
    
    #Coordenada Inicial
    x1 , y1 = Coordenadas.coordenadaInicial(fila,columna)
    #Coordenada Final
    x2 , y2 = Coordenadas.coordenadaFinal(x1,y1,fila,columna)
    
    #Definir color RGB del rectangulo 
    color = (0,256,0)
    #Thickness -> Queremos rellenar el recangulo por eso le ponemos -1
    thickness = -1
    #Agregar rectangulo relleno a la imagen
    image = cv2.rectangle(image, (x1,y1),(x2,y2),color,thickness)

    return image

imagen=cv2.imread("./Mapas/Mendoza/photo1.png")

for x in range(67):
    for y in range(50):
        imagen = dibujarRectangulo(x,y,imagen)

cv2.imwrite("prueba.png",imagen)
