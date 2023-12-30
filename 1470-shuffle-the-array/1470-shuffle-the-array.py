class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        answers = []
        for i in range(n):
            answers .append(nums[i])
            answers .append(nums[i + n])
        return answers
    nums = [2, 5, 1, 3, 4, 7]
        