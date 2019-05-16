# Downloaded from https://raw.githubusercontent.com/TheAlgorithms/Python/master/sorts/bubble_sort.py
# Modified by adding a counter of the number of steps and uniformizing the output with other sorting algorithms

from __future__ import print_function

def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python recording also 
    the number of steps of the algorithm, where steps are comparisons done during the merge phase

    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    ([0, 2, 2, 3, 5],13)

    >>> merge_sort([])
    ([],0)

    >>> merge_sort([-2, -5, -45])
    ([-45, -5, -2],6)
    """
    nb_steps = 0
    def merge(left, right):
        '''merge left and right
        :param left: left collection
        :param right: right collection
        :return: merge result and number of steps of the merge, i.e. size of the merged collections
        '''
        nb_steps = 0
        result   = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
            nb_steps += 1
        return((result + left + right,nb_steps))
    
    if len(collection) <= 1:
        return((collection,1))
    mid = len(collection) // 2
    (sorted_collection_1,nb_steps_1)   = merge_sort(collection[:mid])
    (sorted_collection_2,nb_steps_2)   = merge_sort(collection[mid:])
    (sorted_collection,nb_steps_merge) = merge(sorted_collection_1, sorted_collection_2)
    return((sorted_collection,nb_steps_1+nb_steps_2+nb_steps_merge))

if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Enter numbers separated by a comma: ').strip()
    unsorted_collection = [int(item) for item in user_input.split(',')]
    (sorted_collection,nb_steps) = merge_sort(unsorted_collection)
    print('Sorted collection: ', end = '')
    print(*sorted_collection, sep=',')
    print('Number of steps: '+str(nb_steps))
