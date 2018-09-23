#!/usr/bin/env python
#! -*- coding: utf-8 -*-
"""IS211_Assingment4. A simple sort compare assignment."""

import random
import timeit


def random_list(length):
    """A function to generate a random list of positive integars.

        Args:
            length (int): An integar for the maximum length of the list.

        Returns:
            A list of random numbers.

        Example:
            >>> random_list(14)
            [11, 1, 13, 5, 14, 5, 6, 11, 3, 10, 7, 9, 7, 12]
            >>> random_list(10)
            [7, 8, 9, 2, 6, 6, 1, 7, 8, 3]
    """
    num_list = []
    for n in xrange(length):
        num_list.append(random.randint(1, length))
    return num_list


def insertion_sort(sort_list):
    """A function for insertion sort.

        Args:
            sort_list (list): A list of random positive integars.

        Returns:
            The time it takes to run the insertion sort algorithm and returns the sorted list.

        Exmaples:
            >>> a = random_list(10)
            >>> print a
            [3, 5, 6, 5, 6, 9, 2, 9, 3, 6]
            >>> insertion_sort(a)
            (9.330643003124806e-06, [2, 3, 3, 5, 5, 6, 6, 6, 9, 9])
            >>> a = random_list(15)
            >>> print a
            [2, 5, 8, 7, 7, 1, 7, 14, 9, 1, 15, 7, 2, 5, 6]
            >>> insertion_sort(a)
            (2.8458461130753676e-05, [1, 1, 2, 2, 5, 5, 6, 7, 7, 7, 7, 8, 9, 14, 15])
    """
    start_time = timeit.default_timer()
    for index in range(1, len(sort_list)):
        current_value = sort_list[index]
        position = index
        while position > 0 and sort_list[position - 1] > current_value:
            sort_list[position] = sort_list[position - 1]
            position = position - 1
        sort_list[position] = current_value
    end_time = timeit.default_timer()
    return (end_time-start_time, sort_list)


def gap_insertion_sort(sort_list, start, gap):
    """A funtion for a gap insertion sort.

        Args:
            sort_list (list): A list of integars to be sorted by the funtion.
            start (integar): THe starting psotion for the sub list.
            gap (integar): The end posiiton for the sub list.

        Returns:
            none

        """
    for i in range(start + gap, len(sort_list), gap):
        current_value = sort_list[i]
        position = 1
        while position >= gap and sort_list[position - gap] > current_value:
            sort_list[position] = sort_list[position - gap]
            position = position - gap
        sort_list[position] = current_value


def shell_sort(sort_list):
    """A function demostrate shell sort or 'diminishing increment sort'.

        Args:
            sort_list (list): A list of integars to be sorted by the funtion.

        Returns:
            A list sorted by the function and the times to process.

        Examples:
            >>> a = random_list(8)
            >>> print a
            [6, 1, 6, 7, 6, 4, 6, 7]
            >>> shell_sort(a)
            (1.8661285992038756e-05, [4, 7, 6, 7, 6, 4, 6, 7])
            >>> b = random_list(12)
            >>> print b
            [4, 1, 5, 6, 4, 2, 8, 7, 9, 3, 11, 11]
            >>> shell_sort(b)
            (8.304272267878332e-05, [2, 11, 5, 6, 4, 2, 8, 7, 9, 3, 11, 11])
    """
    start_time = timeit.default_timer()
    sublist_count = len(sort_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(sort_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end_time = timeit.default_timer()
    return (end_time - start_time, sort_list)


def python_sort(sort_list):
        """A function to sort a list of integars with python's built in algorith.

        Args:
            sort_list (list): A list of random positive integars.

        Returns:
            A list of sorted integars and the time to process.

        Examples:
            >>> a = random_list(8)
            >>> print a
            [6, 6, 3, 3, 8, 4, 1, 1]
            >>> python_sort(a)
            (6.064917948658137e-06, [1, 1, 3, 3, 4, 6, 6, 8])
            >>> b - random_list(12)
            >>> print b
            [8, 4, 10, 5, 11, 7, 10, 1, 5, 11, 7, 7]
            >>> python_sort(b)
            (4.665321498009689e-06, [1, 4, 5, 5, 7, 7, 7, 8, 10, 10, 11, 11])
        """
        start_time =  timeit.default_timer()
        sort_list.sort()
        end_time = timeit.default_timer()
        return (end_time - start_time, sort_list)


def main():
    """The main funtion to run all the sort algorithms.

        Args:
            none

        Returns:
            A string for each algorithm and the time to process each sort.

        Examples:
            For a random list of 500:
            Python Sort took  0.0000225 seconds to run, on average.
            Shell Sort took  0.0009668 seconds to run, on average.
            Insertion Sort took  0.0117168 seconds to run, on average.
            For a random list of 1000:
            Python Sort took  0.0000549 seconds to run, on average.
            Shell Sort took  0.0030351 seconds to run, on average.
            Insertion Sort took  0.0601090 seconds to run, on average.
            For a random list of 10000:
            Python Sort took  0.0003076 seconds to run, on average.
            Shell Sort took  0.0340817 seconds to run, on average.
            Insertion Sort took  5.9072282 seconds to run, on average.
        """
    list_size = [500, 1000, 10000]
    sort_algo = {'Insertion': 0,
                 'Shell': 0,
                 'Python': 0}

    for lsize in list_size:
        counter = 0
        while counter < 100:
            list_sort = random_list(lsize)
            sort_algo['Insertion'] += insertion_sort(list_sort)[0]
            sort_algo['Shell'] += shell_sort(list_sort)[0]
            sort_algo['Python'] += python_sort(list_sort)[0]
            counter += 1

        print 'For a random list of %s:' % (lsize)

        for algo in sort_algo:
            print ('%s Sort took %10.7f seconds to run, '
                   'on average.') % (algo, sort_algo[algo] / counter)


if __name__ == '__main__':
    main()
