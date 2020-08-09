import Coordenadas
#Todos estos datos son para el mapa del parque de Mendoza

#Definir camino en el mapa
def pathMendoza():
    
    x = list()
    y = list()
    
    x,y = Coordenadas.lineaHorizontal(13,52,x,y,6)
    x,y = Coordenadas.asignarValores(x,y,7,[13,14,29,35,36,44,45,52])
    x,y = Coordenadas.asignarValores(x,y,8,[13,14,43,52])
    x,y = Coordenadas.lineaHorizontal(29,36,x,y,8)
    x,y = Coordenadas.asignarValores(x,y,9,[13,15,29,36,42,52])
    x,y = Coordenadas.asignarValores(x,y,10,[13,16,29,36,41,52])
    x,y = Coordenadas.asignarValores(x,y,11,[13,17,29,36,40,52])
    x,y = Coordenadas.asignarValores(x,y,12,[13,18,19,20,29,36,40,52])
    x,y = Coordenadas.asignarValores(x,y,13,[13,29,36,40,52])
    x,y = Coordenadas.lineaHorizontal(19,25,x,y,13)
    x,y = Coordenadas.asignarValores(x,y,14,[13,29,36,40,52])
    x,y = Coordenadas.lineaHorizontal(21,25,x,y,14)
    x,y = Coordenadas.lineaHorizontal(21,25,x,y,15)
    x,y = Coordenadas.asignarValores(x,y,15,[13,24,29,36,40,52])
    x,y = Coordenadas.lineaVertical(16,48,x,y,13)
    x,y = Coordenadas.lineaVertical(16,48,x,y,52)
    x,y = Coordenadas.lineaHorizontal(13,52,x,y,49)
    x,y = Coordenadas.lineaHorizontal(13,24,x,y,26)
    x,y = Coordenadas.lineaHorizontal(41,51,x,y,26)
    x,y = Coordenadas.lineaHorizontal(23,41,x,y,17)
    x,y = Coordenadas.lineaHorizontal(23,41,x,y,18)
    x,y = Coordenadas.lineaHorizontal(24,41,x,y,38)
    x,y = Coordenadas.asignarValores(x,y,16,[24,29,36,40])
    x,y = Coordenadas.lineaVertical(19,38,x,y,23)
    x,y = Coordenadas.lineaVertical(19,38,x,y,24)
    x,y = Coordenadas.lineaVertical(19,38,x,y,41)
    x,y = Coordenadas.lineaVertical(28,38,x,y,25)
    x,y = Coordenadas.lineaVertical(28,37,x,y,26)
    x,y = Coordenadas.lineaVertical(38,48,x,y,31)
    x,y = Coordenadas.lineaVertical(38,47,x,y,34)
    x,y = Coordenadas.lineaVertical(33,38,x,y,38)
    x,y = Coordenadas.lineaVertical(33,38,x,y,39)
    x,y = Coordenadas.lineaVertical(34,38,x,y,40)
    x,y = Coordenadas.lineaVertical(34,37,x,y,42)
    x,y = Coordenadas.lineaVertical(34,38,x,y,48)
    x,y = Coordenadas.lineaVertical(32,37,x,y,32)
    x,y = Coordenadas.lineaVertical(32,37,x,y,33)
    x,y = Coordenadas.lineaHorizontal(13,21,x,y,42)
    x,y = Coordenadas.asignarValores(x,y,48,[25,32,33,36,37,45,50,51])
    x,y = Coordenadas.asignarValores(x,y,47,[24,32,33,38,45,49,50,51])
    x,y = Coordenadas.asignarValores(x,y,46,[23,39,46,49])
    x,y = Coordenadas.asignarValores(x,y,18,[42,43,49,50,51])
    x,y = Coordenadas.asignarValores(x,y,45,[22,40,41,46,48])
    x,y = Coordenadas.asignarValores(x,y,44,[20,21,41,42,43,46,47])
    x,y = Coordenadas.asignarValores(x,y,43,[17,18,19,20,21,43,44,46])
    x,y = Coordenadas.asignarValores(x,y,42,[44,45])
    x,y = Coordenadas.asignarValores(x,y,41,[18,19,22,43,45,46])
    x,y = Coordenadas.asignarValores(x,y,40,[17,20,23,42,44,45,46])
    x,y = Coordenadas.asignarValores(x,y,39,[17,21,23,24,41,43,44,46,47])
    x,y = Coordenadas.asignarValores(x,y,38,[16,22,43,47])
    x,y = Coordenadas.asignarValores(x,y,37,[15,31,34])
    x,y = Coordenadas.asignarValores(x,y,36,[14,34])
    x,y = Coordenadas.lineaVertical(33,36,x,y,22)
    x,y = Coordenadas.lineaVertical(34,36,x,y,49)
    x,y = Coordenadas.lineaHorizontal(43,47,x,y,34)
    x,y = Coordenadas.asignarValores(x,y,33,[27])
    x,y = Coordenadas.asignarValores(x,y,32,[29,30,31,34,35])
    x,y = Coordenadas.asignarValores(x,y,31,[28,29,35,36,37])
    x,y = Coordenadas.asignarValores(x,y,30,[28,36,37,39,40])
    x,y = Coordenadas.asignarValores(x,y,29,[27,28,37,38,39,40])
    x,y = Coordenadas.asignarValores(x,y,28,[14,15,27,28,37,38,39,40])
    x,y = Coordenadas.asignarValores(x,y,27,[14,15,38])
    
    return x,y

#Definir las coordenadas iniciales de las filas y columnas    
def columnas1():
    columnas1 = [1,14,28,41,55,69,82,96,110,123,137,151,164,178,192,205,219,233,246,260,274,287,301,315,328,342,356,369,383,  397,410,424,438,451,465,479,492,506,520,533,547,561,574,588,602,615,629,643,656,670]
    return columnas1

def filas1():
    filas1 = [1,16,31,46,62,77,92,107,123,138,153,169,184,199,214,230,245,260,276,291,306,321,337,352,367,383,398,413,428,444,459,474, 490,505,520,535, 551,566,581,597,612,627,642,658,673,688,704,719,734,749,765,780,795,811,826,841,856,872,887,902,918,933,948,963,979,994,1009]
    return filas1

    
 
