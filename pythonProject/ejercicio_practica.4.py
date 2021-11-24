# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int

    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    list_numeros_str = ['5', '2', '3', '-8', '7', 'NaN']
    lista = [int(i) if (i.isdigit() is True) else 0 for i in list_numeros_str]
    print(lista)
    # ¿Ya terminaron el ejercicio? : si . ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?: no se , probare.
    # ¿Qué sucede con isdigit? : que es una funcion util para este tipo de ejercicios  . Sorprendente no? creo que si.

    print("terminamos")