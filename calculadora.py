def sumar(a, b):
    #los espacios son importantes
    c=a+b
    return c

def restar(a, b):
    return a -b

def multi(a,b):
    return a*b

def div_entera(a, b):
    if b == 0:
        print("error div /0")
        return
    return a//b#operador de div entera

def division(a, b):
    if b == 0:
        print("error div /0")
        return
    return a/b#operador de div normal

def modulo(a,b):
    if b == 0:
        print("error div /0")
        return
    return a%b#operador de modulo

def potencia (a,b):
    return a**b

def main():
    op = 0
    while op != 8:
        print("ingresa dos valores")
        x = int(input())
        y = int(input())
        print("1. sumar \n 2.restar\n 3.division entera")
        print("4.division\n 5.modulo\n 6.potencia\n 7.multiplicacion\n8.Salir\n\n")

        op = int(input())
        print("\n\nresultado")
        if op==1:
            print(sumar(x, y))
        elif op == 2:
            print(restar(x, y))
        elif op == 3:
            print(div_entera(x, y))
        elif op == 4:
            print(division(x, y))
        elif op == 5:
            print(modulo(x, y))
        elif op == 6:
            print(potencia(x, y))
        elif op == 7:
            print(multi(x, y))
        elif op == 8:
            break
        else:
            print("opcion no valdia")

if __name__ == "__main__":#comprueba que exista una funcion main
    main()
"""
agreagr a la funcion menu una funcion para salir del programa
"""
