# Algorithmes de tri extraits du manuel de cours UE J1MI2013 : Algorithmes et
# Programmes par Alain Griffault, version du 19 mai 2015.
# Programmes modifiés pour retourner le nombre d'étape élémentaires de calcul

# Fonctions auxiliaires
def estIndice(T,i):
    return(0<=i and i<len(T))

def echange (T,i,j):
    assert(estIndice(T,i) and estIndice(T,j))
    aux  = T[i]
    T[i] = T[j]
    T[j] = aux

def decalageDroite(T,g,d):
    assert(g<=d and estIndice(T,g) and estIndice(T,d))
    nb_etapes = 0
    aux = T[d]
    for k in range(d,g,-1):
        T[k] = T[k-1]
        nb_etapes += 1
    T[g] = aux
    return(nb_etapes)

def decalageGauche(T,g,d):
    assert(g<=d and estIndice(T,g) and estIndice(T,d))
    aux = T[g]
    nb_etapes = 0
    for k in range(g,d):
        T[k] = T[k+1]
        nb_etapes += 1
    T[d] = aux
    return(nb_etapes)

# Fonctions de tris simples (sélection, bulle, insertion)

# Tri selection. Etapes élémentaires = comparaisons entre paires d'éléments
def triSelection(T):
    nb_etapes = 0
    for i in range(len(T)-1):
        iMin=i
        for j in range(i+1,len(T)):
            nb_etapes += 1
            if T[j]<T[iMin]:
                iMin = j
        if iMin != i :
            echange(T,i,iMin)
    return(nb_etapes)

# Tri bulle. Etapes élémentaires = comparaisons entre paires d'éléments et décalages
def triBulle(T):
    nb_etapes = 0
    for i in range(len(T)-1,0,-1):
        for j in range(i):
            nb_etapes += 1
            if T[j]>T[j+1]:
                nb_etapes += decalageDroite(T,j,j+1)
    return(nb_etapes)

# Tri insertion. Etapes élémentaires = comparaisons entre paires d'éléments et décalages
def triInsertion(T):
    nb_etapes = 0
    for i in range(1,len(T)):
        j = i-1;
        while j>=0 and T[i]<T[j]:
            nb_etapes += 1
            j = j-1
        nb_etapes += 1
        nb_etapes += decalageDroite(T,j+1,i)
    return(nb_etapes)

# Tri par fusion. Etapes élémentaires = comparaisons entre paires d'éléments et recopie d'éléments
def fusionner(T,g,m,d):
    R = [0]*(d-g+1)
    i = g
    j = m+1
    k = 0
    nb_etapes = 0
    while i<=m and j<=d:
        nb_etapes += 1
        if T [i]<=T[j]:
            R[k] = T[i]
            i = i+1
        else:
            R[k] = T[j]
            j = j+1
        k = k+1
    while i<=m:
        nb_etapes += 1
        R[k] = T[i]
        i = i+1
        k = k+1
    while j<=d:
        nb_etapes += 1
        R[k] = T[j]
        j = j+1
        k = k+1
    for k in range(len(R)):
        nb_etapes += 1
        T[g+k] = R[k]
    return(nb_etapes)
        
def triFusionRec(T,g,d):
    nb_etapes = 0
    if g<d:
        m = (g+d)//2
        nb_etapes += triFusionRec(T,g,m)
        nb_etapes += triFusionRec(T,m+1,d)
        nb_etapes += fusionner(T,g,m,d)
    return(nb_etapes)

def triFusion(T):
    return(triFusionRec(T,0,len(T)-1))
