
def cargar_consulta(nombre_paciente: str, 
                    peso: float, 
                    altura: float, 
                    temperatura: float, 
                    presion_sistolica: float, 
                    presion_diastolica: float) -> None:
    
    fiebre = definir_fiebre(temperatura)

    analisis_imc = calcular_calorias(peso,altura)

    analisis_presion = calcular_presion(presion_sistolica, presion_diastolica)

    diagnostico = f"""Diagnóstico del paciente {nombre_paciente}:
    Peso: {analisis_imc}
    Temperatura: {fiebre}
    Presión: {analisis_presion}"""

    print(diagnostico)

def definir_fiebre(temperatura: float) -> str:
    if temperatura > 41:
        fiebre = "Muy alta."
    elif temperatura > 39:
        fiebre = "Alta."
    elif temperatura >= 38:
        fiebre = "Fiebre moderada."
    elif temperatura > 37.3:
        fiebre = "Febrícula."
    else:
        fiebre = "Temperatura normal."
    
    return(fiebre)

def calcular_calorias(peso: float,
                    altura: float) -> str:
    imc = peso / (altura ** 2)
    if imc < 18.5:
        analisis_imc = "Es necesario aumentar ingesta calórica."
    elif imc < 25:
        analisis_imc = "Peso equilibrado."
    else:
        analisis_imc = "Es necesario disminuir ingesta calórica."
    
    return(analisis_imc)

def calcular_presion(presion_sistolica: float,
                    presion_diastolica: float) -> str:

    if presion_sistolica < 90 or presion_diastolica < 60:
        analisis_presion = "Baja"
    elif presion_sistolica > 140 or presion_diastolica > 90:
        analisis_presion = "Alta"
    else:
        analisis_presion = "Normal"
    
    return analisis_presion