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

def comparare_cenzurat_necenzurat():
    for i in range(0, len(rand[numar_random][2]), 1):
        if cuvant_necenzurat[i] != cuvant_cenzurat[i]:
            print("cuvintele nu seamana")

comparare_cenzurat_necenzurat()