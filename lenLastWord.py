class Solution(object):
  def lengthOfLastWord(self, s):
    #split solution
    words = s.split()
    return len(words[-1])
    """
    #solution doesn't use split. instead makes a list of bools and sums the last cluster of True values
    x = []
    counter = 0
    for i in s:
      x.append(i.isalpha())
    for i in x:
      if x[-1] == False:
        x.pop(-1)
    for i in x[::-1]:
      if i == True:
        counter += 1
      elif i == False:
        return counter
      return counter
    """