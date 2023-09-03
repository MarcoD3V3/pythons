import pandas as pd
import inquirer
import os

archivo_csv = 'data.csv'

# Función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar la tabla de datos
def mostrar_tabla():
    print("==============================================================================================================")
    print(df)
    print("==============================================================================================================")

# Cargar el archivo CSV
df = pd.read_csv(archivo_csv)

# Mostrar la tabla de datos
mostrar_tabla()

# Preguntar al usuario qué acción desea realizar
questions = [inquirer.List('opcion', message="Selecciona una opción:", choices=['Agregar', 'Eliminar', 'Editar'])]
respuestas = inquirer.prompt(questions)
opcion_seleccionada = respuestas["opcion"]

print(f'Has seleccionado la opción: {opcion_seleccionada}')

if opcion_seleccionada == "Agregar":
    limpiar_consola()
    print('Inserte los datos correspondientes')
    print('')
    print('================================================')
    Nombre = str(input('Nombre del paciente: '))
    Apellido = str(input('Apellido del paciente: '))
    Edad = int(input('Edad del paciente: '))
    DNI = int(input('DNI del paciente: '))
    Nacionalidad = str(input('Nacionalidad del paciente: '))
    Email = str(input('Email del paciente: '))
    Diagnóstico = str(input('Diagnóstico del paciente: '))
    print('================================================')
    print('')
    persona = {
        "Nombre": Nombre,
        "Apellido": Apellido,
        "Edad": Edad,
        "DNI": DNI,
        "Nacionalidad": Nacionalidad,
        "Email": Email,
        "Diagnóstico": Diagnóstico
    }

    df_persona = pd.DataFrame([persona])
    df = pd.concat([df, df_persona], ignore_index=True)
    df.to_csv('data.csv', index=False)
    mostrar_tabla()

if opcion_seleccionada == 'Editar':
    print("Función de edición no implementada todavía")

# Puedes agregar lógica para eliminar datos si lo necesitas

# Ejemplo de cómo buscar una persona por nombre (descomenta si lo necesitas)
# nombre_a_buscar = input("Ingrese el nombre a buscar: ")
# resultado = df[df["Nombre"] == nombre_a_buscar]
# if not resultado.empty:
#     print(resultado)
# else:
#     print(f"No se encontraron registros para el nombre: {nombre_a_buscar}")
