class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        good_pairs = 0
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for j in count.values():
            good_pairs += (j * (j - 1)) // 2
        return good_pairs
        nums = [1,2, 3, 1,1,3]
        
        
        
        