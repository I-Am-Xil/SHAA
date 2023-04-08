from utils import util


def Bubble_sort(rng_list):

    list_length = len(rng_list)
    temp_list = rng_list
    temp_var = 0
    
    comparisons = 0
    writings = 0
    for i in rng_list:
        for j in range(list_length-1):
            
            comparisons += 1
            #print(f"Comparing: {temp_list[j]}, {temp_list[j+1]}")
            
            if temp_list[j] > temp_list[j+1]:
                
                writings += 1
                
                temp_var = temp_list[j]
                temp_list[j] = temp_list[j+1]
                temp_list[j+1] = temp_var
                
                
                
                #print(f"Flipping: {temp_list[j]}, {temp_list[j+1]}")
                #print(temp_list)
    
    print(f"Final list: {temp_list}")
    print(f"Comparisons: {comparisons}")
    print(f"Writings: {writings}")
    
    return



n = input("number of elements in the list: ")

type_int_n, n = util.IsInt(n)

if type_int_n is False:
    #* :)
    print("Nice try dumbass")
    exit(1)

    
Bubble_sort(util.RNG_List(n, 0, 50))