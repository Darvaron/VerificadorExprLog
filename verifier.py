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
        v = re.search(r'^\(((not )?([a-zA-Z1])( and | or | then | iff )(not )?([a-zA-Z1]))\)$',
                      atomic_expr)

        if v:
            val = True
        else:
            val = False

        print('La expresión: {} es: {}'.format(atomic_expr, val))
        return val

    def evaluate(self, expr):
        '''
        Eval
        Args:
            expr -- python list que contiene una lista de carácteres
        Returns:
            valid -- bool que contiene la validez de la expresión
            chars -- listo que contiene tuplas de char - tipo
        '''
        count_par = Counter(expr)
        if not '(' in expr or not ')' in expr or '1' in expr:
            return False, ['No es una entrada válida']
        if count_par['('] != count_par[')']:
            return False, ['No es una entrada válida']
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
        chars = list(set(chars))
        
        return valid, chars
