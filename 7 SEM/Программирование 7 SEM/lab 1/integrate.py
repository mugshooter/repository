import math
import threading
import timeit
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Часть 1: Последовательное интегрирование
def integrate(f, a, b, *, n_iter=1000):
    dx = (b - a) / n_iter
    total_sum = 0
    for i in range(n_iter):
        x = a + i * dx
        total_sum += f(x) * dx
    return total_sum

# Часть 1.2: Thread + Lock
def integrate_threaded(f, a, b, n_threads, n_iter=1000):
    iters_per_thread = n_iter // n_threads
    dx = (b - a) / n_iter
    shared_sum = [0.0]
    lock = threading.Lock()

    def worker(start_idx):
        local_sum = 0
        for i in range(start_idx, start_idx + iters_per_thread):
            x = a + i * dx
            local_sum += f(x) * dx
        with lock:
            shared_sum[0] += local_sum

    threads = []
    for i in range(n_threads):
        t = threading.Thread(target=worker, args=(i * iters_per_thread,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return shared_sum[0]

# Часть 3: Futures (задание 2.1) 
def integrate_futures(f, a, b, n_workers, n_iter=1000, executor_type=ThreadPoolExecutor):
    dx = (b - a) / n_iter
    step = n_iter // n_workers
    
    def partial_sum(start):
        return sum(f(a + i * dx) * dx for i in range(start, start + step))

    with executor_type(max_workers=n_workers) as executor:
        results = executor.map(partial_sum, range(0, n_iter, step))
    return sum(results)