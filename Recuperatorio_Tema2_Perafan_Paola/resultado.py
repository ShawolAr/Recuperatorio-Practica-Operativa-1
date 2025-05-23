

class Resultado:
  __fecha:str
  __idEquipoLocal:str
  __golesLocal:int
  __idEquipoVisitante:str
  __golesVisitante:int
  __inscripcion=45000
  
  
  def __init__(self,fecha,idee,goleslocal,ideevisitante,golesvisita):
    self.__fecha=fecha
    self.__idEquipoLocal=idee
    self.__golesLocal=goleslocal
    self.__idEquipoVisitante=ideevisitante
    self.__golesVisitante=golesvisita
    
  def get_fecha(self):
    return self.__fecha
  
  def get_idelocal(self):
    return self.__idEquipoLocal
  
  def get_idevisitante(self):
    return self.__idEquipoVisitante
  
  def get_gollocal(self):
    return self.__golesLocal
  
  def get_golvisita(self):
    return self.__golesVisitante
  
  def __str__(self):
    return f"Fecha: {self.__fecha}, Id Equipo Local: {self.__idEquipoLocal}, Id Equipo Visitante: {self.__idEquipoVisitante}, Goles visitante: {self.__golesVisitante}, Goles Local: {self.__golesLocal}"
  

  
  
  @classmethod

  def get_importe(cls):
    return cls.__inscripcion



  