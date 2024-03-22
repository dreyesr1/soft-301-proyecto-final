#
#        David Reyes Rodríguez - Entregable-03
#
#               PROYECTO ENTREGABLE 03
#             SISTEMA DE PAGO DE LA POPS®
#                ---------------------

# DEFINICION DE VARIABLE DE PRECIOS

precio_vainilla = 600        
precio_chocolate = 700          
precio_caramelo = 750        
precio_fresa = 800   
precio_batidos_1f = 1200
precio_batidos_2f = 1300
precio_batidos_3f = 1400
desc_pvp = float(.15)   # desc_pvp (descuento PuraVidaPops)
desc_apellido = float(.10) #desc_apellido (descuento por apellido del día)
totaldesc_pvp = 0      # se asigna el valor 0 para que cuando sea llamada no de error
totaldesc_apellido = 0 # se asigna el valor 0 para que cuando sea llamada no de error
cantidad_clientesatendidos = 0

# ATENCIO AL CLIENTE Y DEFINIR APELLIDO DEL DIA

print("\nBienvenido al sistema de pago de la POPS®\n\n")
apellido_condesc = input("\nPof favor ingrese el apellido que contara con descuento el día de hoy: ")
print("Cantidad de clientes atentidos: " + str(cantidad_clientesatendidos))
def atencion_cliente(opcion_atencio):

    # PEDIDO DEL CLIENTE

    print("Pedido del cliente")
    cantidad_vainilla = int(input("Cantidad de helados de vainilla: "))   
    cantidad_chocolate = int(input("Cantidad de helados de chocolate: "))    
    cantidad_batidos = int(input("Cantidad de batidos: "))                

    # OPERACIONES

    total_vainilla = cantidad_vainilla * precio_vainilla        
    total_chocolate = cantidad_chocolate * precio_chocolate        
    total_batidos_1f = cantidad_batidos * precio_batidos_1f        
    subt_g = total_vainilla + total_chocolate + total_batidos_1f    # subt_g (subtotal_general)

    # CONDICION

    opcion = input("\nEl cliente cuenta con una tarjeta de cliente frecuente 'PuraVidaPops' (Sí/No): ")
    if opcion == "Si":
        totaldesc_pvp = subt_g * desc_pvp       # en esta variable se almacena el total del descuento
        total_g = subt_g - totaldesc_pvp
    elif opcion == "No":
        total_g = subt_g
    else:
        print("\n*La opcion que ingresó no es valida. Se interpreta como un 'No'.*")
        total_g = subt_g                        # la tomo como si fuera un "no"

    # IMPRESION DEL REPORTE

    print("\nLa cuenta total del cliente es:\n")
    print(str(total_vainilla) + " colones por helados de vainilla.")
    print(str(total_chocolate) + " colones por helados de chocolate.")
    print(str(total_batidos_1f) + " colones por batidos.")
    print("Total sin descuento: " + str(subt_g))
    print("Descuento por PuraVidaPops: " + str(int(totaldesc_pvp)) + " colones.")
    print("Total a pagar: " + str(int(total_g)) + " colones.\n")



opcion_atencion = input("\nDesea atender a un cliente (Si/No): ")
if opcion_atencion == "Si":
    atencion_cliente(opcion_atencio="Si")
elif opcion_atencion == "No":
    print("ERROR")