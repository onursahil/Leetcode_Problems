def minOperations(nums1, nums2):
    sum1 = sum(nums1)
    sum2 = sum(nums2)
    
    if sum1==sum2:
        return 0
    elif sum1>sum2:
        larger_sum_nums = nums1
        smaller_sum_nums = nums2
    else:
        larger_sum_nums = nums2
        smaller_sum_nums = nums1
    
    sum_diff = abs(sum1-sum2)
         
    gains_in_larger_array = [num-1 for num in larger_sum_nums]
    gains_in_smaller_array = [6-num for num in smaller_sum_nums]
    
    gains = gains_in_larger_array + gains_in_smaller_array
    gains.sort(reverse = True)
    
    count = 0
    
    for i in range(len(gains)):
        sum_diff -= gains[i]
        count += 1
        
        if sum_diff <= 0:
            return count
    
    return -1


nums1 = [1,2,3,4,5,6]
nums2 = [1,1,2,2,2,2]
result = minOperations(nums1, nums2)
print(result)