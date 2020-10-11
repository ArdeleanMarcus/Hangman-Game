import random
import time
import numpy as np

print("*** HANGMAN GAME ***\n")
time.sleep(1)

print("Calculatorul va alege un cuvant random dintr-o lista de cuvinte.\n")
time.sleep(2)
print("Tot calculatorul va incerca ca prin maxim 1200 de incercari sa gaseasca cuvantul respectiv\n")
time.sleep(3)


#generare numar random
numar_random = random.randint(1, 100)
print("Numarul random ales este ",numar_random + 1, "\n")
time.sleep(2)

#citire din  fisier csv
df = np.genfromtxt('cuvinte_de_verificat.txt', delimiter=';', dtype= None, encoding=None)
print("Calculatorul trebuie sa rezolve jocul cu numarul", numar_random + 1, ", acesta aratand in felul urmator:\n")
time.sleep(4)
#afisarea intregului rand din fisierul csv care trebuie rezolvat
rand = list(df)
print(rand[numar_random], "\n")
time.sleep(3)
print("Calculatorul incepe rezolvarea\n")
time.sleep(2)

#algoritm de iverificare a lungimii cuvintelor [  suplimentar, dar necesar :)))  ]
def comparare_lungime_cuvinte():
    if len(rand[numar_random][1]) == len(rand[numar_random][2]):
        print("Cuvintele au aceeasi lungime, se continua procesul de comparare\n")
        time.sleep(2)
    else:
        print("Cuvantul cenzurat nu are acelasi numar de caractere precum cuvantul necenzurat, verifica cuvintele din tabel si mai incearca odata\n")
        time.sleep(2)

comparare_lungime_cuvinte()

#separarea fisierului csv pe coloane
cuvant_cenzurat = rand[numar_random][1]
cuvant_necenzurat = rand[numar_random][2]
alfabet = ["A","Ă","Â","B","C","D","E","F","G","H","I","Î","J","K","L","M","N","O","P","Q","R","S","Ș","T","Ț","U","V","W","X","Y","Z"]
#lista cu cifre se mai putea face si cu UTF 8, dar am avut probleme cu afisarea lor

def litera_de_inlocuit():
    incercari=0
    for i in range(0, len(cuvant_necenzurat)):
        for j in range(0, len(alfabet)):
            if cuvant_necenzurat[i] == alfabet[j] != cuvant_cenzurat[i].isalpha() :
                print(cuvant_necenzurat[i], end="")
                time.sleep(0.25)
                j=j+1
 #calcularea numarului de incercari pe care calculatorul le face pentru a afla cuvantul
            while i != j:
                incercari += 1
                break
    print("\n")
    print("Calculatorul a rezolvat problema in ", incercari, "incercari")


# am verificat fiecare caracter din cuvant, iar daca aceasta este litera, este afisata din prima, daca nu, aceasta trece prin loop-ul litera_de_inlocuit
# unde fiecare caracter steluta este comparat cu fiecare caracter litera din cuvantul necenzurat si cu alfabetul.
for i in range(0,len(cuvant_necenzurat)):
    if cuvant_cenzurat[i].isalpha() == False:
        litera_de_inlocuit()
        break


