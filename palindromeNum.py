class Solution(object):
  def isPalindrome(self, x):
    #string-based solution
    if x < 0:
      return False
    x = str(x)
    y = x[::-1]
    if x == y:
        return True
    return False
    """
    #int-based solution
    if x < 0:
      return False
    num = x
    y = 0
    while num > 0:
      z = num % 10
      num = num // 10
      y = y * 10 + z
    return x == y
    """