def dcount(dictionary):
    d_list = []
    largest = 0
    for d in dictionary:
        if dictionary[d] > largest:
            largest = dictionary[d]
            d_list = d
        elif dictionary[d] == largest:
            largest = largest
    return d_list

def longest_repetition(nums):
    if len(nums) > 0:
        l = 0
        count = 0
        bucket = {}
        for n in nums:
            while l < len(nums):
                if n == nums[l]:
                    count += 1
                l += 1
            if n not in bucket:
                bucket[n] = count
            count = 0
            l = 0
                
        return dcount(bucket)
    else:
        return None
