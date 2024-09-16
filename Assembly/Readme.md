## Assembly Workshop

Workshop by

- Juan Diego Lozada 20222020014
- Cesar Pulido 20222020048

**Compiler: https://onecompiler.com/assembly/42sawaekg**

This workshop is about assembly, the purpose is present a code in assembly

We decide to make a code about subtraction in assembly and how the programm works

The explanation about the code ithe next one: 

```python
section .data
    num1 db 10        
    num2 db 3         
    result db 0       
    output db '0', 0xA 
```
The section data, define the data will be on memory, and define byte (db) for the values 10 and 3, and reserve a byte for save the result of subtraction, which is 0 (for now). output define a string of 2 bytes, 0 is the caracter in ASCII, and 0xA, is the jump line 

```python
section .text
    global _start
```
The section text, contain the executable code, and global_start, indicate the entry point of the programm
```
_start:
    
    mov al, [num1]
    sub al, [num2]
    mov [result], al
```
Start the label, and (mov al) charge the value saved in 'num1' on the record '__AL__', a record 8 bits

And, in 'sub al' we subtract the value saved in 'num2' from the value saved in '__AL__', after the operation, '__AL__' will contain 7, finally, in 'mov [result]' the result is moved from '__AL__' to the variable '__result__'

```
    add al, '0'        
    mov [output], al   
```
in '__add al__' convert the numeric value '__AL__' to his caracter ASCII respectively 
And '__mov__' Save the caracter on the first position of the string

```
    resultado
    mov eax, 1         
    mov edi, 1         
    mov rsi, output    
    mov edx, 2        
    syscall

```
- '__mov eax, 1__' This number identify the syscall (write), which is used to write on a file

- '__mov edi, 1__' specify the file descriptor (stdout)

- '__mov rsi, output__' Put the adress about the string 'output', the string will be printed

- '__mov edx, 2__' specify the length of data to write (1 byte for the caracter, 1 for jump line)

- '__mov edx, 2__' specify the length of data to write (1 byte for the caracter, 1 for jump line)

- '__syscall__'Invokes the specified syscall in EAX , using the other registers to provide the arguments. This writes the output string to the console.

```
    mov eax, 60        
    xor edi, edi       
    syscall
```
- __mov eax, 60__ Places the number 60 in the EAX register. This number identifies the exit syscall, which is used to exit the program.
- __xor edi, edi__ Sets the EDI value to 0 (exit code 0, indicating success). xor edi, edi is an efficient way to set EDI to zero.
- __syscall__ Invokes the exit syscall, ending the execution of the program.
