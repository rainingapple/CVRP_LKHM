# 绘制CVRP训练loss下降情况

import matplotlib.pyplot as plt

log_file = open("record/CVRP_train.out",encoding="utf-8").readlines()

loss_list = []

for line in log_file:
    if line[0] == 'E':
        line = line.split()
        loss_list.append(float(line[3]))

plt.plot(loss_list)
plt.show()