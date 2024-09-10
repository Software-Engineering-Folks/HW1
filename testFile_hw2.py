import hw2_debugging

def test_sorted_input():
    assert hw2_debugging.merge_sort([1,2,3,4]) == [1,2,3,4]

def test_reverse_sorted_input():
    assert hw2_debugging.merge_sort([4,3,2,1]) == [1,2,3,4]

def test_general_input():
    assert hw2_debugging.merge_sort([5,3,7,1]) == [1,3,5,7]
