import arrays

# Lista 1
lista_casa = ["Leche",
    "Pan integral",
    "Huevos",
    "Queso",
    "Tomates",
    "Arroz",
    "Manzanas",
    "Papel higiénico",
    "Detergente",
    "Yogur" ]


# Lista 2: Cena con amigos
lista_cena = [
    "Vino tinto",
    "Queso",
    "Pan tipo baguette",
    "Huevos",
    "Aceitunas",
    "Tomates cherry",
    "Pasta",
    "Salsa pesto",
    "Servilletas",
    "Helado"
]



def mostrar_productos_en_comun(primer_cliente: list,
                               segundo_cliente: list)->None:
    '''
    Muestra por consola los productos en común entre dos clientes.

    Parametros: "primer_cliente" -> historial de compra de un cliente.
                "segundo_cliente" -> historial de compra de un cliente.
    
    '''
    compras_en_comun = arrays.calcular_interseccion(primer_cliente, segundo_cliente)

    print(f"Los productos que ambos clientes compraron son: {compras_en_comun}")

def mostrar_productos_exclusivos(primer_cliente: list,
                                 segundo_cliente: list)-> None:
    '''
    Muestra por consola que productos compró exclusivamente cada cliente.

    Parametros: "primer_cliente" -> historial de compra de un cliente.
                "segundo_cliente" -> historial de compra de un cliente.
    '''
    exclusivos_primer_cliente = arrays.calcular_diferencia(primer_cliente, segundo_cliente)

    exclusivos_segundo_cliente = arrays.calcular_diferencia(segundo_cliente, primer_cliente)

    print(f"Los elementos comprados exclusivamente por el primer cliente son: {exclusivos_primer_cliente}.\n--------------------\nLos elementos comprados exclusivamente por el segundo cliento son: {exclusivos_segundo_cliente}")

def mostrar_catalogo(primer_cliente: list,
                     segundo_cliente: list)-> None:
    '''
    Muestra por consola la union entre el historial de compra de los clientes.

    Parametros: "primer_cliente" -> historial de compra de un cliente.
                "segundo_cliente" -> historial de compra de un cliente.
    '''

    historial_compartido = arrays.calcular_union(primer_cliente, segundo_cliente)

    print(f"El catálogo completo es {historial_compartido}")

def recomendar_productos(primer_cliente: list,
                        segundo_cliente: list)-> None:
    '''
    Muestra por consola la recomendación para cada cliente.

    Parametros: "primer_cliente" -> historial de compra de un cliente.
                "segundo_cliente" -> historial de compra de un cliente.
    '''
    exclusivos_primer_cliente = arrays.calcular_diferencia(primer_cliente, segundo_cliente)
    exclusivos_segundo_cliente = arrays.calcular_diferencia(segundo_cliente, primer_cliente)

    print(f"La recomendación para el primer cliente es: {exclusivos_segundo_cliente}\n-------------\nLa recomendación para el segundo cliente es {exclusivos_primer_cliente}")

recomendar_productos(lista_casa, lista_cena)