#coding=utf-8

from numpy import *
import operator

#创建数据集和标签
def createDataSet():
    group = array([[1.0,0.9],[1.0,1.0],[0.1,0.2],[0.0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

#KNN 分类器
def kNNClassify(newInput,dataSet,labels,k):
    #step1.求newInput 和 数据集的dataSet之间的欧式距离，进行排序
    #shape[0] 是取第一维度，即行的数量
    numSamples = dataSet.shape[0]
    #tile的作用是扩展newInput数组，编程numSamples 行，1列
    diff = tile(newInput,(numSamples,1)) - dataSet
    #对于数组中的每个数进行求平方的运算
    squaredDiff = diff ** 2
    #把数组的每一行进行求合
    squaredDist = sum(squaredDiff,axis = 1)
    #对数组中的每个数进行开方
    distance = squaredDist ** 0.5
    #对数组进行排序，返回的是每个数的index的从小到大排列
    sortedDistIndices = argsort(distance)

    #step2.取排序的前最小k个数，寻找对应的label标签，存放在字典中
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistIndices[i]]
        #字典中的get函数是获取当前key的value，如果不存在则设置默认值0
        classCount[voteLabel] = classCount.get(voteLabel,0) + 1
    print('classCount = ',classCount)
    maxCount = 0

    #step3.在字典中找最大的分类
    for key,value in classCount.items():
        if value>maxCount:
            maxCount = value
            maxIndex = key

    return maxIndex



if __name__ == '__main__':
    dataSet,labels = createDataSet()

    textX = array([1.2,1.0])
    k = 3
    outputLabel = kNNClassify(textX,dataSet,labels,3)
    print("Your input is:", textX, "and classified to class: ", outputLabel)









