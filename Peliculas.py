# -*- coding: cp1252 -*-
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si est� vac�a. """
 
    def __init__(self):
        """ Crea una cola vac�a """
        # La cola vac�a se representa con una lista vac�a
        self.items=[]
    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola est� vac�a levanta una excepci�n. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola est� vac�a")
    
    def es_vacia(self):
        """ Devuelve True si la lista est� vac�a, False si no. """
        return self.items == []
    
    def cantidadElementos(self):
        return len(self.items)

class Pelicula:
    def __init__(self,nombre,genero):
        self.nombre=nombre
        self.genero=genero

def menu():
    opcion = raw_input("\nSeleccione una opcion:\n[A]gregar Pel�cula\n[B]uscar Peliculas por Genero\n ")
    return opcion

def agregarPelicula():
        pelicula = Pelicula(raw_input("Ingrese el Nombre de la Pelicula: "),raw_input("Ingrese el Genero de la Pelicula: "))
        peliculasDesordenadas.encolar(pelicula)

def buscarPeliculas():
        genero = raw_input("Ingrese el Genero: ")
        colaPeliculas = Cola()
        cont = 0;
        
        """ Va recorriendo la cola de peliculas desordenadas, desencolando la primera y encolandola de ultimo, las que coinciden con el g�nero se agregan a la nueva cola de pel�culas."""

        while(cont != peliculasDesordenadas.cantidadElementos()):
            cont+=1
            pelicula = peliculasDesordenadas.desencolar();
            print "Desencol� la pel�cula: ",pelicula.nombre
            if(pelicula.genero == genero):
                colaPeliculas.encolar(pelicula)
                print "La pel�cula es del g�nero, se encola en colaPeliculas"
                
            peliculasDesordenadas.encolar(pelicula)
            print "Encol� la pel�cula al final: ",pelicula.nombre
            
        """ Recorre la nueva cola de peliculas, desencolando cada vez el primer elemento e imprimiendolo hasta que quede vac�a """
        
        print "\nPEL�CULAS DEL G�NERO INGRESADO:"
        while(colaPeliculas.es_vacia() == False):
            pelicula = colaPeliculas.desencolar()
            print pelicula.nombre

def peliculasPredeterminadas():
        peliculasDesordenadas.encolar(Pelicula("Star Wars","Ciencia Ficci�n"))
        peliculasDesordenadas.encolar(Pelicula("Viernes 13","Terror"))
        peliculasDesordenadas.encolar(Pelicula("Terminator","Acci�n"))
        peliculasDesordenadas.encolar(Pelicula("Matrix","Ciencia Ficci�n"))
        peliculasDesordenadas.encolar(Pelicula("El Aro","Terror"))
        peliculasDesordenadas.encolar(Pelicula("Inception","Ciencia Ficci�n"))
        peliculasDesordenadas.encolar(Pelicula("Jumanji","Acci�n"))
        peliculasDesordenadas.encolar(Pelicula("D�a de la Independencia","Ciencia Ficci�n"))
        peliculasDesordenadas.encolar(Pelicula("It","Terror"))
        peliculasDesordenadas.encolar(Pelicula("Actividad Paranormal","Terror"))
        peliculasDesordenadas.encolar(Pelicula("Los Indestructibles","Acci�n"))
        peliculasDesordenadas.encolar(Pelicula("Ex Machina","Ciencia Ficci�n"))
        peliculasDesordenadas.encolar(Pelicula("300","Acci�n"))
        peliculasDesordenadas.encolar(Pelicula("El Conjuro","Terror"))


peliculasDesordenadas= Cola()
peliculasPredeterminadas()                               
while True:

    try:
        opcion = menu();
        if(opcion == "A" or opcion == "a"):
            agregarPelicula();
        elif(opcion == "B" or opcion == "b"):
            buscarPeliculas();
        else:
            break
    except:
        print ("Error")
        break


