class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # this code allocates extra space for a second array
        # check_nums=[]
        # for num in nums:
        #     if num not in check_nums:
        #         check_nums.append(num)
        #     else:
        #         num=None
                
        # nums = check_nums
        # return f'{len(nums)}, {sorted(nums)}'

        # solve without allocating extra space to run in O(1)
        k = len(set(nums))
        return k, list(set(nums))

        
