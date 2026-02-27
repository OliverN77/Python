# Crear una función llamada es_palindromo que reciba un texto como parámetro y retorne True si es un palíndromo (se lee igual al derecho y al revés) o False en caso contrario. La función debe ignorar espacios, mayúsculas/minúsculas y signos de puntuación.

def es_palindromo(texto):
    # Eliminar espacios, mayúsculas/minúsculas y signos de puntuación
    texto_limpio = ''.join(caracter for caracter in texto if caracter.isalnum()).lower()
    # Verificar si el texto limpio es igual a su reverso
    if texto_limpio == texto_limpio[::-1]:
        return True
    else:        
        return False

texto = str(input("Ingrese un texto para verificar si es un palíndromo: "))
if es_palindromo(texto):
    print("El texto es un palíndromo.")
else:
    print("El texto no es un palíndromo.")