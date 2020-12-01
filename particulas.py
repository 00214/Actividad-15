from particula import Particula
import json
from pprint import pprint
from pprint import pformat

# Administrador de Particulas

class Particulas:
    def __init__(self):
        self.__particulas = [] # Lista
    
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + "\n" for particula in self.__particulas
        )

    def dictionary(self):
        dictionary = dict()
    
        for particula in self.__particulas:
            key = particula.origen_x, particula.origen_y 
            value = particula.destino_x, particula.destino_y, particula.distancia
            key_2 = particula.destino_x, particula.destino_y
            value_2 = particula.origen_x, particula.origen_y, particula.distancia
            if key in dictionary:
                dictionary[key].append(value)
            else:
                dictionary[key] = [value]
            if key_2 in dictionary:
                dictionary[key_2].append(value_2)
            else:
                dictionary[key_2] = [value_2]
        str = pformat(dictionary, width=40, indent=1)
        return str
    
    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.contador = 0

        return self
    
    def __next__(self):
        if self.contador < len(self.__particulas):
            particula = self.__particulas[self.contador]
            self.contador += 1
            return particula
        else:
            raise StopIteration
    
    def guardar(self, ubicacion):
        try:
            with open(ubicacion, "w") as archivo:
                Lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(Lista, archivo, indent=5)
            return 1
        except:
            return 0
    
    def abrir(self, ubicacion):
        try:
            with open(ubicacion, "r") as archivo:
                Lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in Lista]
            return 1
        except:
            return 0