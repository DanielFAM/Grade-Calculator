def validador(porcentajes):
    ponderado = 0

    for porcentaje in porcentajes:
        ponderado += porcentaje

    if ponderado == 100:
        respuesta = "Ponderado al 100%, revisar notas y/o porcentajes"
        print(respuesta)
        breakpoint
    
    elif ponderado > 100:
        respuesta = "ponderado mayor al 100%, revisar notas y/o porcentajes"
        print(respuesta)
        breakpoint

    else:
        return ponderado


def faltante_final(notas, porcentajes):
    respuesta = ''

    ponderado = validador(porcentajes)
    
    
    sumaNotas = 3
    porcentaje_faltante = 100 - ponderado

    for i in range(len(notas)):
        sumaNotas -= notas[i] * (porcentajes[i] / 100)

    respuesta = (sumaNotas) / (porcentaje_faltante / 100)
    
    return respuesta
    

def nota_final(notas, porcentajes):

    final = 0

    for i in range(len(notas)):
        final += notas[i] * (porcentajes[i] / 100)

    return final



if __name__ == "__main__":
    notas = [2.8, 2.5, 3.3]
    porcentajes = [10, 20, 20]

    #print(nota_final(notas, porcentajes))
    #print(faltante_final(notas, porcentajes))
    print(faltante_final(notas, porcentajes))
    print(nota_final(notas, porcentajes))