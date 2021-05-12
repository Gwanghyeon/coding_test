# Sorting

array = [5, 3, 7, 9, 10, 3, 7, 8]


# selection
def selection(array):
    for i in range(len(array)):

        for j in range(i+1, len(array)):
            if array[j] <= array[i]:
                array[j], array[i] = array[i], array[j]
                #min_idx = j

    return array

# from the book, selection sorting


def selection_modified(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] <= array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

# insertion


def insertion(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] <= array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array


#print("Selection: " + str(selection(array)))
print(array)
#print("Insertion: ", str(insertion(array)))

# quick_soring


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start+1
    right = end

    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] > array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


def quick_soring_modified(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [y for y in tail if y > pivot]

    return quick_soring_modified(left)+[pivot]+quick_soring_modified(right)


# print(quick_soring_modified(array))


# count sort

def count_sort(array):
    count = [0]*(max(array)+1)

    for i in range(len(array)):
        count[array[i]] += 1

    # Core part of this sort : print the index if it has a value
    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


# count_sort(array)


def insertion_2(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            # NOT right, since the value shoud contiuously be moved
            '''if array[j] >= array[i]:
                array[j], array[i] = array[i], array[j]'''
            if array[j] <= array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break


# insertion_2(array)

#print("result", end='')
# print(array)

def count_sort(array):
    count=[0]*(max(array)+1)

    for i in range(len(array)):
        count[array[i]]+=1

    #print the elements of count

    for i in range(len(count)):
        for _ in range(count[i]):
            print(i, end=' ')
