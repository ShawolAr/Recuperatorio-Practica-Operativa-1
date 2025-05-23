

from equipo import Equipo
import csv

class GestorEquipo:
  __lista_equipos:list
  
  def __init__(self):
    self.__lista_equipos=[]
    
  def cargar_equipo(self):
    archivo=open("equiposLiguilla.csv",mode="r",encoding="UTF-8")
    lector= csv.reader(archivo,delimiter=";")
    bandera=True
    
    for fila in lector:
      if bandera:
        bandera=False
      else:
        equipo=Equipo(fila[0],fila[1],fila[2],int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]))
        self.__lista_equipos.append(equipo)
    archivo.close
    
  def buscar_denominacion(self,idee):
    encontrado=False
    i=0
    
    while not encontrado:
      if i<len(self.__lista_equipos):
        if (self.__lista_equipos[i].get_idequipo()==idee):
          encontrado=True
          denominacion=self.__lista_equipos[i].get_denominacion()
      i+=1
    return denominacion
  
  def buscar_equipo(self,nombre):
    encontrado=False
    i=0
    idlocal=None
    while  not encontrado:
      if i<len(self.__lista_equipos):
        if self.__lista_equipos[i].get_denominacion()==nombre:
          idlocal=self.__lista_equipos[i].get_idequipo()
          encontrado=True
      i+=1
    return idlocal
  
  def setter_puntos(self,idee,cantidad):
    encontrado=False
    i=0
    
    while  not encontrado:
      if i<len(self.__lista_equipos):
        if self.__lista_equipos[i].get_idequipo()==idee:
          self.__lista_equipos[i].set_puntos(cantidad)
          encontrado=True
      i+=1
    return
  
  def listar_posiciones(self):
        
        i=1
        print(f"\n--- Tabla de Posiciones ---")
        print(f"Posición    Equipo                       Puntos    GF    GC   DG")
        for equipo in sorted (self.__lista_equipos,reverse=True):
          print(f"{i+1}       {equipo.get_denominacion()}                     {equipo.get_puntos()}       {equipo.get_golesfavor()}       {equipo.get_golescontra()}       {equipo.get_diferenciagoles()} ")
          i+=1
    
