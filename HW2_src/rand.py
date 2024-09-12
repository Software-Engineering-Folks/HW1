'''This module has a docstring. It's right here. You are looking at it right now.'''
import secrets

def random_array(arr):
    '''This function creates an array of random integers. 
    The length of the array is the same as the length of the input array.'''

    for enum_array in enumerate(arr):
        arr[enum_array[0]] = secrets.randbelow(20) + 1
    return arr
