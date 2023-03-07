def threesum(nums):
    ret_arr = []
    # base case / trivial case. 
    if len(nums) < 3:
        return []
    else:
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                k = j + 1
                while k < len(nums):
                    if (nums[i] + nums[j] + nums[k] == 0):
                        triplet = []
                        triplet.append(nums[i])
                        triplet.append(nums[j])
                        triplet.append(nums[k])
                        # this allows us to check for duplicates. 
                        if sorted(triplet) not in ret_arr:
                            ret_arr.append(sorted(triplet))
                    k+=1
                j+=1
            i+=1
        return ret_arr

a  = threesum([-1,0,1,2,-1,-4])
print(a)

