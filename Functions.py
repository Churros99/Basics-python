# Section 4: Functions 
# Example 1
def suma():
    return 10 + 10

print(suma())

# Example 2:
def tipo():
    return type(15)

print(tipo())

# Example 3:
def Saludo():
    return "Hola Obed, Bienvenido"

print(Saludo())

# Default Parameters:
# Example 1

def Multiplicar(num1:float, num2:float):
    return num1 * num2
    
print(Multiplicar(15,15))

# Example 2 
def ImprimirMensaje(msg: str):
    print(f'El mensaje es: {msg}')

ImprimirMensaje('Bienvenido, al curso de Python')

# Example 3
def sumar_recursiva(n:float):
    if n == 0:
        return 0
    else:
        return n + sumar_recursiva(n-1)
    
print(sumar_recursiva(10))

# Keyword Arguments
#Example 1
def Empleado(Nombre, **kwargs):
    empleado ={'Nombre':Nombre}
    
    for key, val in kwargs.items():    
        empleado[key] = val
    return empleado 

print(Empleado(Nombre='Obed',Edad=30, Ciudad='Ojinaga'))

# Example 2
def Operaciones(accion:str, **kwargs):
    resultado = 0
    if(accion =='Sumar'):
        for key, val in kwargs.items():
            resultado += val
    elif(accion =='Restar'):
        for key, val in kwargs.items():
            resultado += val
    elif(accion =='Multiplicar'):
        for key, val in kwargs.items():
            resultado += val
    elif(accion == 'Division'):
        for key, val in kwargs.items():
            resultado += val
    else:
        print('Operacion no identificada')
    
    print(resultado)
        
        
Operaciones(accion='Sumar',n1= 48, n2=58, n3=57)

# Examples 3
def Ventas(Iva: float, **Kwargs):
    total = 0
    for key, val in Kwargs.items():
        print(f'Articulo: {key} Precio: {val}')
        total += val
    print(f'Subtotal: {total}')
    print(f'IVA: {total * Iva}')
    print(f'Total{(total * Iva) + total}')

Ventas(Iva=0.16, Soda=45, Sabritas=20, pizza=90)