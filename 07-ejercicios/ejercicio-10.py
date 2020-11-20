"""
hacer un programa que pida la nota de 15 alumnos 
y sacar por lla pantalla cuantos han aprobado y cuantos han suspendido 

"""

contador = 1
aprobados = 0
suspendidos = 0

num_alumnos = int(input("cuantos alumnos tienes: "))

while contador <= num_alumnos:
    nota = int(input(f"que nota quieres ponerle al alumno {contador}"))
    if nota >= 5:
        aprobados +=1
    else:
        suspendidos +=1    
    contador += 1

print(f"alumnos aprobados: {aprobados}")   
print(f"alumnos aprobados: {suspendidos}")    