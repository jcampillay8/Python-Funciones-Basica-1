# Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
def length_and_value(tamano,valor):
    lista=[]
    for i in range(tamano):
        lista.append(valor)
    return lista

# print(length_and_value(4,7))

print(length_and_value(6,2))