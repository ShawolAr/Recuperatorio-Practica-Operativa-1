
#Paola Y. Perafan, DNI:37297464, Reg: E-014 - 21.403

from gestorequipos import GestorEquipo
from gestorresultados import GestorResultado


def opcion_1(gestor_1:GestorResultado,gestor_2:GestorEquipo):
  fecha=input("Ingrese la fecha a buscar")
  gestor_1.listar_fechas(fecha,gestor_2)
  
def opcion_2(gestor_2:GestorEquipo,gestor_1: GestorResultado):
  nombre=input("Ingrese nombre equipo: ")
  idlocal=gestor_2.buscar_equipo(nombre)
  gestor_1.listar_equipos(idlocal,nombre,gestor_2)

def opcion_3(gestor_1: GestorResultado,gestor_2: GestorEquipo):
  gestor_1.actualizar_puntos(gestor_2)
  gestor_2.listar_posiciones()
  



def test():
      
        cantidad_resultados=8
        Gestor_1=GestorResultado(cantidad_resultados)
        Gestor_1.cargar_resultado()
        Gestor_2=GestorEquipo()
        Gestor_2.cargar_equipo()
        
        
        while (True):
          opcion=(input("""---------------------------------------------------MENU DE OPCIONES-------------------------------------------------------
                        \n  ------------------------------------ELIJA UNA OPCION ENTRE  'A','B' o 'C' o '0' PARA SALIR-------------------------------------------
                        \na. Ingrese una fecha para imprimir los equipos con sus resultados. Al final del listado el importe recaudado por inscripción de los equipos.
                        \nb. Ingresar un nombre para mostrar los resultados de los partidos que jugo de local, indicando nombre de equipo contrincante y resultado.
                        \nc. Mostar la tabla de posiciones
                        \n0. Salir:
                        \n""").upper())
          if (opcion=="A"):
            opcion_1(Gestor_1,Gestor_2)
            
          elif (opcion=="B"):
            opcion_2(Gestor_2, Gestor_1)
            
          elif (opcion=="C"):
            opcion_3(Gestor_1,Gestor_2)
          
          elif (opcion == "0"):
                return
          else:
            print("Opción inválida")