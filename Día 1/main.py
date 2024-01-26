## -----------------------------
## ----Ejercicio 1 ----
## -----------------------------

# Impresion en consola 
print("hola mundo") 

# ---- Datos primitivos ----
#1. String
texto = "Campus"
print(texto)
print(type(texto))
#2. Int
numeroEntero = 1
print(numeroEntero)
#3. Float 
numeroDecimal = 3.1
print(numeroDecimal)
#4. Double 
numeroDecimalLargo = 3.14167582737283
print(numeroDecimalLargo)
#5. Boolean
booleano = True
print(booleano)
#---- Entradas parte del usuario  con definicion de tipo de dato primitivo ----
entradaUsuarioNumero= input("Ingresa tu edad: ")
numeroFinal = int(entradaUsuarioNumero)
print ("Tu edad es: " , numeroFinal)
#----Ciclos----
#Ciclo for
for i in range (5,10,2):#for contador in range (desde,hasta,pasos):
       print (i)
#Ciclo while 
booleanito = True
while booleanito == True:#whilw condicion_a_cumplir :
       print("sigo vivo")
       booleanito = False 
#---- Condicionales ----
texto1 = "campus"
if texto1 == "campus":
       print ("Soy campus")
else:
       print ("No soy campus")


#---- Funciones ----

#---- Con Parametro Con Retorno ----
       
def promedio (x,y):
       sumaTotal = x
       cantidad = y 
       Total = sumaTotal/cantidad 
       return"su promedio es: ", float (( Total ))
       
sumaTotal = int(input( "Ingrese la suma total: "))
cantidad = int (input("Ingrese la cantidad de digitos: "))

print(promedio(int(sumaTotal),int(cantidad)))

#---- Con Parametro Sin Retorno ----
       
def suma(a,b):
       sumaFinal = a+b
       print(sumaFinal)

a = int(input("ingrese numero 1: "))
b = int(input("ingrese numero 2: "))

suma(a,b)

#---- Sin Parametro Con Retorno ----








## Desarrollado por DANNA ALEJANDRA FLOREZ GOMEZ - 1095792553
