class Solution(object):
    def runningSum(self, nums):
        """
        Nilai saat ini ditambahkan nilai sebelumnya
	more optimal
	for i in range(1, len(nums)):
	        nums[i] += nums[i-1]
        """
        prev = 0
        o = [ ]
        for d in nums:
            o.append(d+prev)
            prev = d+prev
        return o