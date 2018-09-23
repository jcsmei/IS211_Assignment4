#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assingment4 -  A simple search algorithm."""

import timeit
import random
import pprint


def random_list(length):
    """A funtion to generate a list of random positive integars.

    Ars:
        length (int): An number indicating the maximum number of elements.

    Returns:
        num_list (list): A list randomly generated numbers based on the length
        in the argument

    Exmaples:
        >>> random_list(10)
        [5, 5, 3, 3, 2, 8, 1, 9, 8, 2]
        >>> random_list(15)
        [3, 9, 12, 14, 11, 9, 14, 13, 7, 4, 9, 5, 4, 3, 11]
        >>> random_list(20)
        [11, 9, 10, 8, 5, 18, 9, 16, 16, 7, 19, 9, 14, 20, 16, 14, 9, 13, 19, 7]
    """
    num_list = []
    for i in xrange(length):
        num_list.append(random.randint(1,length))
    return num_list


def sequential_search(a_list, item):
    """A sequential search function that searches a value within a list; this
        function sequentailly checks each element  of the list for the value.

        Args:
            listA (list): A list of randomly generated postive integars to be
                                searched.
            item (various): The value to be searched in the list of elements.

        Returns:
            A string indicating the processing time in seconds and the
            boolean value of the value being searched.

        Examples:
            >>> a = random_list(15)
            >>> print a
            [12, 11, 15, 7, 9, 5, 6, 5, 5, 13, 4, 9, 4, 5, 4]
            >>> sequential_search(a, 13)
            (4.665321498967798e-06, True)
            >>> a = random_list(100)
            >>> print a
            [39, 35, 58, 44, 47, 22, 94, 22, 64, 45, 97, 40, 12, 28,
            75, 38, 22, 8, 40, 39, 12, 14, 60, 95, 38, 65, 96, 24,
            60, 34, 36, 88, 41, 59, 38, 90, 73, 50, 3, 80, 27, 32,
            47, 35, 52, 77, 39, 85, 15, 61, 53, 84, 69, 68, 58, 8,
            14, 79, 89, 62, 55, 99, 43, 1, 33, 75, 88, 69, 93, 96,
            69, 93, 34, 25, 82, 62, 28, 75, 41, 51, 60, 63, 87, 76,
            90, 69, 53, 71, 19, 74, 32, 91, 55, 83, 93, 12, 90, 9, 70, 92]
            >>> sequential_search(a, 93)
            (2.845846114496453e-05, True)
        """
    start_time = timeit.default_timer()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1

    end_time = timeit.default_timer()
    run_time = end_time - start_time
    return (run_time, found)


def ordered_sequential_search(a_list, item):
    """A function for an ordered sequential on list, returns
    a string indicating the search time and the boolean of of the value.

        Args:
            listA (list): A list of randomly generated postive integars to be
                                searched.
            item (various): The value to be searched in the list of elements.

        Returns:
            A string indicating the processing time in seconds and the
            boolean value of the value being searched,

        Examples:
            >>> a = random_list(100)
            >>> print a
            [10, 69, 42, 50, 27, 30, 81, 93, 15, 55, 9, 97, 14, 60, 37, 46,
            45, 80, 42, 83, 33, 40, 63, 22, 72, 53, 86, 31, 74, 90, 52, 69,
            9, 38, 86, 59, 24, 81, 76, 60, 6, 49, 55, 45, 86, 23, 96, 4, 14,
            88, 76, 96, 83, 16, 93, 90, 14, 31, 34, 76, 43, 95, 66, 89, 59,
            52, 91, 4, 25, 32, 86, 96, 88, 8, 11, 89, 46, 59, 58, 17, 99,
            93, 76, 55, 42, 50, 99, 81, 8, 65, 95, 79, 36, 49, 4, 31, 90, 96, 10, 45]
            >>> ordered_sequential_search(a, 90)
            (2.0527414595458308e-05, True)
            >>> ordered_sequential_search(a, -1)
            (4.665321498009689e-06, False)
        """
    a_list = sorted(a_list)
    start_time = timeit.default_timer()
    pos = 0
    found = False
    stop = False

    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end_time = timeit.default_timer()
    return (end_time-start_time, found)


def binary_search_iterative(a_list, item):
    """An iterative binary search on a sorted list.

        Args:
            listA (list): A list of randomly generated postive integars to be
                                searched.
            item (various): The value to be searched in the list of elements.

        Returns:
            tuple: A tuple indicating the processing time in seconds and the
            boolean value of the value being searched.

        Examples:
            >>> a = random_list(50)
            >>> print a
            [17, 1, 8, 1, 10, 39, 9, 30, 28, 6, 3, 40, 15, 1, 17, 28, 10,
            14, 31, 24, 41, 29, 10, 37, 45, 40, 29, 17, 31, 17, 37, 16,
            41, 19, 33, 6, 42, 9, 30, 22, 31, 46, 17, 31, 6, 46, 48, 45, 16, 47]
            >>> binary_search_iterative(a, 30)
            (6.997982248451696e-06, True)
            >>> binary_search_iterative(a, -1)
            (5.598385797611627e-06, False)
        """
    a_list = sorted(a_list)

    start_time = timeit.default_timer()
    first = 0
    last = len(a_list) -1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end_time = timeit.default_timer()
    return (end_time-start_time, found)


def binary_search_recursive(a_list, item):
    """A recursive binary search function to find value in a random list.

        Args:
            listA (list): A list of randomly generated postive integars to be
                                searched.
            item (various): The value to be searched in the list of elements.

        Returns:
            tuple: A tuple indicating the processing time in seconds and the
            boolean value of the value being searched.

        Examples:
            >>> a = random_list(50)
            >>> print a
            [23, 22, 32, 39, 35, 16, 11, 39, 30, 2, 11, 18,
            41, 1, 2, 13, 16, 16, 48, 35, 42, 47, 41, 25, 30,
            12, 22, 19, 26, 38, 22, 4, 7, 14, 15, 24, 35, 49,
            40, 27, 28, 18, 17, 12, 18, 29, 32, 5, 47, 15]
            >>> binary_search_recursive(a, 27)
            (4.665321498967819e-07, True)
            >>> binary_search_recursive(a, -1)
            (4.665321498009689e-07, False)
    """
    a_list = sorted(a_list)
    start_time = timeit.default_timer()

    if len(a_list) == 0:
        found = False
    else:
        midpoint = len(a_list) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                return binary_search_recursive(a_list[:midpoint], item)
            else:
                return binary_search_recursive(a_list[midpoint + 1:], item)

    end_time = timeit.default_timer()
    return (end_time-start_time, found)


def main():
    """The main function to run all the search algorithms.

        Args:
            none

        Returns:
            String (string): a String to indicate the time it took to pricess each search.

        Exmaples:
            For a random list size of 500:
            Binary Recursive Search took  0.0000004 secconds to run, on average.
            Binary Iterative Search took  0.0000031 secconds to run, on average.
            Sequential Search took  0.0000947 secconds to run, on average.
            Ordered Sequential Search took  0.0000011 secconds to run, on average.
            For a random list size of 1000:
            Binary Recursive Search took  0.0000007 secconds to run, on average.
            Binary Iterative Search took  0.0000075 secconds to run, on average.
            Sequential Search took  0.0002780 secconds to run, on average.
            Ordered Sequential Search took  0.0000025 secconds to run, on average.
            For a random list size of 10000:
            Binary Recursive Search took  0.0000012 secconds to run, on average.
            Binary Iterative Search took  0.0000537 secconds to run, on average.
            Sequential Search took  0.0019784 secconds to run, on average.
            Ordered Sequential Search took  0.0000050 secconds to run, on average.
        """
    list_size = [500, 1000, 10000]
    search_algo = {'Sequential': 0,
                   'Ordered Sequential': 0,
                   'Binary Iterative': 0,
                   'Binary Recursive': 0}
    
    for lsize in list_size:
        counter =  0
        while counter < 100:
            list_search = random_list(lsize)
            search_algo['Sequential'] += sequential_search(list_search, -1)[0]
            search_algo['Ordered Sequential'] += ordered_sequential_search(list_search, -1)[0]
            search_algo['Binary Iterative'] += binary_search_iterative(list_search, -1)[0]
            search_algo['Binary Recursive'] += binary_search_recursive(list_search, -1)[0]
            counter += 1

        print 'For a random list size of %s:' % (lsize)

        for algo in search_algo:
            print ('%s Search took %10.7f secconds to run, '
                           'on average.') % (algo, search_algo[algo] / counter)


if __name__  == "__main__":
    main()
