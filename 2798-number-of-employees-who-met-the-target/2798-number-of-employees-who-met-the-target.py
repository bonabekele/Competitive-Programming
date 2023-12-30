class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        number=0
        for works in hours:
            if works>=target:
                number+=1
        return number
    
        
        