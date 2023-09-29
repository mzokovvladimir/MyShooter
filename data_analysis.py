from setting import PATH_FILE_STAT
import matplotlib.pyplot as plt
import numpy as np
from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename, encoding='UTF-8') as f:
        return f.readlines()


my_data: List[int] = read_file(PATH_FILE_STAT)
total: List[int] = [int(i.split()[0]) for i in my_data]
missed: List[int] = [int(i.split()[1]) for i in my_data]
timer: List[float] = [float(i.split()[2]) for i in my_data]
level: List[int] = [int(i.split()[3]) for i in my_data]

width: float = 0.4
x_list: List[int] = list(range(1, len(level) + 1))
y1_list = total
y2_list = missed
y3_list = timer
y4_list = level
x_indexes = np.arange(1, len(x_list) + 1)
print(type(x_indexes))

plt.figure()
plt.subplot(1, 2, 1)

plt.title('Line graph')
plt.xticks(x_list, [str(i) for i in range(1, len(y1_list) + 1)])
plt.xlabel('levels')
plt.ylabel('stat')

plt.plot(x_list, y1_list, label='Total', marker='o')
plt.plot(x_list, y2_list, label='Missed', marker='^')
plt.plot(x_list, y3_list, label='Time', marker='1')

plt.subplot(1, 2, 2)
plt.title('Game Stat Bars')
plt.xticks(x_indexes, [str(i) for i in range(1, len(level) + 1)])
plt.xlabel('levels')
plt.ylabel('stat')

plt.bar(x_indexes - (width / 2), y1_list, label='Total', width=width)
plt.bar(x_indexes + (width / 2), y2_list, label='Missed', width=width)
plt.bar(x_indexes - (width / 2), y3_list, label='Time', width=width)
plt.legend()
plt.show()
