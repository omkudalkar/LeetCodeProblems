'''
Author: Om K
Time Complexity = O(N)
'''
def rotate(input_arr : list, k : int):
    i :int = k
    new_arr: list  = []
    while i > 0 :
        last_element :int = input_arr.pop()
        new_arr.insert(0,last_element)
        i-=1
    
    for i in input_arr:
        new_arr.append(i)

    return new_arr

def main():
    test_rotate()


def test_rotate():
    assert rotate([1,2,3,4], 1) == [4,1,2,3]
    assert rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
    assert rotate([1,2,3,4], 4) == [1,2,3,4]


main()
