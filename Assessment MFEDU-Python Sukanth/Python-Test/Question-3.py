"""
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

 
def median_of_array(nums1, nums2):
    def merge(nums1, nums2):
        res = []
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        while i < m:
            res.append(nums1[i])
            i += 1
        while j < n:
            res.append(nums2[j])
            j += 1

        return res
    
    merged_array = merge(nums1, nums2)
    merged_len = len(merged_array)
    if merged_len % 2 == 1:
        result = merged_array[merged_len//2]
        return float(result)
    else:
        n1 = merged_array[(merged_len//2)-1]
        n2 = merged_array[merged_len//2]
        result = (n1 + n2) / 2
        return result
    

nums1 = [1,3]
nums2 = [2,4]
print(median_of_array(nums1, nums2))
