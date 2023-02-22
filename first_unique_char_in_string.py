'''
Author : Om K
Time Complexity : O(N)
'''
def firstUniqChar(s: str) -> int:

    # dict to store unique char as keys and the value for each key is index where that char is seen. 
    dict_of_chars : dict = {} 

    # normalize input so that uppercase and lowercase is not an issue. 
    normalized_input : str = s.lower() 
    i :int = 0

    # creates dictionary with unique chars and locations where they are seen. 
    while i < len(normalized_input):
        if normalized_input[i] not in dict_of_chars:
            dict_of_chars[normalized_input[i]] = [i]
        else:
            dict_of_chars[normalized_input[i]].append(i)
        i+=1

    first_unique_index = -1
    #first_unique_char = ""

    for i in dict_of_chars:
        # we only check those that are unique. 
        if len(dict_of_chars[i]) ==1:
            # if first_unique_char is still -1 at this point, then that means that 
            # we haven't found any unique char yet, so we can directly set the unique
            if first_unique_index == -1:
                first_unique_index = dict_of_chars[i][0]
                #first_unique_char = i

            # if not -1, means there is a pre-existing smallest index, so we need to check if 
            # the current chars index is snaller. 
            else:
                if first_unique_index > dict_of_chars[i][0] :
                    first_unique_index = dict_of_chars[i][0]
                    #first_unique_char = i
    
    return first_unique_index






def main():
    unique_index = firstUniqChar("aabb")
    print(unique_index)

main()