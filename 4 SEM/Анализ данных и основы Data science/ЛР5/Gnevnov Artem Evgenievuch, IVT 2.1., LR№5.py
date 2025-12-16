import numpy as np
import matplotlib.pyplot as plt

def discrete(data):
    data_sorted = np.sort(data.flatten())
    unique_values, counts = np.unique(data_sorted, return_counts=True)
    probabilities = counts / len(data_sorted)
    probabilities = np.cumsum(probabilities)
    return unique_values, probabilities

def interval(data):
    sorted_data = np.sort(data[0])
    n = np.sum(data[1])
    intervals = data[0]
    interval_lengths = np.diff(intervals.flatten())
    interval_lengths = np.cumsum(interval_lengths)
    interval_probabilities = interval_lengths / n

    return intervals, interval_probabilities

data_discrete = np.array([[9, 12, 13, 14, 15, 16, 17, 18, 19, 21, 23, 27],
                           [1, 2, 3, 6, 5, 3, 2, 1, 1, 1, 1, 0]])
values_discrete, ecdf_discrete = discrete(data_discrete)

plt.step(values_discrete, ecdf_discrete, where='post')
plt.title('Дискретный вариационный ряд')
plt.xlabel('Значения')
plt.ylabel('Вероятность')
plt.show()


data_interval = np.array([[200, 400, 600, 800, 1000, 1200],
                           [30, 38, 50, 31, 22, 13],
                           [0.163, 0.207, 0.272, 0.168, 0.120, 0.07]])
intervals, ecdf_interval = interval(data_interval)

plt.step(intervals.flatten()[:-1], ecdf_interval, where='post')
plt.title('Интервального вариационный ряд')
plt.xlabel('Значения')
plt.ylabel('Вероятность')
plt.show()