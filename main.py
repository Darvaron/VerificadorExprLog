from verifier import Verifier

def main():
    print("Ingrese la expresión lógica a ser verificada:")
    expr = input()
    ver = Verifier()
    valid, chars = ver.evaluate(expr)
    if valid == True:
        print('La expresión es válida')
        print('Los términos son: \n{}'.format(chars))
    else:
        print('La expresión NO es válida')
    
if __name__ == "__main__":
    main()

