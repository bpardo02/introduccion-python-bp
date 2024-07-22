#datos usuario
valor_susc = float(input("Indique el valor de suscripción: $"))
cant_usr = int(input("Indique la cantidad de usuarios: "))
gasto_total = float(input("Indique gasto total: $"))
utilidad_anterior = float(input("Indique utilidades del año anterior: "))

#formula
utilidades = valor_susc * cant_usr - gasto_total
razon = utilidades / utilidad_anterior
razon = round(razon,2)

#mostrar datos razon
print(f"El resultado de la razon es {razon}")