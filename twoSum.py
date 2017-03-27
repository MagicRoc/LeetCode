__author__ = 'MagicRoc'

class Solution(object):

	def twoSum(self,nums,target):

		l=len(nums)

		for num1,i in zip(nums,range(l)):

			for num2,j in zip(nums,range(l)):

				if(i==j):

					continue

				if(num1+num2==target):

					return [i,j]

		return None

