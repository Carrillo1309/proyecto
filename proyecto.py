import pandas as pd#importar pandas
import matplotlib.pyplot as plt#importar matplotlib, el cual se usa para graficar
import numpy as np#inportar la libreria numpy
datos = pd.read_csv("CasosNuevosConSintomas.csv")
#aca se llama el archivo el cual se quiere usar 
df = pd.DataFrame(datos)#aca de hace un dataframe para que los datos esten en un mejor orden y se puedan sacar de una forma mas facil
fecha = datos.iloc[0:,[-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]]#aca se sacan las fecha las cuales se van a usar, en este caso las ultimas 2 semanas
contenedor=[]#se forma una variable la cual tenga vacio para luego meter datos
for i in fecha:#se recoore las fechas las cuales s van a usar 
    if i not in contenedor:
        contenedor.append(i)#aca se agregan las fechas y quedan como una lista 
contagios = datos.iloc[0:16,[-14,-13,-12,-11,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]]#aca se obtiene los valores los cuales se van a usar para graficar
print("1)Arica y Parinacota","2)Tarapacá","3)Antofagasta","4)Atacama","5)Coquimbo","6)Valparaíso","7)Metropolitana","8)O’Higgins","9)Maule","10)Ñuble","11)Biobío","12)Araucanía","13)Los Ríos","14)Los Lagos","15)Aysén","16)Magallanes")
print("17)para ver la region con mas contagio o menos contagios")#aca se ponen todas las regiones para que el usuario las lea
x = int(input("ingrese un numero de la ragión: "))#aca el usuario ingresa el numeor el cual decea visualizar 
while x>17 or x<0:#aca se hace un wile para que el usuario ingrese un numero el cual este en las regiones
    print("ingrese nuevamnete un numero correcto:")
    x= int(input())
if x == 1:#aca entra la opcion la cual ingresa el usuario 
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")#luego se hacen 2 variables las cuales son 1 de un grafico acumulativo y la otra de uno no acumulativo 
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[0])# aca se grafican las fechas en x y se selecciona la primera fila de los contagiados 
        plt.show()#se muestra el grafico 
    print("como se ve en el grafico va como una montaña rusa subiendo y bajando")
    if f == "b":
        p = contagios.iloc[0]#se selecciona la primera fila de los caontagiados
        lista = list(p)#se cambias en una lista
        suma = 0#se hace una variable la cual vel 0 
        for i in lista:#se va seleccionando cada 1 de las variables que hay en la lsita 1 por 1
             suma = suma + i #la variable se suma con el valor que viene y asi susesivamente 
        plt.stem("Arica y Parinacota",suma)#se muestra el nombre de la region y los total cuntagiados en cada region
        plt.show()#se muestra el grafico 
        print("en a region de Arica y Parinacota han superado las 500 personas en las ultimas 2 semanas")
#lo que se explica aca se repite 17 veces para asi porder mostrar cada una de las regiones que hay 

if x == 2:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[1])
        plt.show()
        print("en este grafico se ve que va variando en un rango de 20 personas aproximadamente")
    if f == "b":
        p = contagios.iloc[1]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Tarapacá",suma)
        plt.show()  
        print("en la regionde Tarapaca han superadon las 400 personas en las ultimas 2 semanas") 


if x == 3:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[2])
        plt.show()
        print(" se puede ver en el grafico que cada dia hay una alteracion de 20 personas al dias")
    if f == "b":
        p = contagios.iloc[2]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Antofagasta",suma)
        plt.show()
        print("en la regionde Antofagasta an superado las 700 personas contagiadas en las ultimas 2 semanas") 
 

if x == 4:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[3])
        plt.show()
        print("se puede vqr que va variando de 20 personas al dia pero el dia 03-07 hubo una subidade mas de 40 personas")
    if f == "b":
        p = contagios.iloc[3]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Atacama",suma)
        plt.show() 
        print("la region de Atacama esta entre las 600 personas contagiadas en las ultimas 2 semanas")


if x == 5:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[4])
        plt.show()
        print("se puede visualizar que hay días que varia entre 40 personas y en otros que varia 20 y 10 personas")
    if f == "b":
        p = contagios.iloc[4]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Coquimbo",suma)
        plt.show() 
        print(" la regionde Coquimbo esta entre los 1200 contagiados en las ultimas 2 semanas")


if x == 6:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[5])
        plt.show()
        print("se puede ver en unos dias sube de la nada y va bajando poco a pooco, varia entre 50 y 150 personas")
    if f == "b":
        p = contagios.iloc[5]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Valparaíso",suma)
        plt.show()
        print("en la region de Valparaíso esta rozando las 3000 personas en las ultimas 2 semanas")

if x == 7:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[6])
        plt.show()
        print(" se puede verque no baja de las 400 personas y que hay una variacion de entre 400 y 100 personas contagiadas por día")
    if f == "b":
        p = contagios.iloc[6]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Metropolitana",suma)
        plt.show()  
        print("la region Metropolitana esta llegando a los 10000 contagiados en las ultimas 2 semanas")


if x == 8:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[7])
        plt.show()
        print("un un inico iba bajando pero luego hubo un rebote y deasde ahi a variado mucho")
    if f == "b":
        p = contagios.iloc[7]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("O’Higgins",suma)
        plt.show()
        print("la regio de O’Higgins a superado las 1000 personas en las ultimas 2 semanas")  

             
if x == 9:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[8])
        plt.show()
        print("se puede ver en el grafico que ha varia mucho hay días en los cuales se mantiene otros que sube mucho y otros que bajan")
    if f == "b":
        p = contagios.iloc[8]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Maule",suma)
        plt.show()  
        print(" en la region del Maule esta rozando las 2000 personas contagiadas en las ultimas 2 semanas")


if x == 10:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[9])
        plt.show()
        print("se puede notar que ha variado demasiao no hay una contacia de datos ")
    if f == "b":
        p = contagios.iloc[9]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Ñuble",suma)
        plt.show() 
        print("en las region de Ñuble estan en las 700 personas contagiadas en las ultimas 2 semanas ")

if x == 11:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[10])
        plt.show()
        print("se puede ver que varia demasiado ya que no hay un orden notable")
    if f == "b":
        p = contagios.iloc[10]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Biobío",suma)
        plt.show() 
        print("las region del Biobío va por los 2500 contagiados en las ultimas 2 semanas")

    
if x == 12:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[11])
        plt.show()
        print("se puede ver que varia demasiado ya que no hay un orden notable")
    if f == "b":
        p = contagios.iloc[11]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Araucanía",suma)
        plt.show() 
        print("en la region del la Araucanía esta en las 200 personas en las ultimas 2 semanas ")


if x == 13:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[12])
        plt.show()
        print("se puede ver que varia demasiado ya que no se nota un orden seguido ")
    if f == "b":
        p = contagios.iloc[12]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Los Ríos",suma)
        plt.show() 
        print(" en la region de Los Ríos vas por las 1200 personas contagiadas en las ultimas 2 semanas")


if x == 14:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[13])
        plt.show()
        print("se puede ver que varia demasiado y que no tiene un movimiento seguido")
    if f == "b":
        p = contagios.iloc[13]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Los Lagos",suma)
        plt.show() 
        print("en la region del Los Lagos han llegado a las 1400 personas")


if x == 15:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[14])
        plt.show()
        print(" se puede ver que no hay un orden pero nunca han pasado de las 30 personas")
    if f == "b":
        p = contagios.iloc[14]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Aysén",suma)
        plt.show() 
        print( "la region de Aysen ha llegado a las 200 personas las ultimas 2 semanas")


if x == 16:
    print("a-grafico no acumuliativo", "b-grafico acumulativo:")
    f = input("ingrese su opcción: ")
    if f == "a":
        plt.stem(contenedor,contagios.iloc[15])
        plt.show()
        print(" se puede ver que hau yna contancia per se altero en 3 dias ")
    if f == "b":
        p = contagios.iloc[15]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Magallanes",suma)
        plt.show() 
        print(" la region de Magallanes roza las 150 personas")

if x == 17 :
    print("a)comuna con mas contagios", "b)comuna con menos contagios")
    f = input("ingrese su opcion:")
    if f == "a":
        p = contagios.iloc[6]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Metropolitana",suma)
        plt.show() 
        print(" se puede ver que la region Metropolitana esta rozando las 10000 personas contagiadas eso quiere decir que a tenido una media de", suma//14,"personas por dia") 
    if f == "b":
        p = contagios.iloc[15]
        lista = list(p)
        suma = 0
        for i in lista:
             suma = suma + i
        plt.stem("Magallanes",suma)
        plt.show() 
        print(" la regionde Magallanes esta entre los 150 y 200 personas en las ultimas 2 semanas eso queire decir que ha tenido una media de", suma//14,"personas por dia ")        

