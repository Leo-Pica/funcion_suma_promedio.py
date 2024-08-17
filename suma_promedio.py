def suma_y_promedio(numeros): #definimos la función suma_y_promedio
    suma = sum(numeros) #usamos función suma para sumar los números ingresados y almacenarlos en variable suma
    promedio = suma / len(numeros) if numeros else 0 #calculamos promedio dividiendo la suma entre la cnatidad de elementos en numeros que obtenemos con len(numeros)
    #if numeros else 0 es para evitar un error al dividir entre 0 si la lista está vacía. 
    return suma, promedio #la función devuelve una tupla con la suma y el promedio. 

# Ejemplo de uso:
numeros = [20, 20, 40, 40, 50] #acá ingresamos una lista de números separados por comas.
resultado = suma_y_promedio(numeros) #asignamos a la función resultado el valor de la función creada.
print(f"Suma: {resultado[0]}, Promedio: {resultado[1]}") #mostramos el resultado.[0] es el primer parámetro "suma" y [1] el segundo "promedio". 
