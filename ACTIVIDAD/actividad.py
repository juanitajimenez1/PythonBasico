"""
Evalúe un número y especifique si es par o impar
""" 
def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Uso:
try:
    numero = int(input("Ingrese un número: "))
    resultado = verificar_par_impar(numero)
    print(f"El número {numero} es {resultado}.")
except ValueError:
    print("Por favor, ingrese un número válido en formato numérico.")


"""
Evalúe la edad de una persona, si es menor de 18 dígale que el costo es de 
$400, si está entre 19 y 25 de $450 y para más de 26 años $500
"""
def calcular_costo_por_edad(edad):
    if edad < 18:
        return 400
    elif 18 <= edad <= 25:
        return 450
    else: 
        return 500

# Ejemplo de uso:
try:
    edad = int(input("Ingrese la edad de la persona: "))
    costo = calcular_costo_por_edad(edad)
    print(f"El costo para una persona de {edad} años es de ${costo}.")
except ValueError:
    print("Por favor, ingrese una edad válida en formato numérico.")

"""
Evalúe dos años, por ejemplo 2010 y 2050, e imprima a continuación cuántos
años pasarán desde el primer año para llegar al segundo. El código debe 
funcionar para cualquier par de años
"""
def calcular_year_pasan(desde_year, hasta_year):
    if desde_year > hasta_year:
        print("El primer año debe ser menor que el segundo año.")
        return

    year_pasan = hasta_year - desde_year
    print(f"Desde el año {desde_year} hasta el año {hasta_year}, pasarán {year_pasan} años.")

# Ejemplo de uso:
try:
    year_inicual = int(input("Ingrese el primer año: "))
    year_final = int(input("Ingrese el segundo año: "))
    calcular_year_pasan(year_inicual, year_final)
except ValueError:
    print("Por favor, ingrese años válidos en formato numérico.")

"""
Escriba un programa que pida tres números y que escriba si son los tres iguales, 
si hay dos iguales o si son los tres distintos. (Utilice if, elif, else)
"""
try:
    # Solicitar al usuario ingresar tres números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))

    # Verificar las condiciones
    if num1 == num2 == num3:
        print("Los tres números son iguales.")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("Hay al menos dos números iguales.")
    else:
        print("Los tres números son distintos.")
except ValueError:
    print("Por favor, ingrese números válidos en formato numérico.")


"""
Escribir un programa que solicite evalúe una variable que puede 
contener un caracter o un string y que devuelva el mensaje de si 
el contenido de la variable es un caracter o un string (apóyese de la función len() )
"""
# Solicitar al usuario ingresar un valor
entrada = input("Ingrese un valor (carácter o cadena): ")

# Verificar si la entrada es un carácter o una cadena
if len(entrada) == 1:
    print(f"La variable contiene un carácter: '{entrada}'")
else:
    print(f"La variable contiene una cadena: '{entrada}'")


