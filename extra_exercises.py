"""
Crear una función que calcule la temperatura media de un día
a partir de la temperatura máxima y mínima.
"""

def temperaturaMedia():
    minTemp = int(input("Ingresa la temperatura mínima: "))
    maxTemp = int(input("Ingresa la temperatura máxima: "))
    temp = minTemp + maxTemp
    temperatura = temp // 2
    return "la temperatura media es: " + str(temperatura)

"""
Crear un programa principal, que utilizando la función anterior,
vaya pidiendo la temperatura máxima y mínima de cada día
y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.
"""

def temperaturaSemanal(cantidadDias):
  temp = " "
  for i in range(1, cantidadDias + 1):
      print(f"// Dia {i} //")
      temp = temperaturaMedia()
      print(temp)

# temperaturaSemanal(int(input("Cantidad de dias: ")))
      
"""
Crea una función “calcularMaxMin” que recibe una lista
con valores numéricosy devuelve el valor máximo y el mínimo.
"""

def maxMin(x):
    max = 0
    min = 0
    for i in x:
        if i < min :
            min = i
        elif i > max :
            max = i
    print(f"El numero mas alto es el {max}")
    print(f"El numero mas bajo es el {min}")

# Diseñar una función que calcule el área y el perímetro de una circunferencia.
  
def calcularRadioDeCircunferencia():
    diametroDeCircunferencia = int(input("Introduzca el diametro de la circunferencia: "))
    radio = diametroDeCircunferencia // 2
    return radio

def calcularAreaYPerimetro():
    radioDeCircunferencia = calcularRadioDeCircunferencia()
    perimetro = int((3.14 * 2) * radioDeCircunferencia)
    area = int(3.14 * radioDeCircunferencia)
    print(f"El perimetro de la circunferencia es: {perimetro}")
    print(f"El area de la circunferencia es: {area}")

"""
Crear un programa principal donde se pida un nombre de usuario y una contraseña
y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
"""

def loginLimit3():
  for i in range(1, 4):
    usuario = input("usuario: ")
    password = input("password: ")
    if(usuario == "usuario1" and password == "asdasd"):
      print("login exitoso, felicitaciones")
      break
    elif (i == 3):
      print(f"{i}er intento fallido, una pena. Refresca para volver a intentar.")
    else:
      print("esta cuenta no existe, vuelve a intentarlo")
      print(f"intento numero {i} fallido")

"""
Escribir una función que reciba una muestra de números en una lista
y devuelva otra lista con sus cuadrados.
"""

def devolverListaAlCuadrado(lista):
  listaAlCuadrado = []
  for num in lista:
    numAlCuadrado = num * num
    listaAlCuadrado.append(numAlCuadrado)
  return listaAlCuadrado


  
