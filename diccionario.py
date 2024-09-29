# Crear un diccionario con información personal
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Madrid"
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Barcelona"

# Agregar la clave "profesión"
informacion_personal["profesion"] = "Programador"

# Verificar si existe la clave "telefono" y agregarla si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "1234567890"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario final
print(informacion_personal)