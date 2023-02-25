def single_number(input_arr):
    dict_of_numbers : dict = {}

    if len(input_arr) == 1:
        return input_arr[0]

    for i in input_arr:
        if i not in dict_of_numbers:
            dict_of_numbers[i]=1
        else:
            dict_of_numbers[i]+=1

    for i in dict_of_numbers:
        if dict_of_numbers[i]==1:
            return i

def tester():
    assert (single_number([2,2,1])) == 1
    assert (single_number([4,1,2,1,2])) == 4
    assert (single_number([1])) == 1

def main():
    tester()

main()