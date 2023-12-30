class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = celsius + 273.15
        fahrenheit = celsius * 1.80 + 32.00
        formatted_kelvin = float(format(kelvin, '.5f'))
        formatted_fahrenheit = float(format(fahrenheit, '.5f'))
        both_temp = []
        both_temp.append(formatted_kelvin)
        both_temp.append(formatted_fahrenheit)
       
        return both_temp




