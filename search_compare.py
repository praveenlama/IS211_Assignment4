# Praveen Lama
# IS 211
# Assignment 4
# Fall 2017

import matplotlib.pyplot as plt
import time
import random


def sequential_search(listData, item):
    begin = time.time()
    pos = 0
    found = False
    while pos < len(listData) and not found:
        if listData[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    elapsed = end - begin

    if not found:
        pos = -1

    return (pos, elapsed)


def ordered_sequential_search(listData, item):
    listData.sort()
    begin = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(listData) and not found and not stop:
        if listData[pos] == item:
            found = True
        else:
            if listData[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    elapsed = end - begin

    if not found:
        pos = -1

    return (pos, elapsed)


def binary_search_it(listData, item):
    listData.sort()
    begin = time.time()
    first = 0
    last = len(listData) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if listData[midpoint] == item:
            found = True
        else:
            if item < listData[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    elapsed = end - begin

    if not found:
        midpoint = -1

    return (midpoint, elapsed)


def binary_search_rec(listData, item):

    def binary_search_helper(listData, item, begin_time, start, end):
        if start > end:
            return (-1, time.time() - begin)

        midpoint = (start + end) // 2

        if listData[midpoint] == item:
            return (midpoint, time.time() - begin)
        else:
            if item < listData[midpoint]:
                return binary_search_helper(listData, item, begin_time, start,
                                            midpoint - 1)
            else:
                return binary_search_helper(listData, item, begin_time,
                                            midpoint + 1, end)

    listData.sort()
    begin = time.time()
    return binary_search_helper(listData, item, begin, 0, len(listData))


def generate_random_list(size):
    listGenerated = []
    for i in range(size):
        listGenerated.append(random.randint(0, 10000))
    return listGenerated


def main():
    chartList = []
    algorithmList = []
    listCount = 100
    sort_functions = [(sequential_search, "Sequential Search"),
                      (ordered_sequential_search, "Ordered Sequential Search"),
                      (binary_search_it, "Iterative Binary Search"),
                      (binary_search_rec, "Recursive Binary Search")]
    totalLists = [500, 1000, 10000]

    print "Program Starting .... \n"
    print "*** Close the Chart for Next Comparisons *** \n\n"

    for eachList in totalLists:

        sum_of_search_time_list = []

        for i in range(len(sort_functions)):
            sum_of_search_time_list.append(0.0)

        print "\n Generating Chart ... \n"
        print("List of size %d:"%(eachList))

        for i in range(listCount):

            listData = generate_random_list(eachList)

            for j, function_tuple in enumerate(sort_functions):
                function, name = function_tuple
                result, duration = function(listData, -1)
                sum_of_search_time_list[j] += duration

        chartList = []
        algorithmList = []
        for j, function_tuple in enumerate(sort_functions):
            function, name = function_tuple
            timeTaken = sum_of_search_time_list[j]/listCount
            chartList.append(timeTaken)
            algorithmList.append(name)

            print("\t%s took %10.7f seconds to run, on average"%(name,timeTaken))

        plt.plot(chartList)
        plt.yticks(chartList,algorithmList)
        plt.ylabel('Graphic Comparison')
        plt.show()



if __name__ == '__main__':
    main()