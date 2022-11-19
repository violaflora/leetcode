class Solution(object):
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    #if number is negative, uses string manip to add the negative sign to the beginning during reversal and converts back to int. if not, simply reverses string and converts back to int. if reversed val is out of our desired 32-bit range, return 0.
    if x < 0:
      x = int('-' + str(abs(x))[::-1])
    else:
      x = int(str(x)[::-1])
      
    if (x < -2**31) or (x > 2**31 - 1):
      return 0
    return x

print(Solution.reverse(Solution, -1211))