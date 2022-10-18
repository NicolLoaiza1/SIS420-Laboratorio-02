#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Loaiza Alvarez Nicol Noelia
# Al ser una busqueda no informada es dificil resolver el problema porque puede colpsar el almacenamiento de la computadora
# Esta busqueda sirve para problemas mas sencillos
class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)

    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self

    def get_hijos(self):
        return self.hijos

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado

    def __str__(self):
        return str(self.get_datos())


# In[25]:


def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    cantidad_digitos = 10
    while resuelto == False and len(nodos_frontera) != 0:
        nodo_actual = nodos_frontera.pop()
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            for h in range(cantidad_digitos-1):
                hijo_datos = nodo_actual.get_datos().copy()
                temp = hijo_datos[h]
# Este if sirve para que los movimientos no almacenen demasiada informacion y se pueda ejecutar todos los digitos ahorrandonos mucho tiempo y procesamiento de la computadora
                if temp == h+1:
                    True
                else:        
                    hijo_datos[h] = hijo_datos[h + 1]
                    hijo_datos[h + 1] = temp
                    hijo = Nodo(hijo_datos)

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)


# In[26]:


import time
if __name__ == '__main__':
    estado_inicial = [7, 6, 5, 4, 3, 2, 1]
    solucion = [1, 2, 3, 4, 5, 6, 7]
    # Sirve para ver el tiempo que se necesita para ejecutar el codigo
    start = time.time()
    nodo_solucion = bpa(estado_inicial, solucion)
    end = time.time()
    print('Tiempo de ejecucion: ', end-start, 'seg') 
    # Mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    # Este for sirve para que los resultados se impriman uno debajo de otro de manera vertical    
    for r in range(len(resultado)):
       print(resultado[r])

