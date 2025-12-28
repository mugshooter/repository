import threading
import requests
import math

# 1.1: Имена потоков
def print_thread_names():
    def task():
        print(f"Поток: {threading.current_thread().name}")
    for i in range(3):
        threading.Thread(target=task, name=f"MyThread-{i}").start()

# 1.4: Факториал в потоках 
def thread_factorial(n):
    res = [1]
    lock = threading.Lock()
    def part(start, end):
        p = 1
        for i in range(start, end + 1): p *= i
        with lock: res[0] *= p
    
    mid = n // 2
    t1 = threading.Thread(target=part, args=(1, mid))
    t2 = threading.Thread(target=part, args=(mid + 1, n))
    t1.start(); t2.start()
    t1.join(); t2.join()
    return res[0]