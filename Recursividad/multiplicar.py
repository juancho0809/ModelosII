
def multiplicacion(cociente,operador):
    resultado = 0
    for _ in range(operador):
        resultado += cociente
    return resultado
 

print(multiplicacion(3,4))
print(multiplicacion(5,5))

