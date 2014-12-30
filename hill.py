import numpy as np

m = 3
cifre = range(29)
litere = map(chr, range(97, 123)) + ['.', '?', ' ']

def citire():
    """
Functie care citeste cipher/plaintextul dintr-un fisier cipher.txt,
il transforma in numere si returneaza o matrice
    """
    
    f = open("cipher.txt", "r")
    cipher_litere = f.read() # lista cu cipher/plaintextul in litere
    f.close()
    cipher_numere = [] # lista in care vor fi adaugate numerele

    for element in cipher_litere: # se trece de la lista de litere
        i = litere.index(element)
        cipher_numere.append(cifre[i]) # la cea de numere

    while len(cipher_numere)%m !=0:
        cipher_numere.append(28) # daca nr de elem din lista de numere nu e
    #ivizibil cu m, se adauga la finalul listei 28

    nr_lin = len(cipher_numere)/m

    B = np.array(cipher_numere).reshape(nr_lin, m) # se transforma lista in matrice
    B = B.transpose()
    return B

def tip_1(i,j):
    """
    Functie care construieste o matrice elementara de tip 1, adica o matrice
    permutare P_ij
    """
    M = np.eye(m)
    temp = M[i-1,:].copy()
    M[i-1, :] = M[j-1, :]
    M[j-1, :] = temp[:]
    M = M.astype(np.int)
    return M

def tip_2(i,a):
    """
    Functie care construieste o matrice elementara de tip 2, adica o matrice
    E_i(a)
    """
    M = np.eye(m)
    M[i-1, i-1] = a
    M = M.astype(np.int)
    return M

def tip_3(i,j,l):
    """
    Functie care construieste o matrice elementara de tip 3, adica o matricce
    E_ij(l)
    """
    M = np.eye(m)
    M[j-1,i-1] = l
    M = M.astype(np.int)
    return M


def cheie():
    """
    Functie care construieste cheia de criptare/ decriptare
    """
    n = raw_input('Introduceti numarul de factori din cheia de cifrare: ')
    n = int(n)
    K = np.eye(m) # K este matricea unitate. Matricile introduse de la tastatura se vor
                   # inmulti la dreapta 
    K = K.astype(np.int)
    for i in range(1,n+1):
        print 'Introduceti tipul matricii ', i
        t = int(raw_input(': '))
        if t ==1:
            inp = raw_input("introduceti parametrii i si j, separati prin virgula: ").split(',')
            A = tip_1(int(inp[0]), int(inp[1]))
            K = np.dot(K,A)%29
        elif t == 2:
            inp = raw_input("introduceti parametrii i si alfa, separati prin virgula: ").split(',')
            A = tip_2(int(inp[0]), int(inp[1]))
            K = np.dot(K,A)%29
        elif t == 3:
            inp = raw_input("introduceti parametrii i, j si lambda, separati prin virgula: ").split(',')
            A = tip_3(int(inp[0]), int(inp[1]), int(inp[2]))
            K = np.dot(K,A)%29
        else:
            print "Tip gresit!"
    return(K)


def criptare(B):
    """
    Functie pentru criptare/decriptare
    """
    A = np.dot(K, B)%29
    A = A.transpose()
    output_numere = A.flatten()
    output_litere = []

    for element in output_numere:
            i = cifre.index(element)
            output_litere.append(litere[i])
    return(output_litere)

###############################################################################
#          Urmeaza partea in care se apeleaza functiile                       #
###############################################################################

K = cheie() # construim cheia 
output_litere = criptare(citire()) # citim textul din fisierul extern, apoi il
                                # criptam sau decriptam

file=open("out.txt","w") # rezultatul il scriem intr-un fisier extern
for element in output_litere:
	file.write(str(element))
	file.write(" ")
file.close()

        

    
