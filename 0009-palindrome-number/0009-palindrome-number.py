class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        var_x = str(x)
        return var_x == var_x[::-1]
        