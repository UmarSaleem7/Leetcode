def canArrange(arr, k):
    frequencies = [0] * k

    for x in arr:
        remainder = x % k
        frequencies[remainder] += 1

    if frequencies[0] % 2 != 0:
        return False

    for i in range(1, k // 2 + 1):
        if frequencies[i] != frequencies[k - i]:
            return False

    return True
