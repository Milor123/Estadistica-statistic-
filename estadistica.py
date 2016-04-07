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

    def readdata(self):
        # Paste your number in the next variable
        self.data = """
33.1    33.9    34.2    34.5    34.7    35.2
33.4    34.0    34.2    34.5    34.8    35.6
33.6    34.1    34.3    34.6    34.9    35.8
33.7    34.2    34.3    34.6    35.1    36.0
33.4    34.2    34.3    34.6    35.1    36.1
33.8    34.2    34.3    34.7    35.2    36.5"""

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
        self.ampliar()

    def ampliar(self):
        for x in range(self.clase):
            self.ampliado += self.amplitud
            self.valoresampliados.append(self.ampliado)
        # the nex code is for recreate excess
        self.maxofvaloresampliados = '%.1f' % round(max(self.valoresampliados), 1)
        self.maxofvaloresampliados = float(self.maxofvaloresampliados)
        if self.maxofvaloresampliados>self.dmax:
            print max(self.valoresampliados), 'xx' , self.dmax
            print float(max(self.valoresampliados))>float(self.dmax)
            print 'you aqui'

            self.exc += 1
            self.readdata()
            return
        elif self.maxofvaloresampliados<self.dmax:
            self.exc -= 1
            self.readdata()
            return
        # end excess
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


