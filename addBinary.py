class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #iterates through binary strings backwards to get decimal values of them, adds them together in decimal and then returns the sum in binary
        a, b = str(a)[::-1], str(b)[::-1]
        mult = 1
        sum1 = 0
        sum2 = 0
        for i in a:
            sum1 += int(i) * mult
            mult *= 2
        mult = 1
        for i in b:
            sum2 += int(i) * mult
            mult *= 2
        return bin(sum1+sum2)[2:]