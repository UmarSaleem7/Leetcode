def arrayRankTransform(arr):
    dic = {}
    sortedArr = sorted(list(set(arr)))
    result = []
    for rank in range(len(sortedArr)):
        num = sortedArr[rank]
        dic[num] = rank + 1

    for num in arr:
        result.append(dic[num])

    return result
