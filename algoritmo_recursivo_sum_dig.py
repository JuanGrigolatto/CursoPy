# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:21:51 2022

@author: alumno
"""

def suma_digitos(n):
    if(n==0):
        return 0
    return suma_digitos(n//10)+n%10

def main():
    suma_digitos=suma_digitos(150)
    print(suma_digitos)


if __name__ =="__main__":
    main()