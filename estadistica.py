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
60 66 77 70 66 68 57 70 66 52 75 65 69 71 58 66 67 74 61
63 69 80 59 66 70 67 78 75 64 71 81 62 64 69 68 72 83 56
65 74 67 54 65 65 69 61 67 73 57 62 67 68 63 67 71 68 76
61 62 63 76 61 67 67 64 72 64 73 79 58 67 71 68 59 69 70
66 62 63 66
"""

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
                # old code example valuesoftable = filter(lambda x: x if newampliado[a]<=x<newampliado[a+1] else None, self.data)
                valuesoftable = [x for x in self.data if newampliado[a]<=x<newampliado[a+1]]
                self.primeraentrada = False
            elif a==self.clase:
                valuesoftable = [x for x in self.data if newampliado[a]<=x<=newampliado[a+1]]
            else:
                valuesoftable = [x for x in self.data if newampliado[a]<=x<newampliado[a+1]]
            # end if
            # convert to float or int if exist str in list
            if self.id == 1: # float
                valuesoftable = map(float, valuesoftable)
            else: # int
                valuesoftable = map(int, valuesoftable)

            self.tabla_withvalues.append({"{}, {}".format(newampliado[a], newampliado[a+1]): valuesoftable}) # firt number of range is < that x and x < that the next
            self.tabla.append({"{}, {}".format(newampliado[a], newampliado[a+1]): len(valuesoftable)}) # firt number of range is < that x and x < that the next
            self.valuesoftablescomplete.append(len(valuesoftable))
            if valuesoftable:
                self.marca_clase.append((newampliado[a]+newampliado[a+1])/2)
            else: # if not found values between of interval class
                self.marca_clase.append(0)
    #print newampliado , 'newampliado'
    def printme(self, astropy=0):
        print 'Datos ordenados - Organized information\n{}\n'.format(self.data)
        print 'Frecuencia Simple - Simple frequency\n{}\n'.format(self.tfsimple)
        print '(Dato Minimo - Max value) : {}\n(Dato Maximo - Min Value) : {}\n(Viejo Rango - Old range) : {}\n(Rango - Range) : {}\n(Tamano de Clase- Size of class) : {}\n(Vieja Amplitud - Old amplitude) : {}\n(Amplitud - Amplitude) : {}\n(Viejo Exceso - Old excess) : {}\n(Exceso - Excess) : {}\n(Tamano Muestra - Sample size) : {}\n(Marca de clase - Mark of class) : {}\n'.format(self.dmin, self.dmax, self.viejorango, self.rango, self.clase, self.viejoamplitud, self.amplitud, self.viejoexceso, self.exceso, self.n, self.marca_clase)
        print 'El orden es: intervalos, frecuencia absoluta, frecuencia absoluta acumulada, frecuencia relativa, marca de clase'
        print 'Order is: Intervals, Absolute frequency, Cumulative absolute frequency, relative frequency, mark of class'
        if not astropy:
            print '________________________________________________________________________'
        self.absolutf = 0
        self.frecuencia_absoluta_acumulada = []
        self.absolute_frecuency = []
        self.dintervalc = ""
        self.alltable = []
        tmpkey2f = None
        self.frecuencia_relativa = []
        for number, v in enumerate(self.tabla):
            for key,value in v.iteritems():
                self.absolutf += value # acumulate
                self.frecuencia_absoluta_acumulada.append(self.absolutf) # Fi or acumulate
                self.absolute_frecuency.append(value) # fi
                if not self.id:
                    self.dintervalc += key+'+'
                else: # for float numbers
                    tmpkey = key.strip(' ').split(',')
                    tmpkey = map(lambda x: '{:.1f}'.format(float(x)), tmpkey)
                    tmpkey = ', '.join(tmpkey)

                    tmpkey2f = key.strip(' ').split(',')
                    tmpkey2f = map(lambda x: '{:.2f}'.format(float(x)), tmpkey2f)
                    tmpkey2f = ', '.join(tmpkey2f)

                    self.dintervalc += tmpkey+'+'
                self.relativefrequency = float('{:.2f}'.format((float(value)/self.n)*100))
                self.frecuencia_relativa.append(self.relativefrequency)
                if self.id:
                    self.alltable.append((tmpkey2f,value, self.absolutf, str(self.relativefrequency)+' %', self.marca_clase[number]))
                else:
                    self.alltable.append((key,value, self.absolutf, str(self.relativefrequency)+' %', self.marca_clase[number]))
                if not astropy:
                    if self.id:
                        print '|  {}  |  {}  |  {}  |  {} %  |  {}  |'.format(tmpkey2f, value, self.absolutf, self.relativefrequency, self.marca_clase[number])
                    else:
                        print '|  {}  |  {}  |  {}  |  {} %  |  {}  |'.format(key, value, self.absolutf, self.relativefrequency, self.marca_clase[number])
        if not astropy:
            print '_________________________________________________________________________'
            print 'Intervals, fi ,  Fi , fr , xi '
        self.intervalos_label = self.dintervalc[:-1].strip(' ').split('+')
        if astropy:
            self.show_newtable()

    def graphic_histrogram(self):
        from matplotlib import rc as mrc # for update font
        import matplotlib.pyplot as plt

        font = {'family' : 'normal',
                'weight' : 'normal',
                'size'   : 9}

        mrc('font', **font) # change font
        # explaint of plt.subplot(000) 000 correspont to 3 number, the
        # the firts is size of figures, the second is max of figure columns, and
        # the ultimate is the number of figure

        pos = range(len(self.absolute_frecuency))
        # figure with bars fi
        width = 1.0  # gives histogram aspect to the bar diagram
        plt.figure(figsize=(16,10))
        ax1 = plt.subplot(231)
        ax1.set_ylabel('Frecuencia - Frequency')
        #ax1.set_xlabel('Intervalos - Intervals')
        ax1.set_title('Histograma - Histogram')
        # ax1.set_xticks(pos + (width / 2)) this work with numpy
        ax1.set_xticklabels(self.intervalos_label)
        ax1.bar(pos, self.absolute_frecuency, width, color='r')
        for i,j in zip(pos,self.absolute_frecuency):
            ax1.annotate(str(j),xy=(i,j+0)) # this show numbers in the graphic, +1 is for up number, also can +2 +3 +4 blabla

        # figure with lines fi
        pos = range(len(self.absolute_frecuency))
        ax = plt.subplot(232)
        ax.set_ylabel('Frecuencia - Frequency')
        #ax.set_xlabel('Intervalos - Intervals')
        ax.set_title('Frequency polygo - Poligono de Frecuencia')
        ax.set_xticklabels(self.intervalos_label)
        marca_clase = iter(self.marca_clase)
        for i,j in zip(pos,self.absolute_frecuency):
            ax.annotate(str(marca_clase.next()),xy=(i,j+0)) # this show numbers in the graphic, +1 is for up number, also can +2 +3 +4 blabla
        ax.plot(pos, self.absolute_frecuency, '-', linewidth=2)

        # figure with lines Fi (A)
        pos = range(len(self.absolute_frecuency))
        ax3 = plt.subplot(233)
        ax3.set_ylabel('Frecuencia - Frequency')
        ax3.set_xlabel('Intervalos - Intervals')
        ax3.set_title('Ojiva Ascendente - Ascending Ogive')
        ax3.set_xticklabels(self.intervalos_label)
        ax3.plot(pos, self.frecuencia_absoluta_acumulada, '-', linewidth=2)
        for i,j in zip(pos,self.frecuencia_absoluta_acumulada):
            ax3.annotate(str(j),xy=(i,j+0)) # this show numbers in the graphic, +1 is for up number, also can +2 +3 +4 blabla

        # figure with lines Fi (D)
        FI = sorted(self.frecuencia_absoluta_acumulada, reverse=True)
        pos = range(len(FI))
        ax4 = plt.subplot(234)
        ax4.set_ylabel('Frecuencia - Frequency')
        ax4.set_xlabel('Intervalos - Intervals')
        ax4.set_title('Ojiva Descendente - Descending Ogive')
        ax4.set_xticklabels(self.intervalos_label)
        plt.plot(pos, FI, '-', linewidth=2)
        for i,j in zip(pos, FI):
            ax4.annotate(str(j),xy=(i,j+0)) # this show numbers in the graphic, +1 is for up number, also can +2 +3 +4 blabla

        # figure with lines FI (A and D)
        pos = range(len(FI))
        ax5 = plt.subplot(235)
        ax5.set_ylabel('Frecuencia - Frequency')
        ax5.set_xlabel('Intervalos - Intervals')
        ax5.set_title('Ojiva Asendente y Descendente - Ogive Ascending and Descending')
        ax5.set_xticklabels(self.intervalos_label)
        plt.plot(pos, self.frecuencia_absoluta_acumulada, '-', linewidth=2)
        plt.plot(pos, FI, '-', linewidth=2)
        for i,j in zip(pos, FI):
            ax5.annotate(str(j),xy=(i,j+0)) # this show numbers in the graphic, +1 is for up number, also can +2 +3 +4 blabla

        for i,j in zip(pos, self.frecuencia_absoluta_acumulada):
            ax5.annotate(str(j),xy=(i,j+0)) # this show numbers in the graphic, +1 is for up number, also can +2 +3 +4 blabla

        #Figure circle
        labels = []
        ax6 = plt.subplot(236)
        for x,y in zip(self.intervalos_label, self.frecuencia_relativa):
            labels.append(x+' ('+str(y)+'%)')
        sizes = self.frecuencia_relativa
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'blue', 'red', 'orange','green','pink']
        patches, texts = plt.pie(sizes, colors=colors, startangle=90)
        plt.legend(patches, labels, loc="best")
        # Set aspect ratio to be equal so that pie is drawn as a circle.
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    def show_newtable(self):
        from astropy.table import Table, Column
        values=('Intervals', 'fi' ,  'Fi' , 'fr' , 'xi')
        t = Table(rows=self.alltable, names=values)
        print '\n'
        print t

it = estadistica()
it.printme(0) # 0 non use astropy library, 1 Enable astropy
it.graphic_histrogram()
