import Coordenadas, Data
import cv2

#Representar el path encontrado con Aestrella
def dibujarRectangulo(fila,columna,image,color):
    
    #Coordenada Inicial
    x1 , y1 = Coordenadas.coordenadaInicial(fila,columna)
    #Coordenada Final
    x2 , y2 = Coordenadas.coordenadaFinal(x1,y1,fila,columna)
    
    #Thickness -> Queremos rellenar el recangulo por eso le ponemos -1
    thickness = -1
    #Agregar rectangulo relleno a la imagen
    image = cv2.rectangle(image, (x1,y1),(x2,y2),color,thickness)

    return image

def dibujarRegla(fila,columna,image,numero):
    
    #Coordenada Inicial
    x1 , y1 = Coordenadas.coordenadaInicial(fila,columna)
    #Coordenada Final
    x2 , y2 = Coordenadas.coordenadaFinal(x1,y1,fila,columna)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.3
    
    if (fila==0):
        color = (0,255,0)       #Color Verde
    else: 
        color = (255, 0, 0)     #Color Azul
    
    thickness = 1
    
    x = x1
    y = y1-1
    
    image = cv2.putText(image, str(numero), (x,y), font,fontScale, color, thickness, cv2.LINE_AA) 
    return image

#Test corroborar posiciones del mapa
#x,y = Data.pathMendoza()
#rango = len(x)
#imagen=cv2.imread("./Mapas/photo2.png")
#for i in range(rango):
    #imagen = dibujarRectangulo(x[i],y[i],imagen,(0,256,0))
#cv2.imwrite("prueba1.png",imagen)

#Test definir grilla y enumerar cada casilla
#imagen=cv2.imread("./Mapas/photo3.png")
#for x in range(67):
    #for y in range(50):
        ##imagen = dibujarRectangulo(x,y,imagen)
        #if (x==0):
            #imagen = dibujarRegla(x,y,imagen,y)
        #else:
            #imagen = dibujarRegla(x,y,imagen,x)

#cv2.imwrite("prueba.png",imagen)

