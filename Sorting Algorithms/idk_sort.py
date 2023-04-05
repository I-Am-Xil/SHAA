"""
Does this even have a name?
It's like a bubble sort trying to be selection sort
for the meantime i'll called "idk sort" or "scuffed selection sort"
"""

import random as rn

def Random_number_list_generator(n):
    rng_list = []
    for i in range (n):
        #* You can change this to other numbers
        rng_list.append(rn.randint(0, 50))
    print(rng_list)
    return rng_list


def idk_sort(rng_list):
    #* i needed something i could edit without trashing the initial data
    sorted_list = rng_list
    var_1 = 0
    var_2 = 0
    
    steps = 0
        
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            
            steps += 1
            
            var_1 = sorted_list[i]
            var_2 = sorted_list[j]

            print(f"Comparing: {var_1}, {var_2}")
            
            if var_1 > var_2:
                var_3 = var_1
                var_1 = var_2
                var_2 = var_3
                
                sorted_list[i] = var_1
                sorted_list[j] = var_2
                print(f"Flip: {var_1}, {var_2}")
                
    print(sorted_list)
    print(f"steps: {steps}")    
    return



n = input("number of elements in the list: ")

#* i hate this try catch btw
try:
    n = int(n)
    typeof_n = True
except ValueError:
    typeof_n = False

if typeof_n is False:
    #* :)
    print("Nice try dumbass")
    exit(1)

    
idk_sort(Random_number_list_generator(n))