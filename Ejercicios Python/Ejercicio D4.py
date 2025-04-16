
estudiantes = {}


for i in range(0,9):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input("Ingrese la nota del estudiante: "))
    estudiantes[str(i)] = {"nombre": nombre, "nota": nota }
    
    continuar = input("Deseas continuar s/n")
    if continuar.lower() != "s":
        break
        
    
    
