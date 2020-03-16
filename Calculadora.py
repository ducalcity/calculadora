import math


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
print("\nBienvenido a la calculadora, use el . para determinar el decimal")

while ((operacion != "S") and (operacion != "s")):
    operacion=str(input("\
\n\
    Pulse 1 para suma \n\
    Pulse 2 para resta \n\
    Pulse 3 para multiplicación \n\
    Pulse 4 para división \n\
    Pulse 5 para exponencial \n\
    Pulse 6 para raíz cuadrada \n\
    Pulse S para salir \n\n\
    Seleccione operación: "))
    
    if (operacion == "1"):
        suma1=EntradaNumero("Introduzca valor de sumando uno: ")
        suma2=EntradaNumero("Introduzca valor de sumando dos: ")
        SalidaNumero("\nResultado de la suma: ",suma1+suma2,)
    elif (operacion == "2"):
        resta1=EntradaNumero("Introduzca valor del minuendo: ")
        resta2=EntradaNumero("Introduzca valor del minuendo: ")
        SalidaNumero("\nResultado de la resta: ",resta1-resta2)
    elif (operacion == "3"):
        multi1=EntradaNumero("Introduzca valor del multiplicando: ")
        multi2=EntradaNumero("Introduzca valor del multiplicador: ")
        SalidaNumero("\nResultado de la multiplicación: ",multi1*multi2)
    elif (operacion == "4"):
        divi1=EntradaNumero("Introduzca valor del dividendo: ")
        divi2=EntradaNumero("Introduzca valor del divisor: ")
        try:
            divi=divi1/divi2
        except ZeroDivisionError:
            print("\nDivisión por cero = infinito")
        else:
            SalidaNumero("\nResultado de la división: ",divi) 
    elif (operacion == "5"):
        exp1=EntradaNumero("Introduzca valor del número base: ")
        exp2=EntradaNumero("Introduzca valor del exponente: ")
        SalidaNumero("\nResultado de la potencia: ",exp1**exp2)
    elif (operacion == "6"):
        raiz=EntradaNumero("Introduzca valor del número: ")
        if (raiz < 0):
            print("\nNo es posible la raíz de un número negativo")
        else:
            SalidaNumero("Resultado de la raíz: ",math.sqrt(raiz))
    elif (operacion == ("s" or "S")):
        print("\nSe ha solicitado salida de la aplicación")
    else:
        print("\nOpción no válida, introduza un valor válido del menú o pulse S para salir\n ") 
