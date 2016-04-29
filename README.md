#Descriptive statistics

<div id='Description'/>

### Description
-----------------------------

This algorithm allows you to do calculations in `statistic descriptive` in one way very easy, because you only need paste the data and run the script

**What can calculate?:**

| Information  | Tables with  | Figures  | Examples |
| -------------|:-----------:|-----------| --------:|
| Min value | Absolute Frecuency | Histogram | [See Figures](#Figures)|
| Max value | Mark of class | Frequency polygon|   [Results - Resultados](#Results-Step) |
| Old range (Range) | Relative Frecuency - Frecuencia Relativa |Ascending Ogive - Ojiva Ascendente 
| Range (New Range) | Cumulative Absolute Frequency |Descending Ogive|
| Size of interval class | | Ogive Ascending and Descending 
| Old amplitude (Amplitude) | | Circle Dragram
| Amplitude (New Amplitude)
| Old excess (Excess)
| Excess (New Excess)
| Maximun sample size
| Mark of class
| Simple frequency

<br/>
<div id='Table'/>
## Table of Contents
1.  [Description](#Description)
2.  [Table of contens](#Table)
3.  [Requeriments](#Requeriments)
    1.  [Basic requeriments](#BRequeriments)
    2.  [How install pip](#Pipinstall)
4.  [How use](#Howuse)
    1.  [First step](#First-Step)
    2.  [Example](#Example)
    3.  [Optional step](#Optional-Step)
    4.  [Results](#Results-Step)
5. [Copyright and license](#License)

<br/>
<div id='Requeriments'/>
### Requeriments
---------------------------------

You must have a version of python as indicated below or greater, but `but this does not support python 3x`

<div id='BRequeriments'/>

*   **python 2.7x**
    *   Windows : [Download](https://www.python.org/downloads/release/python-279/)
    *   Debian / Ubuntu: `sudo apt-get install python2.7`
*   **matplotlib** (_This is included in python2.7+_)
    *   `pip install matplotlib`
    *   Debian / Ubuntu : `sudo apt-get install python-matplotlib`
    *   Fedora / Redhat : `sudo yum install python-matplotlib`
*   **numpy** (_This is included in matplotlib_)
    *   `pip install numpy`
*   **astropy** _Optional Instalation_
    *   `pip install --no-deps astropy`
  
<br/>
<div id='Pipinstall'/>
**How install pip?**
* [**Windows**](http://stackoverflow.com/a/12476379/4941927)
* **Linux or windows**, after python install you must type in cmd or terminal `easy_install pip` - Despues de instalar python debes escribir en el cmd or terminal `easy_install pip`
* [**Installation documentation**](https://pip.pypa.io/en/stable/installing/)

<br/>
<div id='Howuse'/>
###How use the algorithm?##
------------------------------------------------------

<div id='First-Step'/>
**First Step**

Copy the text of `estadistica.py` in any text editor, in windows for example you could use `notepad`, then paste it and save the file as *any_name.py*, with `.py` extension.

Now follows these steps: 

> You must write the information within `self.data`, if you need exact calculation, you should add a decimal value in any number, example the first number is 60, change it by 60.0 and then the rest will be changed automatically when you run the script

You can add - Puedes Agregar:

* numbers - numeros
* spaces - espacios
* jump of lines - saltos de linea
* dot for decimals (decimal numbers) - puntos para decimales (numeros decimales)

**Warning: Don't Use commas `,`**

<div id='Example'/>

##### Example:

```
self.data = """
60 66 77 70 66 68 57 70
      66 52 75 65 69 71 58 66 67 74 61
63 69 80 59 66        70 67 
78 75 64 71 81 62 64 69 68 72 83 56
65 74 67 54 65 65 69 61 67 73 57 62     67 68 63 
67 71 68 76
   61 62 63 76 61 67
   67 64 72 64 73 79 58 67 71 68 59 69 70
66 62 
63 66

"""
```
<div id='Optional-Step'/>
**Optional Step**

if you want see a pretty tables:

sees the penultimate line of code and change `it.printme(0)` by `it.printme(1)`, because 1 enables astropy tables, which are nice, however if you cant install astropy could use 0 by default.

* [See Astropy Table](#Astropy) 
* [See Default Table](#Default)

**Executing file**

How execute file?:

*   **Windows**, [see - ver](https://stackoverflow.com/questions/1522564/how-do-i-run-a-python-program)
*   **Linux**, [see - ver](https://askubuntu.com/questions/244378/run-python-in-terminal)
*   **Mac osx**, [see - ver](https://stackoverflow.com/questions/21492214/how-to-run-python-script-on-terminal)

<div id='Results-Step'/>
##### Information Obtained After Execute:

```
Datos ordenados - Organized information
[52, 54, 56, 57, 57, 58, 58, 59, 59, 60, 61, 61, 61, 61, 62, 62, 62, 62, 63, 63, 63, 63, 64, 64, 64, 64, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 69, 69, 69, 69, 69, 70, 70, 70, 70, 71, 71, 71, 71, 72, 72, 73, 73, 74, 74, 75, 75, 76, 76, 77, 78, 79, 80, 81, 83]

Frecuencia Simple - Simple frequency
[{52: 1}, {54: 1}, {56: 1}, {57: 2}, {58: 2}, {59: 2}, {60: 1}, {61: 4}, {62: 4}, {63: 4}, {64: 4}, {65: 4}, {66: 7}, {67: 9}, {68: 5}, {69: 5}, {70: 4}, {71: 4}, {72: 2}, {73: 2}, {74: 2}, {75: 2}, {76: 2}, {77: 1}, {78: 1}, {79: 1}, {80: 1}, {81: 1}, {83: 1}]

(Dato Minimo - Max value) : 52
(Dato Maximo - Min Value) : 83
(Viejo Rango - Old range) : 31
(Rango - Range) : 32
(Tamano de Clase- Size of class) : 7
(Vieja Amplitud - Old amplitude) : 4
(Amplitud - Amplitude) : 5
(Viejo Exceso - Old excess) : 3
(Exceso - Excess) : -3
(Tamano Muestra - Sample size) : 80
(Marca de clase - Mark of class) : [54, 59, 64, 69, 74, 79, 84]

El orden es: intervalos, frecuencia absoluta, frecuencia absoluta acomulada, frecuencia realtiva, marca de clase
Order is: Intervals, Absolute frequency, Cumulative absolute frequency, relative frequency, mark of class
```
<br/>
<div id='Astropy'/>
**Astropy Table**
```
Intervals  fi  Fi    fr    xi
--------- --- --- ------- ---
   52, 57   3   3  3.75 %  54
   57, 62  11  14 13.75 %  59
   62, 67  23  37 28.75 %  64
   67, 72  27  64 33.75 %  69
   72, 77  10  74  12.5 %  74
   77, 82   5  79  6.25 %  79
   82, 87   1  80  1.25 %  84
```
<br/>
<div id='Default'/>
**Default Table**
```
________________________________________________________________________
|  52, 57  |  3  |  3  |  3.75 %  |  54  |
|  57, 62  |  11  |  14  |  13.75 %  |  59  |
|  62, 67  |  23  |  37  |  28.75 %  |  64  |
|  67, 72  |  27  |  64  |  33.75 %  |  69  |
|  72, 77  |  10  |  74  |  12.5 %  |  74  |
|  77, 82  |  5  |  79  |  6.25 %  |  79  |
|  82, 87  |  1  |  80  |  1.25 %  |  84  |
_________________________________________________________________________
Intervals, fi ,  Fi , fr , xi 
```
<br/>
**Figures - Figuras**
<div id='Figures'/>
<img src="https://goo.gl/8Lbb9u" alt="Figures" width="780" height="580" border="10" />

<div id='License'/>
## Copyright and license

Code copyright 2016-2020 Mateo Bohorquez. Code released under the [MIT license](https://github.com/Milor123/Estadistica-statistic-/blob/master/LICENSE)
