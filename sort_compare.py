# Praveen Lama
# IS 211
# Assignment 4
# Fall 2017

import matplotlib.pyplot as plt
import random
import time


def insertion_sort(listData):
    begin = time.time()
    for index in range(1, len(listData)):
        current_value = listData[index]
        position = index

        while position > 0 and listData[position - 1] > current_value:
            listData[position] = listData[position - 1]
            position = position - 1

        listData[position] = current_value

    return time.time() - begin


def gap_insertion_sort(listData, start, gap):
    for i in range(start + gap, len(listData), gap):
        current_value = listData[i]
        position = i
        while position >= gap and listData[position - gap] > current_value:
            listData[position] = listData[position - gap]
            position = position - gap
        listData[position] = current_value


def shell_sort(listData):
    begin = time.time()

    sublist_count = len(listData) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(listData, start_position, sublist_count)

        sublist_count = sublist_count // 2
    return time.time() - begin


def python_sort(listData):
    begin = time.time()
    listData.sort()
    return time.time() - begin


def generate_random_list(size):
    listGenerated = []
    for i in range(size):
        listGenerated.append(random.randint(0,10000))
    return listGenerated


def main():
    listCount = 100
    sort_functions = [(insertion_sort, "Insertion Sort"), (shell_sort, "Shell Sort"),
                      (python_sort, "Python Sort")]
    totalLists = [500, 1000, 10000]

    for eachList in totalLists:

        sum_of_search_time_list = []

        for i in range(len(sort_functions)):
            sum_of_search_time_list.append(0.0)

        print "\n Generating Chart ... \n"
        print("List of size %d:" % (eachList))

        for i in range(listCount):

            listData = generate_random_list(eachList)

            for j, function_tuple in enumerate(sort_functions):
                function, name = function_tuple
                list_copy = listData[:]
                duration = function(list_copy)
                sum_of_search_time_list[j] += duration

        chartList = []
        algorithmList = []
        for j, function_tuple in enumerate(sort_functions):
            function, name = function_tuple
            timeTaken = sum_of_search_time_list[j] / listCount
            chartList.append(timeTaken)
            algorithmList.append(name)

            print "\t%s took %10.7f seconds to run, on average" % (name, timeTaken)

        plt.plot(chartList)
        plt.yticks(chartList, algorithmList)
        plt.ylabel('Graphic Comparison')
        plt.show()

if __name__ == '__main__':
    main()