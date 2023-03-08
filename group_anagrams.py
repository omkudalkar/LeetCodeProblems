'''
# Author : Om K
# Description : Groups anagrams tohgether 
'''
def anagrams(strs):
    # this is the list we will return. Whenever we are done finding the anagram(s) for a word, we will append that list.  
    anagram_groups = []
    # this set is so that we don't look at an anagram that has already been found. 
    words_found = set()
    i = 0
    # this loops over all the words in the strs input. This is our main loop. 
    while i < len(strs):
        if strs[i] not in words_found:
            # this list contains all the anagrams for a current word. 
            anagrams_for_curr_word = [strs[i]]
            curr_dict = {}
            # loops over curr_word in strs, and makes dict for char frequency. 
            for j in strs[i]:
                if j not in curr_dict:
                    curr_dict[j] = 1
                else:
                    curr_dict[j]+=1
            j = i+1
            # this loops over the rest of the words in strs so we can find matches for the curr_dict. 
            while j < len(strs):
                compare_dict = {}
                for k in strs[j]:
                    if k not in compare_dict:
                        compare_dict[k] = 1
                    else:
                        compare_dict[k] += 1
                # now we need to check if the two dicts match. 
                if curr_dict == compare_dict:
                    anagrams_for_curr_word.append(strs[j])
                    words_found.add(strs[i])
                    words_found.add(strs[j])
                j+=1
        if (anagrams_for_curr_word) and len(anagrams_for_curr_word)!=0:
            if anagrams_for_curr_word not in anagram_groups:
                anagram_groups.append(anagrams_for_curr_word)
        i+=1
    return(anagram_groups)

def main():
    input = ["eat","tea","tan","ate","nat","bat"]
    print(f"{anagrams(input)}")
main()