#    Trabajo en clase numero 2
#           Entradas

print("\n\n\t\tIngrese los siguiente datos.\n\n")
Cantidad_Inicial_Dinero = int(input("Ingrese la cantidad incial de dinero: "))
Cantidad_Sobrante_Dinero = int(input("\nIngrese la cantidad sobrante de dinero: "))
Porcentaje_Pan = int(input("\nIngrese el costo porcentual del pan: "))
Porcentaje_Jamon = int(input("\nIngrese el costo porcentual del jamon: "))
Porcentaje_Queso = int(input("\nIngrese el costo porcentual del queso: "))
Porcentaje_Tomate = int(input("\nIngrese el costo porcentual del tomate: "))
Porcentaje_Lechuga = int(input("\nIngrese el costo porcentual de la lechuga: "))

#           Procesos

Costo_Total_Productos = Cantidad_Inicial_Dinero-Cantidad_Sobrante_Dinero
Costo_Pan = Costo_Total_Productos*(Porcentaje_Pan/100)
Costo_Jamon = Costo_Total_Productos*(Porcentaje_Jamon/100)
Costo_Queso = Costo_Total_Productos*(Porcentaje_Queso/100)
Costo_Tomate = Costo_Total_Productos*(Porcentaje_Tomate/100)
Costo_Lechuga = Costo_Total_Productos*(Porcentaje_Lechuga/100)

#            Resultados

print("\n\n\tPodra ver el costo de cada ingrediente a continuacion.\n")
print("\nEl costo del pan es de " + str(int(Costo_Pan)) + " colones")
print("\nEl costo del jamon es de " + str(int(Costo_Jamon)) + " colones")
print("\nEl costo del queso es de " + str(int(Costo_Queso)) + " colones")
print("\nEl costo del tomate es de " + str(int(Costo_Tomate)) + " colones")
print("\nEl costo del lechuga es de " + str(int(Costo_Lechuga)) + " colones")
print("\n\n\t\t\t¡Muchas Gracias!\n\n")