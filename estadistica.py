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
    tabla_withvalues = []
    marca_clase = []

    def __init__(self):
        self.readdata()
        self.ampliar()
        self.tablasimple()

    def readdata(self):
        # Paste your number in the next variable
        self.data = """



          737    2462   4327   5633   6627    7428   10241
                 847    2802   4534   5749   6725    7624   12130
                 962    3378   4632   5847   6837    8225
          1548    3894   4484   6082   6964    8327
          1801    4000   4801   6142   7020    8639
          1959    4148   5099   6472   7343    8973
          2412    4189   5321   6588   7417    9166



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
        self.rango = (self.dmax-self.dmin)+(self.exc-1)
        self.n = len(self.data)
        self.clase = round(1+3.322*(log(self.n,10))) # base 10
        self.decimalclase = 1+3.322*(log(self.n,10))
        self.clase = int(self.clase)
        self.amplitud = self.rango/self.clase
        self.exceso = self.rango-self.amplitud*self.clase

        if self.exceso > 0:
            self.exc = self.exceso
            self.exceso = None
            self.readdata()
            return

        self.ampliado = self.dmin
        self.valoresampliados = []
        self.valoresampliados.append(self.dmin)
        self.tabla = []
        self.tabla_withvalues = []
        self.marca_clase= []

    def ampliar(self):
        for x in range(self.clase):
            self.ampliado += self.amplitud
            self.valoresampliados.append(self.ampliado)
        return self.valoresampliados
                # if not max(newampliado)==dmax:
                    # for x in range(exceso):
                        # newampliado[x+1] = newampliado[x+1]+1

    def tablasimple(self):
        newampliado = self.valoresampliados
        for a in range(self.clase):
            if a+1>self.clase:
                break
            valuesoftable = filter(lambda x: x if newampliado[a]<x<newampliado[a+1] else False, self.data)
            self.tabla_withvalues.append({"{}, {}".format(newampliado[a], newampliado[a+1]): valuesoftable}) # firt number of range is < that x and x < that the next
            self.tabla.append({"{}, {}".format(newampliado[a], newampliado[a+1]): len(valuesoftable)}) # firt number of range is < that x and x < that the next
            if valuesoftable:
                self.marca_clase.append((min(valuesoftable)+max(valuesoftable))/2)
            else: # if not found values between of interval class
                self.marca_clase.append(0)
    #print newampliado , 'newampliado'
    def printme(self):
        print self.data, '\n'
        print 'Dato Minimo: {} \nDato Maximo: {}\nRango: {}\nTamano de Clase: {}\nAmplitud: {}\nExceso: {}\nTamano Muestra: {}\nMarca de clase: {}\n'.format(self.dmin, self.dmax, self.rango, self.clase, self.amplitud, self.exceso, self.n, self.marca_clase)
        for v in self.tabla:
            print v

it = estadistica()
it.printme()


