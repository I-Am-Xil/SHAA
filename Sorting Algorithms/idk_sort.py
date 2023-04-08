"""
Does this even have a name?
It's like a bubble sort trying to be selection sort
for the meantime i'll called "idk sort" or "scuffed selection sort"
"""

from utils import util

def idk_sort(rng_list):
    #* i needed something i could edit without trashing the initial data
    sorted_list = rng_list
    
    comparisons = 0
    writings = 0
        
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            
            comparisons += 1

            #print(f"Comparing: {sorted_list[i]}, {sorted_list[j]}")
            
            if sorted_list[i] > sorted_list[j]:
                writings += 1
                var_3 = sorted_list[i]
                sorted_list[i] = sorted_list[j]
                sorted_list[j] = var_3
                
                #print(f"Flip: {sorted_list[i]}, {sorted_list[j]}")
                
    print(sorted_list)
    print(f"Comparisons: {comparisons}")
    print(f"Writings: {writings}")
    return



n = input("number of elements in the list: ")

type_int_n, n = util.IsInt(n)

if type_int_n is False:
    #* :)
    print("Nice try dumbass")
    exit(1)

    
idk_sort(util.RNG_List(n, 0, 50))