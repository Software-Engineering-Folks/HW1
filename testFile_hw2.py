import HW2.hw2_debugging as testModule

def test_sorted_input():
    assert testModule.merge_sort([1,2,3,4]) == [1,2,3,4]

def test_reverse_sorted_input():
    assert testModule.merge_sort([4,3,2,1]) == [1,2,3,4]

def test_general_input():
    assert testModule.merge_sort([5,3,7,1]) == [1,3,5,7]
