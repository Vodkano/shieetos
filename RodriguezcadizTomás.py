


rut = []
nombre = []
nota1 = [] 
nota2 = []

menu1 = input ("""
1.Procesar lista de estudiantes.
2. Registrar estudiante.
3. Modificar nota.
4. Eliminar estudiante.
5. Generar promedio de notas.
6. Generar acta de cierre de curso.
7. Salir""")

if menu1 == "2":
    preguntarut = input("Ingrese el rut del estudiante:")
rut.append(preguntarut)
preuntanomb = input("Ingrese nombre del estudiante:")
nombre.append(preuntanomb)
preguntanota1 = int(input("ingrese nota 1:"))
nota1.append(preguntanota1)
preguntanota2 = int(input("ingrese nota 2:"))
nota2.append(preguntanota2)

if menu1 == "3":
   print ("Eliminar estudiante")
nombreeliminar = input("Inrese nombre del estudiante:")
cpmfirmar = input("escriba (confirmo) si desea eliminar a" (nombreeliminar) )
if cpmfirmar == "Confirmo": 
   nombre.remove(nombreeliminar)