import csv
import random
import time


print("*** HANGMAN GAME ***")
time.sleep(1)
print("Calculatorul va alege un cuvant random dintr-o lista de cuvinte.")
time.sleep(1)
print("Tot calculatorul va incerca ca prin maxim 1200 de incercari sa gaseasca cuvantul respectiv")
time.sleep(1)

#citirea fisierului cu cuvintele de verificare
with open('cuvinte_de_verificat.csv') as f:
    citire_csv = csv.reader(f, delimiter = ';', quotechar =',', quoting = csv.QUOTE_MINIMAL)
    numar_random = random.randint(1, 100)
    print("Numarul random ales este") 
    print(numar_random + 1)
    row = list(citire_csv)
    print(row[numar_random])
   


  