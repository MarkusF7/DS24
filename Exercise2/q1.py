import numpy as np
import time
import random

def sorted_indices_with_numpy(lst):
    if not lst:
        raise ValueError("Input list is empty")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input list contains non-numerical values")
    
    indices = np.argsort(lst)
    return indices

def sorted_indices_without_numpy(lst):
    if not lst:
        raise ValueError("Input list is empty")
    if not all(isinstance(x, (int, float)) for x in lst):
        raise ValueError("Input list contains non-numerical values")
    
    indices = list(range(len(lst)))
    indices.sort(key=lambda x: lst[x])
    return indices
 
def analyse_list(lst, name):
    try:
        start_time = time.time()
        sorted_indices_without_numpy(lst)
        print("List: "+name+" Time taken without NumPy:", time.time() - start_time)


        start_time = time.time()
        sorted_indices_with_numpy(lst)
        print("List: "+name+" Time taken with NumPy:", time.time() - start_time)
    except ValueError: 
        print(name+" Input list is empty or contains non-numerical values")

list1 = [23, 104, 5, 190, 8, 7, -3]
list2 = []
list3 = [random.randint(0, 9876) for _ in range(1000000)]
analyse_list(list1, "7Elements")
analyse_list(list2, "Empty")


for i in range(10):
    analyse_list(list3, "1000000Elements")

    