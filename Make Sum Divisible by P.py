def minSubarray(nums, p):
    arrSum = sum(nums)
    rem = arrSum % p
    if rem == 0:
        return 0
    for num in nums:
        if num == rem:
            return 1
    sumMap = {0: -1}
    currentSum = 0
    ans = len(nums)
    for i, num in enumerate(nums):
        currentSum = (currentSum + num) % p

        if (currentSum - rem) % p in sumMap:
            ans = min (ans, i - sumMap[(currentSum - rem) % p])

        sumMap[currentSum] = i

    if ans < len(nums):
        return ans
    return -1

