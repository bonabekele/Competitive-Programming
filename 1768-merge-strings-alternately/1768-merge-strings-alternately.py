class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merge.append(word1[i])
            merge.append(word2[j])
            i += 1
            j += 1
        merge += word1[i:]
        merge += word2[j:]
        return ''.join(merge)
        