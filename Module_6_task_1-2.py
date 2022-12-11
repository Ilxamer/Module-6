from threading import Thread
import time

def get_thread(thread_name):
    time.sleep(1)
    for i in range(5):
        print(f"Thread's name is {thread_name}")



threads = [Thread(target = get_thread,args = (i+1,))for i in range(5)]

start = time.time()
for t in threads:
    t.start()
    t.join()
end = time.time()
time_consecutive = end - start
print(f'Time_1: {time_consecutive}')


start = time.time()

threads = [Thread(target = get_thread,args = (i+1,))for i in range(5)]

for t in threads:
    t.start()

for t in threads:
    t.join()

end = time.time()
time_parallel = end - start
print(f'Time_2: {time_parallel}')
difference = time_parallel - time_consecutive
print(f'Разница в выполнении: {abs(difference)}')
