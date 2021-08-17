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
        
        
        s = sorted(nums)
        
        print(s)
        for i,num in enumerate(s):
            # current =nums[0]
            # print(num)
            # print(current,"+")
            # if len(nums) > 1 and num == current and i != 0:
            #         nums.pop(num)
            #         nums.pop(0)
            num=str(num)
            if len(nums)==1:
                return nums
            elif len(nums)>1 and num[i]==num[i+1]:
                nums.pop(num[i])
                nums.pop(num[i+1])
            
            

            

                
                

            
        print(nums)
                
            
            
                
            

            
        

            
            
            
            
            