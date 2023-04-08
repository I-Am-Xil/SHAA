from utils import util

def Insertion_sort(rng_list):
    
    comparison_counter = 0
    writings = 0
    
    temp_var = 0
    sorted_list = rng_list
    
    for i in range(len(sorted_list)-1):
        
        #print(f"Comparing: {sorted_list[i]}, {sorted_list[i+1]}")
        
        if sorted_list[i] > sorted_list[i+1]:
            
            for j in range(i+1, 0, -1):        
                
                comparison_counter += 1
                
                if sorted_list[j] < sorted_list[j-1]:
                    writings += 1
                    
                    temp_var = sorted_list[j]
                    sorted_list[j] = sorted_list[j-1]
                    sorted_list[j-1] = temp_var
                    #print(f"Swapping: {sorted_list[j]}, {sorted_list[j-1]}")
    
    print(sorted_list)
    print(f"Comparisons: {comparison_counter}")
    print(f"writings: {writings}")




n = input("number of elements in the list: ")

type_int_n, n = util.IsInt(n)

if type_int_n is False:
    #* :)
    print("Nice try dumbass")
    exit(1)

    
Insertion_sort(util.RNG_List(n, 0, 50))