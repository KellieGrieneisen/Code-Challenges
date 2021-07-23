# An integer is a palindrome when it reads the same backward as forward. 
# For example, 121 is palindrome while 123 is not.
# (Leetcode question-level,easy)

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        self.x=x
        num_list=list(str(x))
        half = len(num_list)//2
        first_half=num_list[:half]
        last_half=num_list[half:]
        print(len(num_list))

        if (len(num_list) % 2)==0:

            if ''.join(first_half) == ''.join(reversed(last_half)):
                print('isssa palindrome!')
            else:
                print('not a palindrome..')

        elif (len(num_list) % 2)!=0:
            mid=last_half[0]
            print(mid)
            last_half.pop(0)
            if ''.join(first_half) == ''.join(reversed(last_half)):
                print('isssa palindrome!')
            else:
                print('not a palindrome..')
            

            
            
