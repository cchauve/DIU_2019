# Downloaded from https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/bubble_sort.py
# Modified by adding a counter of the number of steps and uniformizing the output with other sorting algorithms

from __future__ import print_function

def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python recording also 
    the number of steps of the algorithm, where steps are comparisons between
    two elements of the collection to sort.   

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending, the number of steps

    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    ([0, 2, 2, 3, 5],9)

    >>> bubble_sort([])
    ([],0)

    >>> bubble_sort([-2, -5, -45])
    ([-45, -5, -2],3)
    
    >>> bubble_sort([-23,0,6,-4,34])
    ([-23,-4,0,6,34],9)
    """
    nb_steps = 0
    length = len(collection)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            nb_steps += 1
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
        if not swapped: break  # Stop iteration if the collection is sorted.
    return((collection,nb_steps))

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3
    user_input = raw_input('Enter numbers separated by a comma: ').strip()
    unsorted_collection = [int(item) for item in user_input.split(',')]
    (sorted_collection,nb_steps) = bubble_sort(unsorted_collection)
    print('Sorted collection: ', end = '')
    print(*sorted_collection, sep=',')
    print('Number of steps: '+str(nb_steps))
