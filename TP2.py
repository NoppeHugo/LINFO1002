def Surprise(n):
    "pre: Un entier strictement positif n"
    "post: Un tableau A de taille n + 1 vérifiant une propriété à découvrir"
    A = []
    for i in range (n+1):
        temp = i
        for j in range (1,4):
            temp = temp * i
        A.append(temp)
    
    return A

def Mystère(n):
    "pré: Un entier strictement positif n"
    "post: Une valeur mystère c dans le nom fdp!!"
    
    r = 0
    for i in range (1,n+1):
        for j in range (1,i+1):
            for k in range (j,i+j+1):
                r += 1
                
    return r


def Mystère_Simplified(n):
    '''
    pre: `n` > 0
    post: ???
    '''
    
    
def Secret(n):
    "pré: un entier strictement positif n"
    "Une valeur à découvrir"
    
    r = 1
    while n and i > 1:
        for i in range (n):
            tmp = i
            n -= 1
            for j in range (i):
                tmp = tmp+tmp
                i -= 1
            r = max(r,tmp)
    return r
Secret(3)
