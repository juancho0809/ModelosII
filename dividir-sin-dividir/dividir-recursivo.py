def dividir_recursivo(dividendo, divisor):
    resta = dividendo-divisor
    if divisor == 0:
        return "Inválido"
    if resta < 0:
        return 0
    return 1 + dividir_recursivo(resta, divisor) # Cuenta cuantas veces se realiza la división
    
print(dividir_recursivo(40, 9))
print(dividir_recursivo(40, 5))
print(dividir_recursivo(0,3))