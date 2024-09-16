#!/usr/bin/env python

def puntos_medios(n_rectangulos):
    ancho=1/n_rectangulos
    Puntos=[]
    punto_med=ancho/2
    Puntos.append(punto_med)

    while punto_med<1:
        punto_med+=ancho
        Puntos.append(punto_med)

    return Puntos

def suma_reiman(n_rectangulos,puntos):
    ancho=1/n_rectangulos
    area_rectangulos=[]

    for i in puntos:
        area=ancho/(1+(i**2))
        area_rectangulos.append(area)

    return 4*sum(area_rectangulos)

n_rect=int(input("Ingrese cantidad de rectangulos: \n"))

pi=suma_reiman(n_rect,puntos_medios(n_rect))

print(pi)
