import re

regexInput = "\(([^()]+\d)\)"
validInput = re.compile(regexInput)

def welcome():
    pass

def cli():
    return input("calculador >> ")

def result(w):
    print(f'respuesta >> {w}')

"""
operations se encarga de realizar las operaciones correspondientes
para cada una de la entrada dada en el cli
"""
def operations(op):
    # sustituimos los parentesis de la entrada
    op = re.sub("[()]", "", op)
   
    # separamos cada instruccion por el espacio
    op = op.split(" ")

    try: 
        numero1 = int(op[1])
        numero2 = int(op[2])
        if op[0] == "+":
            result(numero1 + numero2)
        elif op[0] == "-":
            result(numero1 - numero2)
        elif op[0] == "*":
            result(numero1 * numero2)
        elif op[0] == "/":
            result(numero1 / numero2)
        else: 
            result("ERROR! Expresion no valida")
    except ZeroDivisionError:
        result("ERROR! Division entre cero")
    except IndexError:
        result("ERROR! Expresion no valida")
    
"""
commands interpreta cada uno de los comandos ingresados en el cli
"""
def commands(arg):
    if validInput.match(arg):
        operations(arg)
    else:
        result("ERROR! Expresion no valida")
        

def main():
    while 1:
        option = cli()

        if option != "quit":
            commands(option)
        else:
            print("Bye...")
            exit()
    
main()
