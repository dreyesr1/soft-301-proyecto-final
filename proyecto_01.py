#
#        David Reyes Rodríguez - Entregable-03
#
#               PROYECTO ENTREGABLE 03
#             SISTEMA DE PAGO DE LA POPS®
#                ---------------------

# DEFINICION DE VARIABLE DE PRECIOS

precio_helado = 0        
precio_batido = 0
desc_pvp = float(.15)   # desc_pvp (descuento PuraVidaPops)
desc_apellido = float(.10) #desc_apellido (descuento por apellido del día)
totaldesc_pvp = 0      # se asigna el valor 0 para que cuando sea llamada no de error
totaldesc_apellido = 0 # se asigna el valor 0 para que cuando sea llamada no de error
cantidad_clientesatendidos = 0
total_vendido_dia = 0
total_helados_dia = 0
total_batidos_dia = 0


# ATENCIO AL CLIENTE Y DEFINIR APELLIDO DEL DIA

print("\nBienvenido al sistema de pago de la POPS®\n")
apellido_condesc = input("\nPof favor ingrese el apellido que contara con descuento el día de hoy: ")
cantidad_clientesporatender = int(input("Digite la cantidad de cliente que se atenderan el día de hoy: "))
print("Cantidad de clientes atentidos: " + str(cantidad_clientesatendidos))
print("\nIniciando con la toma de pedidos...\n")
while cantidad_clientesatendidos < cantidad_clientesporatender:

    # PEDIDO DEL CLIENTE
    cantidad_clientesatendidos = cantidad_clientesatendidos + 1
    print("Pedido del cliente " + str(cantidad_clientesatendidos) + "\n")
    apellido_cliente = input("Apellido del cliente: ")
    opcion_descpvp = input("Tiene tarjeta PuraVidaPops (Si/No): ")
    cantidad_helados = int(input("Cantidad de helados: "))
    sabor_helado = input("Sabor de los helados: ")
    cantidad_batidos = int(input("Cantidad de batidos: "))
    cantfrutas_batidos = int(input("Cantidad de frutas de los batidos: "))

    # CONDICIONES HELADOS Y BATIDOS

    if sabor_helado == "vainilla":
        precio_helado = 600
    elif sabor_helado == "chocolate":
        precio_helado = 700
    elif sabor_helado == "caramelo":
        precio_helado = 750
    elif sabor_helado == "fresa":
        precio_helado = 800
    else:
        print("\nNo contamos con ese sabor.\n")
        cantidad_helados = 0

    if cantfrutas_batidos == 1:
        precio_batido = 1200
    elif cantfrutas_batidos == 2:
        precio_batido = 1300
    elif cantfrutas_batidos == 3:
        precio_batido = 1400
    else:
        print("\nNo contamos con esa cantidad de frutas en los batidos.\n")
        cantidad_batidos = 0

    # OPERACIONES

    total_helados = cantidad_helados * precio_helado           
    total_batidos = cantidad_batidos * precio_batido
    subt_g = total_helados + total_batidos # subt_g (subtotal_general)
    total_g = subt_g
    totaldesc_apellido = subt_g * desc_apellido # en esta variable se almacena el total del descuento por apellido
    totaldesc_pvp = subt_g * desc_pvp       # en esta variable se almacena el total del descuento por tajeta puravidapops
    # CONDICION DESCUENTO POR APELLIDO

    if apellido_cliente == apellido_condesc:
        total_g = total_g - totaldesc_apellido
    else:
        totaldesc_apellido = 0
        total_g = total_g

    # CONDICION DESCUENTO PURAVIDAPOPS

    if opcion_descpvp == "Si":
        total_g = total_g - totaldesc_pvp
    else:
        totaldesc_pvp = 0
        total_g = total_g
   

    # IMPRESION DEL REPORTE

    print("\nLa cuenta total del cliente " + str(cantidad_clientesatendidos) + " es:\n")
    print(str(total_helados) + " colones por helados.")
    print(str(total_batidos) + " colones por batidos.")
    print("Total sin descuento: " + str(subt_g))
    print("Descuento por Apellido del Día: " + str(int(totaldesc_apellido)) + " colones.")
    print("Descuento por PuraVidaPops: " + str(int(totaldesc_pvp)) + " colones.")
    print("Total a pagar: " + str(int(total_g)) + " colones.\n")

    # SUMA DE LOS TOTALES PARA EL REPORTE FINAL DEL DÍA

    total_vendido_dia = total_vendido_dia + total_g
    total_helados_dia = total_helados_dia + cantidad_helados
    total_batidos_dia = total_batidos_dia + cantidad_batidos



print("Reporte final del día para Heladería POPS®\n   ---------------------\n")
print("Total de ventas del día: " + str(int((total_vendido_dia))) + " colones")
print("Total de helados vendidos: " + str(total_helados_dia))
print("Total de batidos vendidos: " + str(total_batidos_dia))
print("\nToma de pedidos finalizada.")