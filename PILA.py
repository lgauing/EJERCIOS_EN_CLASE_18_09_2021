#Nicole Estefania Garcia Chiquito
# Software A1 3 semestre


class Pila_1:
    def __init__(self,tamanio):
        self.lista=[]
        self.size=tamanio
        self.top=0

    def push(self,dato):
        if self.top <self.size:
            self.lista = self.lista + [dato]
            self.top += 1
            return True
        else:
            return False

    def pop(self):
        if self.empty():
            return None
        else:
            top = self.lista[- 1]
            self.lista = self.lista[:-1]
            self.top -= 1
            return top
        
    def show(self):
        for top in range(self.top-1,-1,-1):
            print("[{}]".format(self.lista[top]))
    
    def longitud(self):
        return self.top
        
    def empty(self):
        if self.top == 0:
            return True
        else:
            return False
        
        
"""pila1 = Pila_1(3)
print(pila1.push(8))
print(pila1.push(10))
print(pila1.push(12))
print(pila1.push(4))
print(pila1.push(4))
pila1.show()
print(pila1.longitud())"""