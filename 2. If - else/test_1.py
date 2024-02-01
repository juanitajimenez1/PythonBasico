#if - else 

"""
Condiciones lógicas 
Igualdad: a == b
Diferente: a != b
Menor que: a < b
Menor o igual que: a <= b
Mayor que: a > b
Mayor o igual que: a >= b
"""


a = 33
b = 200

if a == b:
    print("los valores son iguales")

if a < b:
    print("a es menor que b")

#Elif 
a = 33
b = 33
if a > b:
    print("b es mas grande que a")
elif a == b:
    print("los valores son idénticos")
    
#Else
a = 200
b = 33

if b > a:
    print("b es ayor que a")
else:
    print("a es mayor que b")

a = 200
b = 33
if b > a:
    print("b es mayor que a")
elif a == b:
    print("ambos valores son idénticos")
else: 
    print("a es mayor que b")

#If corto 
a = 200
b = 33

if a > b: print("a es mayor que b")

#If - else corto
print("a es mayor que b") if a>b else print("b es mayor que a")

#and combina las condiciones de dos comparaciones
a = 200
b = 33
c = 500

if a >b and c > a:
    print("ambas condiciones son verdaderas")
else:
    print("alguna condición es falsa")

#or comparar que una de dos condiciones se cumpla
a = 200
b = 33
c = 500

if a > b or a >c:
    print("al menos una de las dos consiciones se cumple")

#not niega o invierte el resultado de una comparacion
a = 200
b = 33

if not a > b:
    print("a es mayor que b")

#anidad if
x = 12
if x > 10:
    print("El valor esta sobre 10")
    if x > 20:
        print("valor sobre b")
    else:
        print("el valor esta entre 10 y 20")


x = input("Dame un numero")
print("El valor fue:" , x)


def es_par(numero):
    if numero % 2 == 0:
        return True 
      
    else:
        return False

"""
Evalúe la edad de una persona, si es menor de 18 dígale que el costo es de 
$400, si está entre 19 y 25 de $450 y para más de 26 años $500
"""
def costo_por_edad(edad):
    if edad < 18:
        return "El costo es de $400."
    elif edad >= 19 and edad <= 25:
        return "El costo es de $450."
    elif edad > 26:
        return "El costo es de $500."
    else:
        return "Edad inválida."

edad = 20
print(costo_por_edad(edad))




