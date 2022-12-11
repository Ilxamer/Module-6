from threading import Thread
import time
import requests

def get_html(link):
    text = requests.get(link).text
    print(f'({link} web-page contains {len(text)} symbols)')

links = ['https://ru.stackoverflow.com/','https://www.python.org/','https://www.youtube.com/','https://metanit.com/','https://py.checkio.org/']
threads = [Thread(target=get_html,args = (links[i],))for i in range(5)]

time_start = time.time()
for t in threads:
    t.start()
    t.join()
time_end = time.time()
time_consecutive = time_end - time_start
print(f'Time of parallel execution is {time_consecutive} ')

threads = [Thread(target=get_html,args = (links[i],))for i in range(5)]

time_start = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
time_end = time.time()
time_parallel = time_end - time_start
print(f'Time of parallel execution is {time_parallel} ')

print(f'Time"s difference is {abs(time_parallel - time_consecutive)}')
