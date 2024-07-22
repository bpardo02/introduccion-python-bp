#datos para usuario
valor_susc = float(input("Indique el valor de suscripción: $"))
cant_usr = int(input("Indique la cantidad de usuarios: "))
gasto_total = float(input("Indique gasto total: $"))

#formula
utilidades = valor_susc * cant_usr - gasto_total

#mostrar datos
print(f"El valor de utilidades es: {utilidades}")