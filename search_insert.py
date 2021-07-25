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
      
        print("looking for",target,"in",nums)

        if target in set(first_half):
            return first_half.index(target)
                
        elif target not in set(nums):
            nums.append(target)
            nums.sort()
        print(target,"indecy is/would be",nums.index(target))
        print(nums)
        return(nums.index(target))

