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
## Desarrollado por DANNA ALEJANDRA FLOREZ GOMEZ - 1095792553
