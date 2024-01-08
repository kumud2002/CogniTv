def allocateBooks(n, m, time):
    s = sum(time)
    maxTime = max(time)
    l = maxTime
    r = s
    answer = s

    while l <= r:
        mid = (l + r) // 2
        days = 1
        currentTime = 0

        for j in range (m):
            currentTime += time[j]
            if currentTime > mid:
                days += 1
                currentTime = time[j]

        if days <= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
          
    return answer

