#Nombre: Nicole Estefania Garcia Chiquito
#3er semestre de Software A1
# 20 de Agosto del 2021
class Matriz:
    def __init__(self,matriz,fila,columna):
        self.matriz = matriz
        self.fila = fila
        self.columna = columna
        
    def ingresar(self,dato):
        self.matriz = []
        for fila in range (self.fila):
            columnas= []
            for col in range(self.columna):
                valor= input("Fila [{}] Col [{}]:".format(fila,col))
                columnas.append(valor)
            self.matriz.append(columnas)
    
    def presentar(self):
        for fila in range(len(self.matriz)):
            # print(numeros[fila])
            # print(len(self.matriz[fila]))
            for col in range (len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]), end = " ")
            print()
            
    def buscar(self,valor):
       pass
        
        
    def sumar(self,matriz1, matriz2):
        pass
        
        
    
            
        
        
        # for fila in range(len(self.matriz)):
        #     if fila == valor:
        #         return self.matriz[fila]
        # for col in range (len(self.matriz[fila])):
        #     if col == valor:
        #         return self.matriz[col]
        
        # for pos,ele in enumerate(self.matriz):
        #     for pos, ele in enumerate(self.matriz[ele]):
        #         if ele == valor: 

        
    


numeros = [[10,20],[60,80]]
numeros2 = [[10,20],[60,80]]

# col = numeros[0]
# print(col[1])
# print(numeros[0],numeros[0][1])
# print(col,col[1])
# print(col[0])
# print(numeros[1][0])
# print(numeros[2][0])

# for i in numeros:
#     print(i)

mat=Matriz(numeros,2,2)

mat.sumar(mat)
# mat.presentar()