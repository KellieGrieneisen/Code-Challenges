# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# EXAMPLE CODE:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        half = int(len(nums)/2)
        first_half = nums[:half]
        last_half= nums[half:]
        print(first_half,"**",last_half)

        if target in set(first_half):
            for idx,num in enumerate(first_half):
                if target==num:
                    print(idx)
                
            
        elif target in last_half:
            for idx,num in enumerate(last_half):
                if target==num:
                    print(idx)


        elif target not in set(nums):
            if target in range(first_half[0],first_half[-1]):
                for i,num in first_half:
                    print(i,num)
                    if target > num[i] and target < num[i+1]:
                        print(i+1)


            elif target in range(last_half[0],last_half[-1]):
                for i,num in enumerate(last_half):
                    if target > num[i] and target < num[i+1]:
                        print(i+1)

