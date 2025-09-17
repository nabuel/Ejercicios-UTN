#Se piden los datos al consumidor.
metros_consumidos = int(input("Ingrese la cantidad de metros cuadrados consumidos: "))
categoria = str(input("Ingrese su categoria de cliente (Residencial/Comercial/Industrial): "))

#Se calcula el precio base de la tarifa para luego calcular las bonificaciones.
costo_por_consumo = metros_consumidos * 200
tarifa_base =  costo_por_consumo + 7000

#Se aplica bonificación según tipo de cliente.
tarifa_final = tarifa_base
recargo = 0
bonificacion = 0


match categoria:
    case "Residencial":
        #Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo
        if metros_consumidos < 30: 
            bonificacion = costo_por_consumo * 0.1
        #Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
        elif metros_consumidos > 80: 
            recargo = costo_por_consumo * 0.15

    case "Comercial":
        #Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
        if metros_consumidos < 50: 
            recargo = costo_por_consumo * 0.05
        #Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
        elif metros_consumidos > 300: 
            bonificacion = costo_por_consumo * 0.12
        #Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
        elif metros_consumidos > 150:
            bonificacion = costo_por_consumo * 0.08


    case "Industrial":
        #Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
        if metros_consumidos < 200: 
            recargo = costo_por_consumo * 0.1
        #Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
        elif metros_consumidos > 1000: 
            bonificacion = costo_por_consumo * 0.3
        #Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del consumo.
        elif metros_consumidos > 500: 
            bonificacion = costo_por_consumo * 0.2


#Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
if tarifa_base < 35000 and categoria == "Residencial":
    bonificacion = bonificacion + (tarifa_base * 0.05)

#Valor de la tarifa sin calcular el IVA.
tarifa_final = tarifa_base + bonificacion - recargo

#Valor del IVA.
iva = tarifa_final * 0.21

#Aplica el 21% de recargo del IVA.
total_a_pagar = tarifa_final + iva

print(f"El subtotal sin recargo y bonificaciones es de: {tarifa_base}$ \nEl recargo es de {recargo}$\nLa bonificación es de {bonificacion}$\nEl subtotal con recargo y bonificaciones es de: {tarifa_final}$\nRecargo del IVA {iva}$\nTotal a pagar es de {total_a_pagar}$")
