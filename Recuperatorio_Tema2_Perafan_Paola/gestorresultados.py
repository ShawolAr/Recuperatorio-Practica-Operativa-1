
from resultado import Resultado
from gestorequipos import GestorEquipo
import numpy as np
import csv

class GestorResultado:
  __arre:None
  __capacidad_real:int
  __cantidad_resultados:int
  
  def __init__(self,capacidad):
    self.__capacidad_real=capacidad
    self.__arre=np.empty(self.__capacidad_real,dtype=Resultado)
    self.__cantidad_resultados=0
    
  def agregar_resultado(self,nuevo:Resultado):
    if self.__cantidad_resultados==self.__capacidad_real:
      self.__capacidad_real+=5
      
      temp_arre=np.empty(self.__capacidad_real,dtype=Resultado)
      for i in range (self.__cantidad_resultados):
        temp_arre[i]=self.__arre[i]
      self.__arre=temp_arre
    self.__arre[self.__cantidad_resultados]=nuevo
    self.__cantidad_resultados+=1
    
  def cargar_resultado(self):
    archivo=open("resultadosLiguilla.csv",mode="r",encoding="UTF-8")
    lector= csv.reader(archivo,delimiter=";")
    bandera=True
    
    for fila in lector:
      if bandera:
        bandera=False
      else:
        resultado=Resultado(fila[0],fila[1],int(fila[2]),fila[3],int(fila[4]))
        self.agregar_resultado(resultado)
    archivo.close()
    
    
  def listar_fechas (self,fecha,gestor_1: GestorEquipo):
    importe=0
    
    for resultados in self.__arre:
      if isinstance(resultados, Resultado) and resultados.get_fecha() == fecha:
          idlocal=resultados.get_idelocal()
          idevisitante=resultados.get_idevisitante()
          goleslocal=resultados.get_gollocal()
          golesvisita=resultados.get_golvisita()
          denominacionlocal=gestor_1.buscar_denominacion(idlocal)
          denominacionvisitante=gestor_1.buscar_denominacion(idevisitante)
          
          importe+=(int(Resultado.get_importe())*2)
          print (f"Fecha jugada: {fecha}")
          print (f"\n---El equipo local fue: {denominacionlocal}. Anoto {goleslocal} goles. El equipo visitante fue: {denominacionvisitante}. Anoto {golesvisita} goles. ---- ")
    print(f"El importe recaudado en esta fecha por los equipos fue: {importe}") 
    
  def listar_equipos(self, idlocal,nombre,gestorequipos:GestorEquipo):
    
    for resultado in self.__arre:
      if isinstance(resultado, Resultado) and resultado.get_idelocal() == idlocal:
        print (f"Resultados de local:")
        print (f"Equipo: {nombre}")
        print (f"Tiene {resultado.get_gollocal()} goles de local")
        denominacionvisitante=gestorequipos.buscar_denominacion(resultado.get_idevisitante())
        print(f"Jugo contra el {denominacionvisitante}")
        if int(resultado.get_golvisita())<int(resultado.get_gollocal()):
          print (f"Y gano.")
        else:
          print (f"Y perdio.")
          
          
    
        
  def actualizar_puntos(self,gestorequipos: GestorEquipo):
    
    for i in range (self.__cantidad_resultados):
      idequipo=self.__arre[i].get_idelocal()
      idequipovisita=self.__arre[i].get_idevisitante()
      if int(self.__arre[i].get_gollocal()) > int(self.__arre[i].get_golvisita()):
         
        gestorequipos.setter_puntos(idequipo,3)
      elif  int(int(self.__arre[i].get_golvisita()) > self.__arre[i].get_gollocal()):
        gestorequipos.setter_puntos(idequipovisita,3)
      else:  
            gestorequipos.setter_puntos(idequipo,1)
            gestorequipos.setter_puntos(idequipovisita,1)
    return
  
  
      
  
  
    
          
  