class Solution(object):
  def numJewelsInStones(self, jewels, stones):
    #uses list comprehension to convert string to list instead of typecasting, uses for loop and counter var to sum jewel matches and returns counter
    counter = 0
    x = [x for x in jewels]
    for i in stones:
      if i in x:
        counter += 1
    return counter
