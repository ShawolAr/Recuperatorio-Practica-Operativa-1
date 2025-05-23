

class Equipo:
  __idEquipo:str
  __denominacion:str
  __presidente:str
  __puntos:int
  __golesfavor:int
  __golesontra:int
  __diferenciagoles:int
  
  def __init__(self,idee,denominac,presidente,punto,golesfavor,golescontra,difgoles):
    self.__idEquipo=idee
    self.__denominacion=denominac
    self.__presidente=presidente
    self.__puntos=punto
    self.__golesfavor=golesfavor
    self.__golesontra=golescontra
    self.__diferenciagoles=difgoles
  
  
  def get_denominacion(self):
    return self.__denominacion
  
  def get_idequipo(self):
    return self.__idEquipo
  def get_puntos(self):
    return self.__puntos
  def get_diferenciagoles(self):
    return self.__diferenciagoles
  def get_golesfavor(self):
    return self.__golesfavor
  def get_golescontra(self):
    return self.__golesontra
  
  def set_puntos(self,cant):
    self.__puntos=cant
    
  def __str__(self):
    return f"Id Equipo: {self.__idEquipo}, Denominacion: {self.__denominacion}, Goles a favor: {self.__golesfavor}, Goles en contra: {self.__golesontra}, Diferencia de goles: {self.__diferenciagoles}"
    
  def __gt__(self, other):
        
        if self.__puntos != other.get_puntos:
            return self.__puntos > other.get_puntos()
        
        elif self.__diferenciagoles != other.get_diferenciagoles():
            return self.diferencia_goles > other.get_diferenciagoles()
        
        else:
            return self.__golesfavor> other.get_golesfavor()
  
  
  """1. El equipo que gana un partido (tiene una cantidad de goles mayor que el otro equipo al que
enfrenta), acumula 3 puntos.
2. Cuando empatan (igual cantidad de goles para ambos equipos), se acumula un punto para
cada equipo.
"""
  
  
  
    