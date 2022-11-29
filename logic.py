def ponderado(porcentajes):
    
    ponderado = 0

    for porcentaje in porcentajes:
        ponderado += porcentaje

    return ponderado


def faltante_final(notas, porcentajes):

    pond = ponderado(porcentajes)

    if pond > 100 or pond == 100:
        return "revisar notas, el % no puede ser mayor o igual a 100%"
    
    else: 
        sumaNotas = 3
        porcentaje_faltante = 100 - pond

        for i in range(len(notas)):
            sumaNotas -= (notas[i]) * (porcentajes[i] / 100)

        return (sumaNotas) / (porcentaje_faltante / 100)
    

def nota_final(notas, porcentajes):

    pond = ponderado(porcentajes)

    if pond > 100 or pond < 100:
        return "Es necesario que el porcentaje de todas las notas sea 100% para calcular la nota final"
    
    else:
        final = 0

        for i in range(len(notas)):
            final += notas[i] * (porcentajes[i] / 100)

        return final
