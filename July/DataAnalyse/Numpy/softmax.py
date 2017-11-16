import numpy as np

#生成一个10*10 的随机二维数组，再加上1000
m = np.random.randn(10,10) * 10 + 1000
print(m)

#axis=1 表示在二维数组中沿着横轴进行取最大值的操作
m_row_max = m.max(axis = 1)
print(m_row_max,m_row_max.shape)

#每一行减去自己本行最大的数字，用到broadcast，reshape
#不这么处理会导致INF
m = m - m_row_max.reshape(10,1)
print(m)

#计算e的指数次幂
m_exp = np.exp(m)
print(m_exp,m_exp.shape)

#对每一行进行一次求和操作
m_exp_row_sum = m_exp.sum(axis=1).reshape(10,1)
print(m_exp_row_sum,m_exp_row_sum.shape)

#每一行的原始数据m_exp / 每一行的和
softmax = m_exp / m_exp_row_sum
print(softmax)

#校验softmax数组是否正确的方法是查看每一行的和是否是1
print(softmax.sum(axis=1).reshape(10,1))
