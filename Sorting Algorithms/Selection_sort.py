from utils import util

steps_counter = 0


def Selection_sort(rng_list):
    sorted_list = rng_list
    list_length = len(rng_list)
    temp_var = 0
    
    for j in range(list_length):
            
        min_val_position = min_value(rng_list, list_length, initial=j)
            
        #print(f"Sorting: {sorted_list[j]}, {sorted_list[min_val_position]}")
        
        temp_var = sorted_list[j]
        sorted_list[j] = sorted_list[min_val_position]
        sorted_list[min_val_position] = temp_var
    
    print(f"Sorted list: {sorted_list}")
    
    return sorted_list



#TODO: Add step counter
def min_value(rng_list, list_length, initial):
    
    min_val = rng_list[initial]
    min_val_position = initial
    
    for i in range(initial, list_length):
        if rng_list[i] < min_val:
            min_val = rng_list[i]
            min_val_position = i
        
        global steps_counter
        steps_counter += 1
            
    #print(f"Min: {min_val} Position: {min_val_position}")
    return min_val_position


n = input("number of elements in the list: ")

type_int_n, n = util.isint(n)

if type_int_n is False:
    #* :)
    print("Nice try dumbass")
    exit(1)
    
Selection_sort(util.RNG_list(n, 0, 50))
print(f"Steps: {steps_counter}")