def solution(x, y, n):
    answer = 0
    dp = {}
    data = [x]
    dp[x] = 0
    if x == y:
        return 0
    while data:
        newData = []
        for d in data:
            for e in [d + n, d * 2, d * 3]:
                if e > y or dp.get(e) is not None:
                    continue
                if e == y:
                    return dp[d] + 1
                dp[e] = dp[d] + 1
                newData.append(e)
        data = newData
    return -1