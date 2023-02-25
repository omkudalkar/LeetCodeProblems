def move_zeroes(nums) -> None:
    i :int = 0

    zero_count : int = 0

    for i in nums:
        if i == 0:
            zero_count+=1

    inner_loop_runs : int = 0
    while inner_loop_runs < zero_count:
        i=0
        while i < len(nums)-1:
            if nums[i] == 0:
                temp = nums[i+1]
                nums[i+1] = 0
                nums[i] = temp
            i+=1
            #print(nums)
        inner_loop_runs+=1

    return nums

def tester():
    assert (move_zeroes([0,1,0,3,12])) == [1,3,12,0,0]
    assert (move_zeroes([0,1,0,3,0,12])) == [1,3,12,0,0,0]
    assert (move_zeroes([0,1,0,3,12,13,0,0,15,16,17,0])) == [1,3,12,13,15,16,17,0,0,0,0,0]
    assert (move_zeroes([0])) == [0]
    assert (move_zeroes([])) == []
    assert (move_zeroes([1,3,12])) == [1,3,12]

def main():
   tester()

main()