# https://www.pythontutorial.net/python-concurrency/python-threading/
from time import sleep, perf_counter

def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    print(f'The task {id} completed')


start_time = perf_counter()

for n in range(1, 11):
    task(n)

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')