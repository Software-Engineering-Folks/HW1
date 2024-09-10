'''This module has a docstring. It's right here. You are looking at it right now.'''
import subprocess


def random_array(arr):
    '''This function creates an array of random integers. 
    The length of the array is the same as the length of the input array.'''

    shuffled_num = None

    for iter in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check='True')
        arr[iter[0]] = int(shuffled_num.stdout)
    return arr
