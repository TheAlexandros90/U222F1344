# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 19:55:45 2022

@author: alexr
"""

#Ejercicio 1.1

# 1

x = 2

print(x)

# 2

y = float(3)

print(y)

# 3

z =x+y

print(z)
print(type(z))

# es un float


# 4

lista1 = [1, 2, 5, 4, 8, 0]
lista2 = [3.1, 4.2, 5.6, 88, 4, 10]


lista3 = []
for a in lista1:
    posicion = lista1.index(a)
    lista3.append((lista1[posicion],lista2[posicion]))
    posicion += 1
print(lista3)

# 5


for a in lista1:
    posicion = lista1.index(a)
    print("El número ",lista1[posicion]," es ",lista1[posicion]/lista2[posicion]," veces mayor que el número ",lista2[posicion])
    posicion += 1
    
#1.2

#1

texto = "En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. "   

#2
def contador_a(texto):
    contador = 0
    for letra in texto:
        if letra =="a":
            contador +=1
        else:
            contador = contador
    return contador
    
    
print("con mi fórmula salen ",contador_a(texto)," resultados y con .count()", texto.count("a"))

#3

def cambiar_n_por_N(texto):
    textoN=""
    for palabra in texto:
        for letra in palabra:
            if letra == "n":
                letra ="N"
                textoN += letra
            else:
                letra = letra
                textoN += letra
    return textoN

print(cambiar_n_por_N(texto))
        
#4

def quijote(texto):
    quijote = {}
    for palabra in texto:
        palabra = palabra.upper()
        for letra in palabra:
            if letra not in quijote.keys():
                quijote[letra] = 1
            else: 
                quijote[letra] += 1
    return quijote
print(quijote(texto))

#5

#def quijote2(texto):
    #quijote = {}
    #contador = 0
    #for palabra in texto:
       # palabra = palabra.upper()
        #for letra in palabra:
         #   if letra not in quijote:
          #      contador = contador+1
          #      quijote[letra] = {"posiciones":[contador],"repeticiones":[1]}
          #  else: 
          #      contador = contador+1
          #      quijote[letra] = {"posiciones":[].append(contador),"repeticiones":[]+1}
 #   return quijote

#print(quijote2(texto))


#1.3


#1

grupo1 = ["A", "B", "C", "D", "E", "E", "A", "Z", "A", "R", "A", "D", "D"]
grupo2 = ["A", "F", "E", "F", "Z", "L","M", "N", "M", "A", "R"]

#2

#	Número de elementos de cada lista

def contarelementos(grupo):
    contador = 0
    for letra in grupo:
        contador +=1
    return (contador)

print("grupo1 tiene ",contarelementos(grupo1)," elementos y grupo2 tiene ",contarelementos(grupo2)," elementos")

# 	Número de elementos distintos de cada lista

def elementosdistintos(grupo):
    contador = contarelementos(grupo)
    dicionario = {}
    for letra in grupo:
        if letra not in dicionario.keys():
            dicionario[letra] = 1
        else:
            contador -=1
    return dicionario
print("grupo1 tiene ",len(elementosdistintos(grupo1))," elementos distintos y grupo2 tiene ",len(elementosdistintos(grupo2))," elementos distintos")

#  Número de elementos comunes entre los dos 

def elementos_comunes(grupo1,grupo2):
    contador = 0
    lista1=elementosdistintos(grupo1)
    lista2=elementosdistintos(grupo2)
    for letra in lista1:
        if letra in lista2:
            contador += 1
        else:
            contador = contador
    return contador
print("las dos listas tienen ",elementos_comunes(grupo1,grupo2),"en común.")

#  Número de elementos no comunes entre las dos listas          

def elementos_no_comunes(grupo1,grupo2):
    contador = elementos_comunes(grupo1,grupo2)
    lista1=len(elementosdistintos(grupo1))
    lista2=len(elementosdistintos(grupo2))
    
    return (lista1+lista2-2*contador)

print("las dos listas tienen ",elementos_no_comunes(grupo1,grupo2),"no comunes.")

# 	Número de elementos totales entre las dos listas. (Entiendo contado repetidos y no repetidos)

def elementos_totales(grupo1,grupo2):
    a = contarelementos(grupo1)
    b = contarelementos(grupo2)
    return( a+b)
print("El número de elementos totales entre las dos listas es de ", elementos_totales(grupo1,grupo2))

# Número de elementos distintos entre las dos listas

def numero_de_elementos_distintos(grupo1,grupo2): #Entiendo que no se repiten detro de la lista y comprándolas entre ellas
    a = len(elementosdistintos(grupo1))
    b = len(elementosdistintos(grupo2))
    c = elementos_comunes(grupo1,grupo2)
    return(a+b-2*c)
print("El número de elementos distintos entre las dos listas es de",numero_de_elementos_distintos(grupo1,grupo2))

#3 
grupo3 = list(grupo1)
lista = (0,len(grupo3),len(grupo3))
while "A" in grupo3:
    grupo3.remove("A")
    
print(grupo3)
for numero in lista:
    grupo3.insert(numero,"T")

print(grupo3)

#1.4

#1

listax = [1, 2.1, 'a', None, 'A', 4, 5, 3.141516, 2.3 + 0.1111j, '6.2', None]

#2 

def limpiar_lista(listax):
    lista_limpia = []
    for elemento in listax:
        if type(elemento) == int or type(elemento) == float:
            lista_limpia.append(elemento)
        else:
            lista_limpia = lista_limpia 
    return lista_limpia

print(limpiar_lista(listax))

#3

def limpiar_lista_2(listax):
    lista_limpia = []
    for elemento in listax:
        if elemento is None:
            lista_limpia.append(0)
        if type(elemento) == int or type(elemento) == float:
            lista_limpia.append(elemento)
        else:
            lista_limpia = lista_limpia 
    return lista_limpia

print(limpiar_lista_2(listax))

#4

def media_propia(listax):
    a = limpiar_lista(listax)
    b = limpiar_lista_2(listax)
    contadora = 0
    contadorb = 0
    sumaa = 0
    sumab = 0
    for valor in a:
        sumaa = sumaa+valor
        contadora = contadora +1
        
    for valor in b:
        sumab = sumab+ valor
        contadorb = contadorb +1
        
    return(sumaa/contadora,sumab/contadorb)
   
          
print("las medias de limpiar_lista y limpiar_lista_2 son respectivamente ", media_propia(listax))          

#5
# Lo primero es definir una función como quijote pero sin que distinga entre mayus y minus ya que son números:
 
def quijote_a(listax):
    quijote = {}
    for numero in listax:
        if numero not in quijote.keys():
            quijote[numero] = 1
        else:
            quijote[numero] += 1
    return quijote

# Vamos a hayar cuantos valores tiene la lista:
    
def largo_lista(listax):
    contador =0 
    for elemento in listax:
        contador = contador +1
    return(contador)
print(largo_lista(listax))


#Vamos a obtener la media de esta lista:

def media_propia(listax):
    b = limpiar_lista_2(listax)
    contadorb = 0
    sumab = 0
    for valor in b:
        sumab = sumab+ valor
        contadorb = contadorb +1
    return(sumab/contadorb)
        
#Siguiente vamos a obtener los cálculos del coeficiente de asimetría de fisher ( ) 

       
        
def calculos(listax):
    dicionario_final = {}
    a = limpiar_lista_2(listax)
    N = quijote_a(a)
    media = media_propia(listax)
    valores_fisher = []
    resultado_operacion_fisher = 0
#Para el coeficiente de asimetría de fisher ( )
    key_list = list(N.keys())
    val_list = list(N.values())
    for llave, valor in N.items():
        valores_fisher.append([llave ,valor, media] )
    for llave,valor,media in valores_fisher:
        resultado_operacion_fisher = ((llave - media)**3) + resultado_operacion_fisher
    dicionario_final["coeficiente de asimetría "] =  (resultado_operacion_fisher/largo_lista(a)) 
    return(dicionario_final)
print(calculos(listax))

    