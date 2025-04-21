# Ejercicio 1: Suma de elementos en una lista de listas
def suma_matriz(matriz):
    fil = len(matriz)
    col = len(matriz[0])
    acumulador = 0 
    for i in range (fil):
        for j in range(col):
            acumulador += matriz[i][j]
    return acumulador
 
   
# Ejercicio 2: Encontrar el valor máximo en una matriz
def maximo_matriz(matriz):
    maximo = matriz[0][0]
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
    return maximo
    
# Ejercicio 3: Verificar si un número es primo
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2,numero):
        if numero % i == 0:
            return False
    return True

# Ejercicio 4: Transponer una matriz
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        transpuesta.append(nueva_fila)
    return transpuesta    

# Ejercicio 5: Filtrar números pares
def filtrar_pares(lista):
   pares = []
   for numero in lista:
       if numero % 2 == 0:
           pares.append(numero)
   return pares

# Ejercicio 6: Contar la cantidad de palabras en una frase
def contar_palabras(frase):
    contador = 0
    palabras = frase.split(" ")
    for palabra in palabras:
        if palabra != "":
            contador += 1
    return contador

# Ejercicio 7: Crear una tabla de multiplicar
def tabla_multiplicar(n):
   tabla = []
   for i in range (1,11):
       tabla.append(n * i)
   return tabla

# Ejercicio 8: Contar números negativos en una lista
def contar_negativos(lista):
    contador = 0
    for numero in lista:
        if numero < 0:
            contador += 1
    return contador


# Ejercicio 9: Determinar si una lista está ordenada
def lista_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Ejercicio 10: Cifrar un texto con el cifrado César
def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                base = ord('A')
            else:
                base = ord('a')
            cifrado = ord(caracter) - base
            cifrado = (cifrado + desplazamiento) % 26 + base
            nuevo_caracter = chr(cifrado)
            resultado += nuevo_caracter
        else:
            resultado += caracter   
    return resultado


#Aquí comienza el progrma principal. No modifiques el código debajo de esta línea.
def main():
    # Ejercicio 1: Suma de elementos en una lista de listas
    lista = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    resultado = suma_matriz(lista)
    print(f"suma de todos los elementos es: {resultado}")

    # Ejercicio 2: Encontrar el valor máximo en una matriz
    matriz = [[3, 7, 2,], [9, 4, 6]]
    maximo = maximo_matriz(matriz)
    print(f"El valor máximo de la matriz es: {maximo}")  

    # Ejercicio 3: Verificar si un número es primo
    numero = (int(input("Ingrese un número para verificar si es primo: ")))
    numero = es_primo(numero)
    if es_primo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")
    print (f"El número {numero} es primo: {es_primo(numero)}")

    # Ejercicio 4: Transponer una matriz
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transpuesta = transponer_matriz(matriz)
    print("Matriz original:")   
    for fila in matriz:
        print(fila)
    print("Matriz transpuesta:")    
    for fila in transpuesta:
        print(fila)

    # Ejercicio 5: Filtrar números pares    
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = filtrar_pares(lista)
    print(f"Números pares: {pares}")

    # Ejercicio 6: Contar la cantidad de palabras en una frase
    frase = "Hola, ¿cómo estás?"
    cantidad_palabras = contar_palabras(frase)
    print(f"La cantidad de palabras en la frase es: {cantidad_palabras}")

    # Ejercicio 7: Crear una tabla de multiplicar
    n = int(input("Ingrese un número para generar su tabla de multiplicar: "))
    tabla = tabla_multiplicar(n)
    print(f"Tabla de multiplicar del {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {tabla[i-1]}")

    # Ejercicio 8: Contar números negativos en una lista
    lista = [-1, 2, -3, 4, -5] 
    cantidad_negativos = contar_negativos(lista)
    print(f"La cantidad de números negativos en la lista es: {cantidad_negativos}")

    # Ejercicio 9: Determinar si una lista está ordenada
    lista = [1, 2, 3, 4, 5]
    if lista_ordenada(lista):
        print("La lista está ordenada.")
    else:
        print("La lista no está ordenada.") 

    # Ejercicio 10: Cifrar un texto con el cifrado César
    texto = int(input("Ingrese el texto a cifrar: "))
    desplazamiento = int(input("Ingrese el desplazamiento: "))
    texto_cifrado = cifrado_cesar(texto, desplazamiento)
    print(f"Texto cifrado: {texto_cifrado}")


if __name__ == "__main__":
    main()


#ESTE texto es un comentario para verificar un error en los commits de git
# NOTA: a la hora de subir los archivos a git no me queria dejar guardar, los commits se realizaban pero cuando iba hacer el "push" no seveian reflejados en el repositorio remoto 