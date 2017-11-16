#codeing:utf-8
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x = np.arange(0.,10,0.2)

y1 = np.cos(x)
y2 = np.sin(x)
y3 = np.sqrt(x)

plt.plot(x,y1,color='blue',linewidth=1.5,linestyle='-',marker='.',label=r'$y = cos{x}$')

plt.plot(x,y2,color='green',linewidth=1.5,linestyle='-',marker='*',label=r'$y = sin{x}$')

plt.plot(x,y3,color='m',linewidth=1.5,linestyle='-',marker='x',label=r'$y = \sqrt{x}$')

#将figure设置的画布大小分成几个部分，参数‘221’表示2(row)x2(colu),即将画布分成2x2，两行两列的4块区域，1表示选择图形输出的区域在第一块，图形输出区域参数必须在“行x列”范围 ，此处必须在1和2之间选择——如果参数设置为subplot(111)，则表示画布整个输出，不分割成小块区域，图形直接输出在整块画布上
ax = plt.subplot(111)
ax.spines['top'].set_color('none')   #去掉上边线，即颜色设置为白色
ax.spines['right'].set_color('none') #去掉右边线，即颜色设置为白色
#移动下边线，相当于移动x轴
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
#移动左边边线框，相当于移动y轴
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
#设置x，y轴的刻度值范围
plt.xlim(x.min()*1.1,x.max()*1.1)
plt.ylim(-1.5,4.0)
plt.xticks([2,4,6,8,10],[r'2',r'4',r'6',r'8',r'10'])
plt.yticks([-1.0,0.0,1.0,2.0,3.0,4.0],[r'-1.0',r'0.0',r'1.0',r'2.0',r'3.0',r'4.0'])

#设置标题、x轴、y轴
plt.title(r'$the \ function \ figure \ of \ cos() , \sin() \ and \ sqrt() $',fontsize=19)
plt.xlabel(r'$the \ input \ value \ of \ x $',fontsize=18,labelpad=88.8)
plt.ylabel(r'$y = f(x) $',fontsize=18,labelpad = 12.5)

#在数据图中添加文字描述text：
plt.text(4,1.68,r'$x \in [0.0, \ 10.0]$',color='k',fontsize=15)
plt.text(4,1.38,r'$y \in [-1.0, \ 4.0]$',color='k',fontsize=15)

#在数据图中给特殊点添加注解 annotate：
plt.scatter([8,],[np.sqrt(8),],50,color='m') #使用散点图放大当前点
#添加特殊的箭头
plt.annotate(r'$2\sqrt{2}$', xy=(8, np.sqrt(8)), xytext=(8.5, 2.2), fontsize=16, color='#090909', arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=0.1', color='#090909'))

#设置图例
#plt.legend(['cos(x)', 'sin(x)', 'sqrt(x)'], loc='upper right')
plt.legend(loc='upper right') 
#显示网格线
plt.grid(True)
plt.show()

