section .data
    num1 db 10        ; Primer número (10 en decimal)
    num2 db 3         ; Segundo número (3 en decimal)
    result db 0       ; Variable para almacenar el resultado
    output db '0', 0xA  ; Espacio para el carácter del resultado y un salto de línea

section .text
    global _start

_start:
    ; Cargar los números en registros
    mov al, [num1]
    sub al, [num2]
    mov [result], al

    ; Convertir el resultado a carácter ASCII
    add al, '0'        ; Convertir el número en AL a su representación ASCII
    mov [output], al   ; Guardar el carácter en la cadena output

    ; Llamar a write para mostrar el resultado
    mov eax, 1         ; syscall: write
    mov edi, 1         ; file descriptor: stdout
    mov rsi, output    ; mensaje a imprimir
    mov edx, 2         ; longitud del mensaje
    syscall

    ; Salir del programa
    mov eax, 60        ; syscall: exit
    xor edi, edi       ; código de salida: 0
    syscall
