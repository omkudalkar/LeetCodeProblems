'''
Author: Om K
Time Complexity: O(N^2)
'''
def two_sum(nums : list, target: int):
    i: int = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if (nums[i] + nums[j] == target):
                return ([i,j])
            j+=1
        i+=1

def main():
    test_twosum()

def test_twosum():
    assert two_sum([3,3], 6) == [0,1]
    assert two_sum([2,7,11,15], 9) == [0,1]
    assert two_sum([3,2,4], 6) == [1,2]

 

main()
