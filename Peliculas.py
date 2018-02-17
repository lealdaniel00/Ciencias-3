# -*- coding: cp1252 -*-
class Cola:
    """ Representa una cola con operaciones de encolar, desencolar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una cola vacía """
        # La cola vacía se representa con una lista vacía
        self.items=[]
    def encolar(self, x):
        """ Agrega el elemento x a la cola. """
        # Encolar es agregar al final de la cola.
        self.items.append(x)

    def desencolar(self):
        """ Devuelve el elemento inicial y lo elimina de la cola.
            Si la cola está vacía levanta una excepción. """
        try:
            return self.items.pop(0)
        except IndexError:
            raise ValueError("La cola está vacía")
    
    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []
    
    def cantidadElementos(self):
        return len(self.items)

class Pelicula:
    def __init__(self,nombre,genero):
        self.nombre=nombre
        self.genero=genero

def menu():
    opcion = raw_input("\nSeleccione una opcion:\n[A]gregar Película\n[B]uscar Peliculas por Genero\n ")
    return opcion

def agregarPelicula():
        pelicula = Pelicula(raw_input("Ingrese el Nombre de la Pelicula: "),raw_input("Ingrese el Genero de la Pelicula: "))
        peliculasDesordenadas.encolar(pelicula)

def buscarPeliculas():
        genero = raw_input("Ingrese el Genero: ")
        colaPeliculas = Cola()
        cont = 0;
        
        """ Va recorriendo la cola de peliculas desordenadas, desencolando la primera y encolandola de ultimo, las que coinciden con el género se agregan a la nueva cola de películas."""

        while(cont != peliculasDesordenadas.cantidadElementos()):
            cont+=1
            pelicula = peliculasDesordenadas.desencolar();
            print "Desencoló la película: ",pelicula.nombre
            if(pelicula.genero == genero):
                colaPeliculas.encolar(pelicula)
                print "La película es del género, se encola en colaPeliculas"
                
            peliculasDesordenadas.encolar(pelicula)
            print "Encoló la película al final: ",pelicula.nombre
            
        """ Recorre la nueva cola de peliculas, desencolando cada vez el primer elemento e imprimiendolo hasta que quede vacía """
        
        print "\nPELÍCULAS DEL GÉNERO INGRESADO:"
        while(colaPeliculas.es_vacia() == False):
            pelicula = colaPeliculas.desencolar()
            print pelicula.nombre

def peliculasPredeterminadas():
        peliculasDesordenadas.encolar(Pelicula("Star Wars","Ciencia Ficción"))
        peliculasDesordenadas.encolar(Pelicula("Viernes 13","Terror"))
        peliculasDesordenadas.encolar(Pelicula("Terminator","Acción"))
        peliculasDesordenadas.encolar(Pelicula("Matrix","Ciencia Ficción"))
        peliculasDesordenadas.encolar(Pelicula("El Aro","Terror"))
        peliculasDesordenadas.encolar(Pelicula("Inception","Ciencia Ficción"))
        peliculasDesordenadas.encolar(Pelicula("Jumanji","Acción"))
        peliculasDesordenadas.encolar(Pelicula("Día de la Independencia","Ciencia Ficción"))
        peliculasDesordenadas.encolar(Pelicula("It","Terror"))
        peliculasDesordenadas.encolar(Pelicula("Actividad Paranormal","Terror"))
        peliculasDesordenadas.encolar(Pelicula("Los Indestructibles","Acción"))
        peliculasDesordenadas.encolar(Pelicula("Ex Machina","Ciencia Ficción"))
        peliculasDesordenadas.encolar(Pelicula("300","Acción"))
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


