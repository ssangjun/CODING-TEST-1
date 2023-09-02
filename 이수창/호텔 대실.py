import heapq

def solution(book_time):
    def changeTime(str):
        str = str.split(":")
        hour = int(str[0]) * 60
        minute = int(str[1])
        return hour + minute

    book_time.sort(key=lambda x: x[0])  
    q = []
    heapq.heapify(q)
    
    for i in range(len(book_time)):
        start_time = book_time[i][0]
        
        if len(q) == 0:
            heapq.heappush(q, book_time[i][1])
            continue
        
        end_time = heapq.heappop(q)
        
        if changeTime(start_time) < changeTime(end_time)+10: 
            heapq.heappush(q, end_time)
        
        heapq.heappush(q, book_time[i][1])
    
    return len(q)  
