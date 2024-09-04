def dividir_recursivo(dividendo, divisor, iteraciones = 0):
    resta = dividendo-divisor
    if resta < 0:
        return iteraciones
    if resta == 0:
        return iteraciones + 1
    return dividir_recursivo(resta, divisor, iteraciones + 1)
    
print(dividir_recursivo(40, 9))
print(dividir_recursivo(40, 5))