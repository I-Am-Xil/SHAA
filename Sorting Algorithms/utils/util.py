import random as rn

def RNG_list(n, initial ,final):
    rng_list = []
    
    for i in range (n):
        rng_list.append(rn.randint(initial, final))
        
    print(rng_list)
    return rng_list


def isint(n):
    n_1 = 0
    
    try:
        n_1 = int(n)
        type_int = True
    except ValueError:
        type_int = False

    return type_int, n_1