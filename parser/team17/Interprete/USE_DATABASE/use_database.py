from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from StoreManager import jsonMode as j

#####################################
# Patrón intérprete: CREATE DATABASE#
#####################################

# CREATE DATABASE: crear una base de datos


class UseDatabase(NodoArbol):

    def __init__(self, id_):
        self.id = id_

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):
        if self.exist(self.id) is True:
            entorno.setBD(self.id)
            arbol.console.append('tytus> Trabajando en: \'' + self.id + '\'')
            print('tytus> Trabajando en: \'' + self.id + '\'')
        else:
            '''
            			  ______ _____  _____   ____  _____  
            			 |  ____|  __ \|  __ \ / __ \|  __ \ 
            			 | |__  | |__) | |__) | |  | | |__) |
            			 |  __| |  _  /|  _  /| |  | |  _  / 
            			 | |____| | \ \| | \ \| |__| | | \ \ 
            			 |______|_|  \_\_|  \_\\____/|_|  \_\

            			Descripcion: BD %databaseName% no existe ("BD " + databaseName + " no existe")
            			'''
            print("error no existe la bd")
            return

    def exist(self, database: str) -> bool:
        tables_: list = j.showTables(database)
        # La Base de datos existe
        if tables_ != None:
            return True
        else:
            return False
