def time_to_int(time):
    hh, mm = tuple(map(int, time.split(":")))
    return mm + (hh*60)

CLEANING_TIME = 10
MAX_TIME = time_to_int("23:59")

def solution(book_time):   
    time_line = [0 for _ in range(MAX_TIME)]
        
    for times in book_time:
        start_time = time_to_int(times[0])
        end_time = min(time_to_int(times[1]) + CLEANING_TIME, MAX_TIME)
        
        for i in range(start_time, end_time):
            time_line[i] += 1

    return max(time_line)
  
