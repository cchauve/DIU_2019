# Downloaded from https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/bubble_sort.py
# Modified by adding a counter of the number of steps and uniformizing the output with other sorting algorithms

from __future__ import print_function

def insertion_sort(collection):
    """Pure implementation of the insertion sort algorithm in Python recording also 
    the number of steps of the algorithm, where steps are elements shifts

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    ([0, 2, 2, 3, 5],5)

    >>> insertion_sort([])
    ([],0)

    >>> insertion_sort([-2, -5, -45])
    ([-45, -5, -2],3)
    """
    nb_steps = 0
    for index in range(1, len(collection)):
        while index > 0 and collection[index - 1] > collection[index]:
            nb_steps += 1
            collection[index], collection[index - 1] = collection[index - 1], collection[index]
            index -= 1

    return((collection,nb_steps))


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma: ').strip()
    unsorted_collection = [int(item) for item in user_input.split(',')]
    (sorted_collection,nb_steps) = insertion_sort(unsorted_collection)
    print('Sorted collection: ', end = '')
    print(*sorted_collection, sep=',')
    print('Number of steps: '+str(nb_steps)) 
