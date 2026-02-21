#Crear un programa que permita gestionar y visualizar contenido multimedia. Utilizar listas, diccionarios, mapeo y filtrado para crear un sistema que
#permita agregar contenido, registrar visualizaciones, mapear titulos, filtrar por genero y mostrar el contenido mas visualizado.

#Se debe utilizar una lista de diccionarios para almacenar la informacion de cada elemento de contenido. Cada diccionario
#representara un elemento de contenido y contendra claves como titulo, genero, duracion y visualizaciones.

#Implementa una funcionalidad que tome la entrada del usuario para el titulo, genero y duracion del contenido. Luego crea
#un diccionario con esta informacion y agregalo a la lista de contenido.

#Desarrolla una funcionalidad que permite al usuario seleccionar un contenido existente y aumentar el contador de visualizaciones
#en el diccionario correspondiente.

#Crea una funcionalidad que recorra la lista de contenido y retorne una nueva lista con los titulos de cada elemento. Mostrar
#los titulos disponibles en consola.

#Crea una funcionalidad para mostrar al usuario el menu de opciones y leer su eleccion. Dependiendo de la opcion seleccionada,
#llama a las funciones apropiadas para realizar la operacion correspondiente.

#Utiliza un bucle principal que mantenga el programa en ejecucion mientras el usuario no elija la opcion de salir. En cada
#iteracion, muestra el menu y realiza la operacion seleccionada por el usuario.

def agregarPelicula(catalogo, titulo, genero, duracion): #1.Agregar contenido
    nuevoContenido = {
        'titulo': titulo,
        'genero': genero,
        'duracion': duracion,
        'visualizaciones': 0 
    }
    catalogo.append(nuevoContenido)
    print('Contenido agregado exitosamente.')

def mostrarPeliculas(catalogo): #2.Mostrar todas las peliculas dentro del catalogo
    for i in catalogo:
        print(f'Titulo: {i['titulo']} Genero: {i['genero']} Duracion: {i['duracion']} minutos Visualizaciones: {i['visualizaciones']}')

def buscarPelicula(catalogo, titulo): #3.Consultar informacion de una pelicula
    titulos = [t['titulo'] for t in catalogo] #se agrega a una lista los titulos de todas las peliculas en el catalogo
    while titulo not in titulos: #mientras el usuario ingrese un titulo de pelicula que no este en el catalogo
        print('Pelicula no encontrada. Ingrese nuevamente') #mensaje de error
        titulo = str.upper(input('Ingrese el titulo de una pelicula: ')) #el usuario vuelve a ingresar el titulo de una pelicula
    for t in catalogo:
        if t['titulo'] == titulo: #si la pelicula existe dentro del catalogo, se muestra la informacion asociada
            print(f'Genero: {t['genero']}, Duracion: {t['duracion']}, Visualizaciones: {t['visualizaciones']}')
            t['visualizaciones']+= 1 #el dato de visualizaciones aumenta en 1

def obtenerTitulos(catalogo): #4.Obtener los titulos de todas las peliculas
    titulos = [t['titulo'] for t in catalogo]
    for tit in titulos:
        print(f'Titulo: {tit}')

def filtrarGenero(catalogo, genero): #5.Filtrar por genero
    generos = [g['genero'] for g in catalogo] #guardo los generos en una lista
    while genero not in generos: #verifico que el usuario introduzca un genero almacenado en el catalogo
        print('Genero no encontrado. Ingrese nuevamente.')
        genero = str.lower(input('Ingrese un genero para ver las peliculas asociadas: '))#el usuario vuelve a introducir un genero
    for g in catalogo:
        if g['genero'] == genero: #si el genero es correcto, se muestran las peliculas asociadas
            print(f'Titulo: {g['titulo']} Duracion: {g['duracion']} minutos.')

def masVisto(catalogo): #6.Pelicula mas vista
    visualizaciones = [v['visualizaciones'] for v in catalogo] #almaceno en una lista todos los datos de visualizaciones
    for vis in catalogo:
        if vis['visualizaciones'] == max(visualizaciones):#se obtiene el dato de visualizacion mas alto y la pelicula asociada
            print(f'Titulo: {vis['titulo']} Genero: {vis['genero']} Duracion: {vis['duracion']} minutos.')

def mayorDuracion(catalogo): #7.Pelicula con mayor duracion
    duracion_de_peliculas = [d['duracion'] for d in catalogo] #almaceno en una lista todos los datos de duracion
    for dur in catalogo:
        if dur['duracion'] == max(duracion_de_peliculas):#se obtiene el dato de duracion mas alto y la pelicula asociada
            print(f'Titulo: {dur['titulo']} Genero: {dur['genero']} Visualizaciones: {dur['visualizaciones']}')

def menorDuracion(catalogo): #8.Pelicula con menor duracion
    duracion_de_peliculas = [d['duracion'] for d in catalogo]
    for dur in catalogo:
        if dur['duracion'] == min(duracion_de_peliculas):#se obtiene el dato de duracion mas bajo y la pelicula asociada
            print(f'Titulo: {dur['titulo']} Genero: {dur['genero']} Visualizaciones: {dur['visualizaciones']}')

def eliminarPelicula(catalogo, titulo): #9.Eliminar una pelicula
    titulos = [t['titulo'] for t in catalogo]
    while titulo not in titulos:
        print('La pelicula que busca no esta en el catalogo. Intente nuevamente.')
        titulo = str.upper(input('Ingrese el titulo de una pelicula: '))
    for e in catalogo:#itero dentro de la lista
        if e['titulo'] == titulo: #si el titulo ingresado se encuentra en uno de los diccionarios
            catalogo.remove(e) #se elimina el diccionario
    print(f'La pelicula {titulo} ha sido eliminada.')

def gestorMultimedia(): #Funcion principal
    catalogo = [] #la lista que contendra cada diccionario con informacion de las peliculas
    while True:
        print("""Menu de opciones:
    1. Agregar pelicula\n
    2. Mostrar peliculas\n
    3. Consultar informacion de una pelicula\n
    4. Obtener titulos de todas las peliculas\n
    5. Filtrar peliculas por genero\n
    6. Pelicula mas visualizada\n
    7. Pelicula con mayor duracion\n
    8. Pelicula con menor duracion\n
    9. Eliminar una pelicula\n
    10. Salir del menu""")
        opcion = int(input('Ingrese el numero de la opcion elegida: ')) #el usuario ingresa el numero de la opcion
        if opcion == 1:
            titulo = str.upper(input('Ingrese un titulo: '))
            genero = str(input('Ingrese el genero de la pelicula: '))
            duracion = int(input('Ingrese la duracion de la pelicula en minutos: '))
            agregarPelicula(catalogo, titulo, genero, duracion)
        elif opcion == 2:
            mostrarPeliculas(catalogo)
        elif opcion == 3:
            titulo = str.upper(input('Ingrese el titulo de una pelicula para ver informacion asociada: '))
            buscarPelicula(catalogo, titulo)
        elif opcion == 4:
            obtenerTitulos(catalogo)
        elif opcion == 5:
            genero = str.lower(input('Ingrese un genero para ver las peliculas asociadas: '))
            filtrarGenero(catalogo, genero)
        elif opcion == 6:
            masVisto(catalogo)
        elif opcion == 7:
            mayorDuracion(catalogo)
        elif opcion == 8:
            menorDuracion(catalogo)
        elif opcion == 9:
            titulo = str.upper(input('Ingrese el titulo de la pelicula que desea eliminar: '))
            eliminarPelicula(catalogo, titulo)
        elif opcion == 10:
            print('Saliendo del menu')
            break #para que el bucle while finalice
        else:
            print('Opcion no encontrada.')
    return ''

print(gestorMultimedia())
