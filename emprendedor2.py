#datos para usuario
valor_susc = float(input("Indique el valor de suscripción: $"))
cant_usr = int(input("Indique la cantidad de usuarios: "))
usr_premium = int(input("Indique la cantidad de usuarios premium: "))
gasto_total = float(input("Indique gasto total: $"))

#conversion usuario premium
valor_premium = valor_susc* 1.5

#formula actualizada
utilidades = (valor_susc * cant_usr) + (valor_premium * usr_premium) - gasto_total


#mostrar datos
print(f"El valor de utilidades es: {utilidades}")