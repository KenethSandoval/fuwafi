validOperations = ["+", "-", "/", "*"]
validExpressionRegex = "." 

def welcome():
    pass

def cli():
    return input("calculador >> ")

def result(w):
    print(f'respuesta >> {w}')

def instructions(arg):
    if arg[0] in validOperations:
        print(arg)
    elif arg == "quit":
        print("Bye...")
        exit()

def main():
    #while 1:
    option = cli()
    characters = "()"

    option = ''.join( x for x in option if x not in characters)
    print(option)
        #instructions(option)
    
main()
