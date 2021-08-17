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
        

        # the best solution to maximize space is to use XOR
        # the xor of  a number and itself is 0
        # the xor of a number and 0 is the number
        # example: 7^3^4^5^3^4
        #  can look like 7 ^(3^3)^(4^4)^(5^5)
        #  7 ^ 0 ^ 0 ^ 0
        # giving a return of 7
        # solution found, read through and then tested to understanding
        current=nums[0]

        for i in range(1,len(nums)):
            current = current ^ nums[i]

        print(current)




        # not a plausible solution.
        # brute force code

        # s = sorted(nums)
        
        # print(s)
        # for i,num in enumerate(s):
           
        #     num=str(num)
        #     if s[i+1] != None:
        #         try:
                    
        #             if s[i]==s[i+1]:
        #                 s.remove(s[i+1])
        #                 s.remove(s[i])
                
        #         except IndexError as error:
        #             print(nums)
            
        #     elif len(s)==1:
        #         nums=s
        #         print(nums[0])


        
                       
            
            
                
            

            
        

            
            
            
            
            