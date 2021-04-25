from verifier import Verifier
import msvcrt
        
def main():
    print("Programa desarrollado en Python 3.7 por:")
    print("David Armando Rodríguez Varón - 20181020041")
    print("Juan Sebastián Sánchez Tabares - 20181020008")
    print("")
    print("Bienvenido al verificador de expresiones lógicas.")
    print("Este programa realiza la verificación de si una expresión lógica se encuentra bien escrita.")
    print("Para lo cual debe tener en cuenta lo siguiente:")
    print("1. No debe utilizar los siguientes paréntesis para encerrar '{' '}'")
    print("2. De igual forma tampoco los siguientes '[' ']'")
    print("3. Por ende únicamente es válido el uso de los paréntesis. '(' ')'")
    print("4. Como ejemplo de la manera en la que debe escribir la expresión:")
    print("((p and q) then (q iff (r or not s)))")
    print("5. Como se puede observar todo va entre parentesis de forma ordenada.")
    print("6. No son considerados válidos los espacios antes o despues de los paréntesis.")
    print("Si se incumple cualquiera de las condiciones anteriores se considerará como una expresión no válida.")
    print("")
    print("EMPECEMOS")    
    print("Ingrese la expresión lógica a ser verificada:")
    expr = input()
    ver = Verifier()
    valid, chars, variables, conds = ver.evaluate(expr)
    if valid == True:
        print("La expresión es válida")
        print("Los términos son: \n{}".format(chars))
        print("Las variables usadas son: ",variables)
        print("Los condicionales usados son: ",conds)
    else:
        print("La expresión NO es válida")
    
if __name__ == "__main__":
    main()

