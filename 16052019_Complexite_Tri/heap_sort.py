# Downloaded from https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/bubble_sort.py
# Modified by adding a counter of the number of steps and uniformizing the output with other sorting algorithms

from __future__ import print_function

def heapify(unsorted, index, heap_size):
    nb_steps    = 0
    largest     = index
    left_index  = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    nb_steps += 1

    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    nb_steps += 1
        
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        nb_steps += heapify(unsorted, largest, heap_size)

    return(nb_steps)
        
def heap_sort(collection):
    '''
    Pure implementation of the heap sort algorithm in Python  recording also 
    the number of steps of the algorithm, where steps are comparisons

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    ([0, 2, 2, 3, 5],20)

    >>> heap_sort([])
    ([],0)

    >>> heap_sort([-2, -5, -45])
    ([-45, -5, -2],8)
    '''
    nb_steps = 0
    n = len(collection)
    for i in range(n // 2 - 1, -1, -1):
        nb_steps += heapify(collection, i, n)
    for i in range(n - 1, 0, -1):
        collection[0], collection[i] = collection[i], collection[0]
        nb_steps += heapify(collection, 0, i)
    return((collection,nb_steps))

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma: ').strip()
    unsorted_collection = [int(item) for item in user_input.split(',')]
    (sorted_collection,nb_steps) = heap_sort(unsorted_collection)
    print('Sorted collection: ', end = '')
    print(*sorted_collection, sep=',')
    print('Number of steps: '+str(nb_steps))
