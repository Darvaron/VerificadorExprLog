from collections import Counter
import re

class Verifier:
    def __init__(self):
        self.expr_list = []
        pass

    def getPar(self, expr):
        '''
        Envia a self.expr_list el contenido entre dos paréntesis,
        incluyendo los paréntesis
        Args:
            expr -- python list que contiene una lista de carácteres
        Returns:
            None
        '''
        expressions = []
        countPar = 0
        parLong = 0
        part = ''
        for p , i in enumerate(expr):
            part += i
            if i == '(':
                parLong += 1
                if p != 0:
                    expressions.append(self.getPar(expr[p:]))
            if i == ')':
                countPar += 1
                if countPar == parLong:
                    break
        self.expr_list.append(part)

    def evaluate_atomic(self, atomic_expr):
        '''
        Evalua una expresión atómica
        Args:
            atomic_expr -- String que contiene una expresión lógica atómica
        Returns:
            val -- Bool que contiene la validez de dicha expresión
        '''
        v = re.search(r'^\(((not )?([a-zA-Z1])( and | or | then | iff )(not )?([a-zA-Z1]))\)$',
                      atomic_expr)

        if v:
            val = True
        else:
            val = False

        #print('La expresión: {} es: {}'.format(atomic_expr, val))
        return val

    def evaluate(self, expr):
        '''
        Eval
        Args:
            expr -- python list que contiene una lista de carácteres
        Returns:
            valid -- bool que contiene la validez de la expresión
            chars -- python list que contiene los términos encontrados
            new_var -- python list que contiene las variables usadas
            new_cond -- python list que contiene los condicionales usados
        '''
        count_par = Counter(expr)
        if not '(' in expr or not ')' in expr or '1' in expr or '[' in expr or ']' in expr:
            return False, None, None, None
        if count_par['('] != count_par[')']:
            return False, None, None, None
        valid = True
        chars = []
        to_pop = []
        print("La expresión a evaluar sera: {}".format(expr))
        expr_chars = list(expr)
        self.getPar(expr_chars)
        self.expr_list = list(set(self.expr_list))
        ended = False        
        while not ended: #Mientras que no exista solo una expresión
            ended = True
            #print('La lista de expresiones actual es: \n{}'.format(self.expr_list))
            for i, exp in enumerate(self.expr_list):
                #print('Entrando con la expresión: {}'.format(exp))
                count_items = Counter(exp)
                if count_items['('] + count_items[')'] == 2: #Si es atómica
                    #print('Cumple como atómica')
                    atomic_val = self.evaluate_atomic(exp)
                    if atomic_val == True and valid == True: #Si es válida
                        for i, st in enumerate(self.expr_list):
                            if exp in st:
                                #print('A {}'.format(self.expr_list[i]))
                                self.expr_list[i] = self.expr_list[i].replace(exp, '1')
                                #print('B {}'.format(self.expr_list[i]))
                    else:
                        #print('El valor cambia en: {}'.format(exp))
                        valid = False
                        break
            #print('Ciclo terminado')
            if valid == False: #Si alguna de las expresiones no es válida
                break
            for i in self.expr_list:
                if len(i) > 1:
                    ended = False
        #print('Las expresiones finales son {}:'.format(self.expr_list))

        chars = expr.split(' ')
        new_chars = []
     
        for posicion in chars: #Mostrando componentes de la expresión lógica
            if not ')' in posicion and not '(' in posicion:
                chars_2 = posicion
                new_chars.append(chars_2)
            if '(' in posicion:
                chars_2=posicion.replace("(","")
                new_chars.append(chars_2)
            if ')' in posicion:
                chars_2=posicion.replace(")","")
                new_chars.append(chars_2)
            
        #print(new_chars) 
        chars = set(new_chars)

        new_var=[]
        new_cond=[]
        for posicion in chars:
            if posicion == 'and'  or posicion == 'or' or posicion == 'then' or posicion == 'iff':
                chars_2 = posicion
                new_cond.append(chars_2)
            else:
                chars_2 = posicion
                new_var.append(chars_2)

        #print(new_var)
        #print(new_cond)
        
        return valid, chars, new_var, new_cond
