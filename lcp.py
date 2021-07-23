# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        self.strs=strs
        current_letter=""
        common_prefix=""

        if len(strs)==0:
            return common_prefix

        for obj in range(0,len(strs[0])):
            for idx,word in enumerate(strs):
               
                try:
                    if idx == 0:
                        current_letter=word[obj]
                    elif word[obj] != current_letter:
                        return common_prefix
                    else:
                        pass
                except IndexError:
                    return common_prefix

            common_prefix = common_prefix + current_letter
            current_letter=""

        return common_prefix
            