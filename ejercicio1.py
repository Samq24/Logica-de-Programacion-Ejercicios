def tabla_multiplicar(numero):
    resultado = f'# Tabla del {numero} #'
    
    print(resultado)
    
    for i in range(1, 11):
        multiplicacion = i * numero
        print(multiplicacion)

tabla_multiplicar(5)

