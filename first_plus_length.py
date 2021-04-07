# First Plus Length : crea una función que acepta una lista y devuelve la suma del primer valor de la lista más la longitud de la lista.
# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)
def first_plus_length(lista):
    return lista[0]+lista[len(lista)-1]

print(first_plus_length ([1,2,3,4,5]))
