class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digits[-1]=digits[-1]+1
        # if digits[-1] > 9:
        #     digits[-1]=str(digits[-1])
        #     pt1 = digits[-1][0].split()
        #     pt2= digits[-1][1].split()
        #     print(pt1,pt2)
        #     digits[-1]=int(pt1[0])
        #     digits.append(int(pt2[0]))
        number=''
        for digit in digits:
            number = number + str(digit)
        number= int(number) + 1
        digits=[]
        for i in str(number):
            digits.append(int(i))

        
        return digits

    # accepted by leetcode !! 
    #  24 ms, faster than 41.64% of Python online submissions for Plus One.
    # 13.4 MB, less than 71.00% of Python online submissions for Plus One.