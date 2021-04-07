# Valores mayores que el segundo : escribe una función que acepte una lista y crea una nueva lista que contenga solo los valores de la lista original que sean mayores que su segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False
def values_greater_than_second (lista):
    if len(lista)<2:
        return False
    else:
        new_list=[]
        for i in range(0,len(lista)-1,2):
            if lista[i] >= lista[i+1]:
                new_list.append(lista[i])
            else:
                new_list.append(lista[i+1])
        return new_list

# print(values_greater_than_second ([5,2,3,2,1,4]))
print(values_greater_than_second ([5]))
