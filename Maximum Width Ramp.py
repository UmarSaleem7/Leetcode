def maxWidthRamp(self, nums: List[int]) -> int:
        maxArr = [0] * len(nums)
        maxNum = 0
        i = len(nums)-1
        while i >= 0:
            if nums[i] > maxNum:
                maxNum = nums[i]
            maxArr[i] = maxNum
            i -= 1
        left = 0
        diff = 0
        for right in range(len(nums)):
            while nums[left] > maxArr[right]:
                left += 1
            diff = max(diff, right - left)
        return diff
