print("Notas del Estudiante")


cantidad = int(input("Ingresela cantidad de Estudiantes que desea ingresar: "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre del estudiante: {i+1} ")
    notas = int(input("Ingrese la cantidad de notas a promediar: "))
    for j in range(notas):
        notas1 = int(input(f"Ingrese la nota: {j+1}"))

except ValueError:
    print("Error: Debes ingresar números válidos.")

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

except TypeError:
    print("Error: No puedes combinar diferentes tipos de datos (por ejemplo, número + texto).")

except Exception as e:
    print("Se produjo un error inesperado:", e)

else:
    print(f"Resultado de la división: {resultado}")
    print(f"Suma con texto (esto no debería ejecutarse): {suma}")

finally:
    print("Fin del proceso.")