# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Input: nums = [4,1,2,1,2]
# Output: 4

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(set(nums))
        
        
        count=0
        
        
        for num in nums:
            current =nums[-1]
            # print(num)
            if num == current:
                nums.pop(num)
                nums.pop(current)
        print(nums)
                
            
            
                
            

            
        

            
            
            
            
            