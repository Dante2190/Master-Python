"""
ejericio 5 
Crear una lista con el contenido de esta tabla:

ACCION      AVENTURAS           DEPORTES
GTA         ASSINS              FIFA 21
COD         CRASH               PRO 21
PUGB        PRINCE OF PERSIA    MOTO GP 21

Mostrar esta informacion ordenada 
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "COD", "PUGN"]
    },
    {
        "categoria": "AVENTURAS",
        "juegos": ["ASSASING", "CRASH", "PRINCE OF PERSIA"]
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "PRO 21", "MOTO GP 21"]
    }
]

for categoria in tabla:
    print(f"-------------{categoria['categoria']}-------------")
    for juegos in categoria['juegos']:
        print(juegos)

