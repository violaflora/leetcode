class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)): #iterate through nums
      for j in range(i+1, len(nums)): #checks every other number
        if nums[i] + nums[j] == target: #if both numbers add up to the target value
          return [i, j] #return indicies of points