#-*-coding:utf-8-*-
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

## 直线的斜率m 和 最佳拟合直线的纵截距

xs = np.array([1,2,3,4,5], dtype=np.float64)
ys = np.array([5,4,6,5,6], dtype=np.float64)

def best_fit_slope_and_intercept(xs,ys):
    m = (((mean(xs)*mean(ys)) - mean(xs*ys)) /
         ((mean(xs)*mean(xs)) - mean(xs*xs)))

    b = mean(ys) - m*mean(xs)

    return m, b

m, b = best_fit_slope_and_intercept(xs,ys)

regression_line = [(m*x)+b for x in xs]

# plt.scatter(xs,ys,color='#003F72')
# plt.plot(xs, regression_line)
# plt.show()


predict_x = 7
predict_y = (m*predict_x)+b

plt.scatter(xs,ys,color='#003F72',label='data')
plt.plot(xs, regression_line, label='regression line')
# plt.plot(predict_x, predict_y, color='#003F72',label='p')
plt.legend(loc=4)
plt.show()
