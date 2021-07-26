class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1]=digits[-1]+1
        if digits[-1] > 9:
            digits[-1]=str(digits[-1])
            pt1 = digits[-1][0].split()
            pt2= digits[-1][1].split()
            print(pt1,pt2)
            digits[-1]=int(pt1[0])
            digits.append(int(pt2[0]))

        return digits