from utils import util
import random as rn

steps = 0
comparisons = 0


def Quicksort(rng_list):
    global steps
    global comparisons
    steps += 1
    
    rng_list_len = len(rng_list)
    left = []
    right = []
    
    try:
        #*randrange() >>>>>>>>>> randint()
        pivot_position = rn.randrange(0, rng_list_len, 1)
        pivot = rng_list[pivot_position]
    except:
        return rng_list
        

    #print(f"Pivot: {pivot}")
    
    for i in rng_list:
        comparisons += 1
        if i <= pivot:
            left.append(i)
            continue
        
        right.append(i)
    
    #print(f"Left: {left}")
    #print(f"Right: {right}")
    
    
    comparisons += 1
    if  (len(left) < 2) and (len(right) < 2):
        sorted = left + right
        #print(f"Sorted: {sorted}")
        return sorted
    
    comparisons += 1
    if left and right:
        if (ArithmeticMean(left) == left[0]) and (ArithmeticMean(right) == right[0]):
            sorted = left + right
            #print(f"Sorted: {sorted}")
            return sorted
    
    comparisons += 1
    if not left:
        if ArithmeticMean(right) == right[0]:
            sorted = right
            return sorted
    
    comparisons += 1
    if not right:
        if ArithmeticMean(left) == left[0]:
            sorted = left
            return sorted
        
    
    left = Quicksort(left)
    right = Quicksort(right)
    
    sorted = left + right
    
    return sorted
    
    
    
    
def ArithmeticMean(lst):
    try:
        return sum(lst)/len(lst)
    except:
        #* An impossible value since we are working only with natural numbers + {0}
        return -1
        



    

n = input("number of elements in the list: ")

type_int_n, n = util.IsInt(n)

if type_int_n is False:
    #* :)
    print("Nice try dumbass")
    exit(1)

    
sorted_list = Quicksort(util.RNG_List(n, 0, 50))

print(f"Final list: {sorted_list}")
print(f"Steps: {steps}")
print(f"Comparisons: {comparisons}")