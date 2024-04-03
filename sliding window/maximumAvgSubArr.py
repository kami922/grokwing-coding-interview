'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
'''
def maxSubArrAvg(arr:list,k:int) -> int:
    avg = []
    _sum, start =0,0
    for end in range(len(arr)):
        _sum += arr[end]
        
        if end >= k-1:
            avg.append(_sum/k)
            _sum -= arr[start]
            start += 1
    return max(avg)      
            
arr1 = [1,12,-5,-6,50,3]
ra = 4

print(maxSubArrAvg(arr1,ra))