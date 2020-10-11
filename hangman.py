import csv
import random
import time
import pandas as pd
import numpy as np
import string

print("*** HANGMAN GAME ***\n")
time.sleep(0)
print("Calculatorul va alege un cuvant random dintr-o lista de cuvinte.\n")
time.sleep(0)
print("Tot calculatorul va incerca ca prin maxim 1200 de incercari sa gaseasca cuvantul respectiv\n")
time.sleep(0)


#numar random
numar_random = random.randint(1, 100)
print("Numarul random ales este ",numar_random + 1, "\n")

#citire fisier csv
df = np.genfromtxt('cuvinte_de_verificat.txt', delimiter=';', dtype= None, encoding=None)
print("Calculatorul trebuie sa rezolve jocul cu numarul", numar_random + 1, ", acesta aratand in felul urmator:\n")
time.sleep(0)
rand = list(df)
print(rand[numar_random])
time.sleep(0)
print("Calculatorul incepe rezolvarea\n")
time.sleep(0)

#algoritm de identificare a lungimii cuvintelor
def comparare_lungime_cuvinte():
    if len(rand[numar_random][1]) == len(rand[numar_random][2]):
        print("Cuvintele au aceeasi lungime, se continua procesul de comparare")
        time.sleep(0)
    else:
        print("Cuvantul cenzurat nu are acelasi numar de caractere precum cuvantul necenzurat, verifica cuvintele din tabel si mai incearca odata\n")
        time.sleep(0)

comparare_lungime_cuvinte()

cuvant_cenzurat = rand[numar_random][1]
cuvant_necenzurat = rand[numar_random][2]
alfabet = []
alfabet = string.ascii_uppercase
#alfabet = [A,Ă,Â,B,C,D,E,F,G,H,I,Î,J,K,L,M,N,O,P,Q,R,S,Ș,T,Ț,U,V,W,X,Y,Z]

def comparare_cenzurat_necenzurat():
    for i in range(0, len(cuvant_necenzurat), 1):
        if cuvant_necenzurat[i] == cuvant_cenzurat[i]:
            print(cuvant_necenzurat[i])
        else:
            print(cuvant_cenzurat[i])
'''
for i in range(0, len(alfabet), 1):
    if cuvant_necenzurat[i] != cuvant_cenzurat[i]:
        print(cuvant_cenzurat.replace(cuvant_cenzurat[i], alfabet[1]))
'''
for i in range(0,len(alfabet)):
    if cuvant_cenzurat[i].isalpha() == True:
        print(cuvant_cenzurat[i])
    elif cuvant_cenzurat[i].isalpha() == False:
        print(cuvant_necenzurat[i])







comparare_cenzurat_necenzurat()