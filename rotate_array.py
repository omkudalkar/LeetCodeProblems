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
    input_arr = [1,2,3,4,5,6,7]
    k=3
    rotated_array = rotate(input_arr, k)
    print(rotated_array)

main()