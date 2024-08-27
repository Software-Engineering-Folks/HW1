import myfile as mf

def test_successful():
    assert mf.bubblesort([1,6,5,3]) == [1,3,5,6]

def test_successful():
    assert mf.bubblesort([1,5,0,3]) == [0,1,3,5]

# def test_failed():
#     assert mf.bubblesort([1,6,5,3]) == [1,5,3,6]