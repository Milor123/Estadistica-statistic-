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
    relativefrequency = 0
    def __init__(self):
        self.readdata()

    def readdata(self):
        # Paste your number in the next variable
        self.data = """


52       57       61    64    67    69    74    77    82    88
55       61    63    65    68    72    74    79    84    93"""

        self.data = re.sub(r'([0-9]+[.]{0,1}[0-9]{0,})[\s\t\n]+', r'\g<1>,', self.data)
        self.data = self.data.split(',')


        try:
            self.data = map(int, [x for x in self.data if not x==''])
            self.id=0
        except:
            self.data = map(float, [x for x in self.data if not x==''])
            self.id=1
        # Generate simple frecuency table
        self.new = []
        for x in self.data:
            self.new.append({x:self.data.count(x)})
        self.tfsimple = []
        [self.tfsimple.append(x) for x in self.new if not x in self.tfsimple]
        self.tfsimple.sort()
        # end table
        self.data.sort()
        self.dmin = min(self.data)
        self.dmax = max(self.data)
        self.rango = (self.dmax-self.dmin)+(self.exc)
        self.n = len(self.data)
        self.clase = round(1+3.322*(log(self.n,10))) # base 10
        self.decimalclase = 1+3.322*(log(self.n,10))
        self.clase = int(self.clase)
        if self.id==1:
            self.amplitud = (self.rango/self.clase)
        else:
            self.amplitud = int(round(float(self.rango)/float(self.clase)))
        self.exceso = self.rango-self.amplitud*self.clase
        if self.exceso > 0 and self.flag and self.never:
            self.tmpampliado = self.dmin
            for x in range(self.clase):
                self.tmpampliado += self.amplitud
            if self.tmpampliado >= self.dmax:
                self.never = False
            self.viejorango = self.dmax-self.dmin
            # Nota en viejoamplitud tambien debo considerar los decimales,
            # arreglar despues
            self.viejoamplitud = (self.viejorango/self.clase)
            self.viejoexceso = self.viejorango-(self.viejoamplitud*self.clase)
            self.exc += 1
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
        # the next code is for recreate excess
        if isinstance(max(self.valoresampliados), float):
            self.maxofvaloresampliados = '%.1f' % round(max(self.valoresampliados), 1)
            self.maxofvaloresampliados = float(self.maxofvaloresampliados)
        else:
            self.maxofvaloresampliados = max(self.valoresampliados)
        # if self.maxofvaloresampliados>self.dmax:
            # if self.antibucle or self.antibucle2:
                # self.exc -= 1
                # self.antibucle = False
                # self.flag = False
                # self.readdata()
                # return
        # elif self.maxofvaloresampliados<self.dmax:
            # if self.antibucle or self.antibucle2:
                # self.exc += 1
                # self.antibucle2 = False
                # self.flag = False
                # self.readdata()
                # return
        # self.destroy = True
        # if not self.antibucle and not self.antibucle2 and self.destroy:
            # self.exc += self.exceso
            # self.destroy = False
            # self.readdata()
        # end cycle
        self.tablasimple()
        return self.valoresampliados
                # if not max(newampliado)==dmax:
                    # for x in range(exceso):
                        # newampliado[x+1] = newampliado[x+1]+1

    def tablasimple(self):
        newampliado = self.valoresampliados
        self.primeraentrada = True
        self.valuesoftablescomplete = []
        for a in range(self.clase):
            if a+1>self.clase:
                break
            # for capture values in ranges
            if self.primeraentrada:
                valuesoftable = filter(lambda x: x if newampliado[a]<=x<newampliado[a+1] else False, self.data)
                self.primeraentrada = False
            elif a==self.clase:
                valuesoftable = filter(lambda x: x if newampliado[a]<x<=newampliado[a+1] else False, self.data)
            else:
                valuesoftable = filter(lambda x: x if newampliado[a]<=x<newampliado[a+1] else False, self.data)
            # end if
            self.tabla_withvalues.append({"{}, {}".format(newampliado[a], newampliado[a+1]): valuesoftable}) # firt number of range is < that x and x < that the next
            self.tabla.append({"{}, {}".format(newampliado[a], newampliado[a+1]): len(valuesoftable)}) # firt number of range is < that x and x < that the next
            self.valuesoftablescomplete.append(len(valuesoftable))
            if valuesoftable:
                self.marca_clase.append((newampliado[a]+newampliado[a+1])/2)
            else: # if not found values between of interval class
                self.marca_clase.append(0)
    #print newampliado , 'newampliado'
    def printme(self):
        print 'Datos ordenados\n{}\n'.format(self.data)
        print 'Frecuencia Simple\n{}\n'.format(self.tfsimple)
        print 'Dato Minimo: {} \nDato Maximo: {}\nViejo Rango: {}\nRango: {}\nTamano de Clase: {}\nVieja Amplitud: {}\nAmplitud: {}\nViejo Exceso: {}\nExceso: {}\nTamano Muestra: {}\nMarca de clase: {}\n'.format(self.dmin, self.dmax, self.viejorango, self.rango, self.clase, self.viejoamplitud, self.amplitud, self.viejoexceso, self.exceso, self.n, self.marca_clase)
        print 'El orden es: intervalos, frecuencia absoluta, frecuencia absoluta acomulada, frecuencia realtiva, marca de clase'
        print '________________________________________________________________________'
        self.absolutf = 0
        for number, v in enumerate(self.tabla):
            for key,value in v.iteritems():
                self.absolutf += value
                self.relativefrequency = float('{:.2f}'.format((float(value)/self.n)*100))
                print '|  {}  |  {}  |  {}  |  {} %  |  {}  |'.format(key,value, self.absolutf, self.relativefrequency, self.marca_clase[number])
        print '_________________________________________________________________________'
it = estadistica()
it.printme()


