def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i, num in enumerate(numbers):
        while True:
            if not stack:
                stack.append(i)
                break
                
            idx = stack[-1]
            
            if numbers[idx] >= num:
                stack.append(i)
                break
                
            answer[idx] = num
            stack.pop()
        
    return answer
