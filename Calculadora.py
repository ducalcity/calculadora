
def EntradaNumero(mensaje):
    count = False
    while not count:                
            try:
                numero = float(input(mensaje))
            except ValueError:
                print("Valor erróneo, introduzca un número.")
            else:
               count = True               
    return numero
    
def SalidaNumero(mensaje,resultado):
    try:
        VerFloatOrInt=resultado%int(resultado)
    except ZeroDivisionError:
            print(mensaje, resultado)
    else:
        if(resultado%int(resultado)==0):
            resultado = int(resultado)
        print(mensaje, resultado)
        
operacion = 0
print("Bienvenido a la calculadora, use el . para determinar el decimal\n")

while ((operacion != "S") and (operacion != "s")):
    operacion=str(input("Seleccione operación: +, -, *, / o S para salir: "))
    if (operacion == "+"):
        suma1=EntradaNumero("Introduzca valor de sumando uno: ")
        suma2=EntradaNumero("Introduzca valor de sumando dos: ")
        SalidaNumero("Resultado de la suma: ",suma1+suma2)
    elif (operacion == "-"):
        resta1=EntradaNumero("Introduzca valor del minuendo: ")
        resta2=EntradaNumero("Introduzca valor del minuendo: ")
        SalidaNumero("Resultado de la resta: ",resta1-resta2)
    elif (operacion == "*"):
        multi1=EntradaNumero("Introduzca valor del multiplicando: ")
        multi2=EntradaNumero("Introduzca valor del multiplicador: ")
        SalidaNumero("Resultado de la multiplicación: ",multi1*multi2)
    elif (operacion == "/"):
        divi1=EntradaNumero("Introduzca valor del dividendo: ")
        divi2=EntradaNumero("Introduzca valor del divisor: ")
        try:
            divi=divi1/divi2
        except ZeroDivisionError:
            print("División por cero = infinito")
        else:
            SalidaNumero("Resultado de la división: ",divi)        
    else:
        print("Opción no válida") 
