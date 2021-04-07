# Cuenta regresiva : crea una función que acepte un número como entrada. Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número (como el elemento 0) hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
def cuenta_regresiva():
    num=int(input("Ingresa un numero: "))
    lista=[]
    for i in range(num,-1,-1):
        lista.append(i)
    return lista

print(cuenta_regresiva())