#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO.



listaProductos_precios = {
    "Muebles":500000,
    "Sabanas":80000,
    "Televisor":2000000,
    "Portatil":1100000,
}

for llaves , valor in listaProductos_precios.items():
    print(llaves , valor )
    
    
    
print("¿Que producto y cantidad deseas? ")
producto = input("producto ")
cantidad = input("cantidad ")


if producto in listaProductos_precios:
    print(f"producto: {producto} y cantidad: {cantidad} equivale a: ", listaProductos_precios[producto] * cantidad)


