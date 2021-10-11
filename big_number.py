# FR: Résumer la grandeur d’un nombre
# EN: Minimize a long number's length

import itertools 



def factorial(n):
    if n == 0 or n == 1: return 1
    else: return n * factorial(n-1)
	
# FR: Cette fonction pour créer les labels à ajouter çà la fin des nombres
# EN: This function creates labels to be added at the end of numbers

def bilettres_minuscules():
    alphabet = [chr(97 + i) for i in range(26)]
    bilettres_minuscules = itertools.product(alphabet,alphabet)
    bilettres_minuscules = list(bilettres_minuscules)
    for i in range(len(bilettres_minuscules)):
        bilettres_minuscules[i] = ''.join(bilettres_minuscules[i])
    return bilettres_minuscules



def show_number(f):
    b=[]
    i = len(f) - 1
    while i >= 0:
        a = []
        c = 0
        while c < 3 and i-c >= 0:
            a.append(f[i-c])
            c+=1 
        a.reverse()
        a = ''.join(a)
        i -= 3
        b.append(a)
    b.reverse()
    ch = ''
    for i in range(len(b)):
        ch = ch + str(b[i]) + ' '
    return ch

# FR: Cette retourne l'indice de l'exetnsion ajoutée (lettres à ajouter)
# EN: This function returns added extension's index (letters to be added)

def find_index(f):
    index = 0
    while f >= 1000:
        f = f // 1000
        index += 1
    return index, f


def big_number(n):
    lettres_ajoutees = ['', 'K', 'M', 'G', 'T']
    bilettres_min = bilettres_minuscules()
    for i in range (len(bilettres_min)):
        lettres_ajoutees.append(bilettres_min[i])
    
    #print(lettres_ajoutees)
    for i in range(n):  
        f = factorial(i)
        index, fact = find_index(f) 
        aff = str(fact) + lettres_ajoutees[index] + ' : ' + show_number(str(f))
        print(aff)



big_number(30)

