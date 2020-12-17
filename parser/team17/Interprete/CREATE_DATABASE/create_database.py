from Interprete.NodoAST import NodoArbol
from Interprete.Tabla_de_simbolos import Tabla_de_simbolos
from Interprete.Arbol import Arbol
from Interprete.Valor.Valor import Valor
from StoreManager import jsonMode as dbms

#####################################
# Patrón intérprete: CREATE DATABASE#
#####################################

# CREATE DATABASE: crear una base de datos


class CreateDatabase(NodoArbol):

    def __init__(self, id_, replace_, ifnotexists_):
        self.id = id_
        self.replace = replace_
        self.ifnotexists = ifnotexists_

    def execute(self, entorno: Tabla_de_simbolos, arbol: Arbol):

        if self.replace is True and self.ifnotexists is True or self.replace is False and self.ifnotexists is False:
            resultado = dbms.createDatabase(self.id)
            if resultado == 0:  # OPERACION EXITOSA
                arbol.console.append('tytus> Base de datos \'' + self.id + '\' creada exitosamente')
                print('tytus> Base de datos \'' + self.id + '\' creada exitosamente')
            elif resultado == 1:  # ERROR EN LA OPERACION
                '''
                            			  ______ _____  _____   ____  _____  
                            			 |  ____|  __ \|  __ \ / __ \|  __ \ 
                            			 | |__  | |__) | |__) | |  | | |__) |
                            			 |  __| |  _  /|  _  /| |  | |  _  / 
                            			 | |____| | \ \| | \ \| |__| | | \ \ 
                            			 |______|_|  \_\_|  \_\\____/|_|  \_\

                            			Descripcion: error en la operacion
                            			'''
                print("error en la operacion")
            else:  # LA BASE DE DATOS YA EXISTE
                '''
                            			  ______ _____  _____   ____  _____  
                            			 |  ____|  __ \|  __ \ / __ \|  __ \ 
                            			 | |__  | |__) | |__) | |  | | |__) |
                            			 |  __| |  _  /|  _  /| |  | |  _  / 
                            			 | |____| | \ \| | \ \| |__| | | \ \ 
                            			 |______|_|  \_\_|  \_\\____/|_|  \_\

                            			Descripcion: la BD ya existe ("BD " + databaseName + " ya existe")
                            			'''
                print("ya existe la base de datos")
        elif self.replace is True and self.ifnotexists is False:
            if self.existe(self.id) is True:
                dbms.dropDatabase(self.id)
                arbol.console.append('tytus> Base de datos \'' + self.id + '\' eliminada exitosamente')
                print('tytus> Base de datos \'' + self.id + '\' eliminada exitosamente')
            dbms.createDatabase(self.id)
            arbol.console.append('tytus> Base de datos \'' + self.id + '\' creada exitosamente')
            print('tytus> Base de datos \'' + self.id + '\' creada exitosamente')
        else:
            if self.existe(self.id) is False:
                dbms.createDatabase(self.id)
                arbol.console.append('tytus> Base de datos \'' + self.id + '\' creada exitosamente')
                print('tytus> Base de datos \'' + self.id + '\' creada exitosamente')
            else:
                '''
                                            			  ______ _____  _____   ____  _____  
                                            			 |  ____|  __ \|  __ \ / __ \|  __ \ 
                                            			 | |__  | |__) | |__) | |  | | |__) |
                                            			 |  __| |  _  /|  _  /| |  | |  _  / 
                                            			 | |____| | \ \| | \ \| |__| | | \ \ 
                                            			 |______|_|  \_\_|  \_\\____/|_|  \_\

                                            			Descripcion: la BD ya existe ("BD " + databaseName + " ya existe")
                                            			'''
                print("ya existe la base de datos")

    def existe(self, database: str) -> bool:
        tables_: list = dbms.showTables(database)
        # La Base de datos existe
        if tables_ is not None:
            return True
        else:
            return False