def bubblesort(array):
    for i in range(0, len(array)- 1):
        for j in range(i,len(array)):
            if (array[i] > array[j]):
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

# print("hello world")