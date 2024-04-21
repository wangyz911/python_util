import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# 已知数据：最低值、最高值和平均值
T_min = 10  # 最低温度
T_max = 30  # 最高温度
T_avg = 20  # 平均温度

# 创建正弦拟合函数
def sine_func(x, a, b, c, d):
    return a * np.sin(b * x + c) + d

# 定义正弦拟合参数
a = (T_max - T_min) / 2
b = 2 * np.pi / 24
c = 0
d = T_avg

# 计算每个小时的积分值
integral_results = []
for hour in range(24):
    integral_result, _ = quad(lambda x: a * np.sin(b * x + c) + d, hour, hour + 1)
    integral_results.append(integral_result)

# 绘制每小时的积分值图像
plt.figure()
plt.plot(range(24), integral_results, marker='o')
plt.xlabel('Hour')
plt.ylabel('Integral Value')
plt.title('Integral Value for Each Hour')
plt.grid(True)
plt.show()
