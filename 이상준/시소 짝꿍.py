def solution(weights):
    answer = 0
    counts = [0] * 2001
    
    for w in weights:
        counts[w] += 1
    
    for i in range(100, 1001):        
        answer += counts[i] * (counts[i]-1) // 2
        answer += counts[i] * counts[int(i*2)]
        if (i*4/3)%1 == 0:
            answer += counts[i] * counts[int(i*4/3)]
        if (i*3/2)%1 == 0:
            answer += counts[i] * counts[int(i*3/2)]

    return answer
