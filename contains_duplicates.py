def contains_duplicates(input_arr):
    dict_of_nums : dict = {}
    if len(input_arr) == 0 or len(input_arr) == 1:
        return False
    for i in input_arr:
        if i not in dict_of_nums:
            dict_of_nums[i] = 1
        else:
            dict_of_nums[i]+=1
            return True
    return False

def tester():
    assert (contains_duplicates([1,2,3,1])) == True
    assert (contains_duplicates([1,2,3,4])) == False
    assert (contains_duplicates([1])) == False
    assert (contains_duplicates([])) == False

def main():
    tester()

main()