"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 """

def closest_sum(nums,t):
    n = len(nums)
    sums = []
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                sum_ = nums[i] + nums[j] + nums[k]
                sums.append(sum_)
    #print(sums)

    sort_array = []    
    for i in range(len(sums)):
        inner = []
        inner.append(abs(sums[i]-t))
        inner.append(sums[i])
        sort_array.append(inner)

    sort_array.sort(key=lambda x: x[0])
    #print(sort_array)
    return sort_array[0][1]
        
nums = [-1,2,1,4]
target = 1

print(closest_sum(nums,target))
