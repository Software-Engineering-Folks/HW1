'''This file is created by Software Engineering Folks. 
It is used for testing ./src/myFile.py'''
import src.my_file as mf

def test_successful():
    '''testing bubble sort'''
    assert mf.bubblesort([1,6,5,3]) == [1,3,5,6]

# def test_failed():
#     assert mf.bubblesort([1,6,5,3]) == [1,5,3,6]
