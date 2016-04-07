# /usr/bin/env python 2.7
# -*- coding: utf-8 -*-
# Author: Mateo Bohorquez
# Description: Algorithm for simple calculus in statistical
# How do I use this? Paste the data with numbers,
# spaces or jump of line in self.data, example: """ 444 777 5551 """ field

# for spanish users: Como uso esto? Pega los datos con numeros,
# espacios o saltos de linea en el campo self.data, ejemplo:  """ 444 77 555 33 """

import re
from math import log
class estadistica(object):
    data = """"""
    dmin = 0
    dmax = 0
    rango = 0
    n = 0
    clase = 0
    amplitud = 0
    exceso = None
    decimalclase = 0.0
    ampliado = 0
    exc = 0
    newampliado = []
    tabla = []
    viejorango = None
    viejoamplitud = []
    viejoexceso = None
    tabla_withvalues = []
    marca_clase = []
    flag = True
    antibucle = True
    antibucle2 = True
    never = True
    def __init__(self):
        self.readdata()

    def readdata(self):
        # Paste your number in the next variable
        self.data = """


1959         4534         7020         6725         6964         7428
2802         2462         4000        3378         7343         4189
2412         7624         1548        4801         737         5321
6837        8639         7417         6082         10241         962
5099        6627         4484         5633         4148         6588
6472        8327         8225         6142         12130         9166
5749        1801         4632         9359          8973         849
3894         5847         4327

"""

        self.data = re.sub(r'([0-9]+[.]{0,1}[0-9]{0,})[\s\t\n]+', r'\g<1>,', self.data)
        self.data = self.data.split(',')


        try:
            self.data = map(int, [x for x in self.data if not x==''])
        except:
            self.data = map(float, [x for x in self.data if not x==''])
        self.data.sort()
        self.dmin = min(self.data)
        self.dmax = max(self.data)
        self.rango = (self.dmax-self.dmin)+(self.exc)
        self.n = len(self.data)
        self.clase = round(1+3.322*(log(self.n,10))) # base 10
        self.decimalclase = 1+3.322*(log(self.n,10))
        self.clase = int(self.clase)
        self.amplitud = (self.rango/self.clase)
        self.exceso = self.rango-self.amplitud*self.clase
        if self.exceso > 0 and self.flag and self.never:
            self.tmpampliado = self.dmin
            for x in range(self.clase):
                self.tmpampliado += self.amplitud
            if self.tmpampliado >= self.dmax:
                self.never = False
            self.viejorango = self.dmax-self.dmin
            self.viejoamplitud = (self.viejorango/self.clase)
            self.viejoexceso = self.viejorango-(self.viejoamplitud*self.clase)
            self.exc = self.exceso
            self.exceso = None
            self.flag = False
            self.readdata()
            return

        self.ampliado = self.dmin
        self.valoresampliados = []
        self.valoresampliados.append(self.dmin)
        self.tabla = []
        self.tabla_withvalues = []
        self.marca_clase= []
        self.ampliar()

    def ampliar(self):
        for x in range(self.clase):
            self.ampliado += self.amplitud
            self.valoresampliados.append(self.ampliado)
        #the next code is for recreate excess
        if isinstance(max(self.valoresampliados), float):
            self.maxofvaloresampliados = '%.1f' % round(max(self.valoresampliados), 1)
            self.maxofvaloresampliados = float(self.maxofvaloresampliados)
        else:
            self.maxofvaloresampliados = max(self.valoresampliados)
        if self.maxofvaloresampliados>self.dmax:
            if self.antibucle or self.antibucle2:
                self.exc -= 1
                self.antibucle = False
                self.flag = False
                self.readdata()
                return
        elif self.maxofvaloresampliados<self.dmax:
            if self.antibucle or self.antibucle2:
                self.exc += 1
                self.antibucle2 = False
                self.flag = False
                self.readdata()
                return
        # end cycle
        self.tablasimple()
        return self.valoresampliados
                # if not max(newampliado)==dmax:
                    # for x in range(exceso):
                        # newampliado[x+1] = newampliado[x+1]+1

    def tablasimple(self):
        newampliado = self.valoresampliados
        for a in range(self.clase):
            if a+1>self.clase:
                break
            valuesoftable = filter(lambda x: x if newampliado[a]<=x<newampliado[a+1] else False, self.data)
            self.tabla_withvalues.append({"{}, {}".format(newampliado[a], newampliado[a+1]): valuesoftable}) # firt number of range is < that x and x < that the next
            self.tabla.append({"{}, {}".format(newampliado[a], newampliado[a+1]): len(valuesoftable)}) # firt number of range is < that x and x < that the next
            if valuesoftable:
                self.marca_clase.append((min(valuesoftable)+max(valuesoftable))/2)
            else: # if not found values between of interval class
                self.marca_clase.append(0)
    #print newampliado , 'newampliado'
    def printme(self):
        print self.data, '\n'
        print 'Dato Minimo: {} \nDato Maximo: {}\nViejo Rango: {}\nRango: {}\nTamano de Clase: {}\nVieja Amplitud: {}\nAmplitud: {}\nViejo Exceso: {}\nExceso: {}\nTamano Muestra: {}\nMarca de clase: {}\n'.format(self.dmin, self.dmax, self.viejorango, self.rango, self.clase, self.viejoamplitud, self.amplitud, self.viejoexceso, self.exceso, self.n, self.marca_clase)
        for v in self.tabla:
            print v

it = estadistica()
it.printme()


