class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        def calculate(a, b):
            while b:
                a, b = b, a % b
            return a
        smallest = (2 * n) // calculate(2, n)
        return smallest
    
        