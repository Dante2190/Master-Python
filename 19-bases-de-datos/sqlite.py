# importar el modulo
import sqlite3

# abrir conexion
conexion = sqlite3.connect('pruebas.db')

# crear cursor para poder hacer las consultas 
cursor = conexion.cursor()

# crear una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"titulo varchar(100), "+
"descripcion text, "+
"precio int(255)"+
")")

# guardar cambios 
conexion.commit()

# insertar datos
#cursor.execute("INSERT INTO productos VALUES(null, 'primer producto', 'descripcion del producto', 550)")
# guardar cambios 
#conexion.commit()

# borrar rwgistros 
#cursor.execute("DELETE FROM productos")
#conexion.commit()

# insertar varios registros a la ves 
productos=[
    ("ordenador portatil", "buen pc", 400),
    ("ordenador de escritorio", "buen pc", 500),
    ("cell fon portatil", "bueno", 100),
]

cursor.executemany("INSERT INTO productos VALUES(null,?,?,?)", productos)
conexion.commit()

# Update
cursor.execute("")

# lectura de datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

for producto in productos:
    print("id: ", producto[0])
    print("titulo: ", producto[1])
    print("descripcion: ", producto[2])
    print("precio: ", producto[3])
    print("\n")


# cerrar conexion
conexion.close()