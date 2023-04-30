# If Else statements Examples
# Example 1
Edad = 29 

if Edad <= 17:
    print('Eres menor de Edad')
elif Edad >= 18 and Edad <=30:
    print('Eres un adulto')
elif Edad >= 31 and Edad <= 40:
    print('Eres un Chavorruco')
elif Edad >= 41 and Edad <= 50:
    print('Eres un señor hecho y derecho')
elif Edad >= 51:
    print('Ya eres de la tercera edad')

# example 2
numero = 15

if(numero % 2 == 0):
    print(f'el número {numero} es par')
else:
    print(f'el número {numero} es impar')
    

# Example 3

lista = [1,2,3,4,5,6,7,8,10]
num = 9
if(num in lista):
    print(f'El número {num} esta dentro de la lista')
else:
    print(f'el número {num} no existe en la lista')

# Ternary Operator examples
# example 1
empleados = ['Obed', 'Juan', 'Marco', 'Aria']
empleado = 'Obed'

existe = True if empleado in empleados else False

print(f'El empleado existe?: {existe}')

# example 2
num1 = 15
num2 = 5

divisible = True if num1 % num2 == 0 else False

print(f'los numeros: {num1} y {num2} son divisibles entre si? {divisible}')

# example 3
edad = 18

adulto = True if edad >=18 else False

print(f'eres un adulto? {adulto}')

# for loop with range() examples
# Example 1
par = []
inpar = []
for i in range(100):
    if(i%2 ==0):
        par.append(i)
    else:
        inpar.append(i)

print(f'los numeros pares son: {par}')
print(f'los numeros impar son: {inpar}')

# Example 2

suma = 0
for i in range(5,15):
    suma += i

print(f'El resultado de la suma: {suma}')

# Example 3
sumar_par = 0
for i in range(50):
    if i % 2 == 0:
        sumar_par += i

print(f'el resultado de la suma de los pares: {sumar_par}')

# While Examples
# Example 1
while  i <= 30:
    print(i)
    i += 1

# Example 2    
while True:
    try:
        num = float(input("Ingrese un número: "))
    except ValueError:
        print("El dato ingresado no es un número válido. Intente de nuevo.")
        break

# Example 3
num1 = 1
num2 = 1
while num1 % num2 == 0:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = True if num1 % num2 == 0 else False
        print(f'son divisibles? {resultado}')
    except ValueError:
        print("El dato ingresado no es un número válido. Intente de nuevo.")
        num1 = 1
        num2 = 1
