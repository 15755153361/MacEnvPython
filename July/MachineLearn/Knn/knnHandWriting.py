#coding=utf-8
import numpy as np
import operator
from os import listdir
#intX是测试集 dataSet是训练集 labels是标签，k是分类
def classifyKnn(intX,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]
    #intX本身是一个1024维度的vector，扩展到dataSetSize行，列只扩展一次，相当于复制数据dataSetSize次
    diffMat = np.tile(intX,(dataSetSize,1)) - dataSet
    #矩阵每个数字做平方
    sqDiffMat = diffMat ** 2
    #axis = 0是在列的方向操作，axis=1是在行的方向上操作
    row_SumDistances = sqDiffMat.sum(axis = 1)
    oushi_distance = row_SumDistances ** 0.5
    '''
    数字：4 3 5 2
    下标：0 1 2 3
    argsort：3 1 0 2 ，即sortedDistIndices存的是3 1 0 2，代表原数组中下标位3的数字最小
    所以sortedDistIndices[0] = 3  代表原数组的2 ->下标3对应的标签找分类
        sortedDistIndices[1] = 1  代表原数组的3 ->下标1对应的标签找分类
    '''
    sortedDistIndices = oushi_distance.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    
    maxCount = 0  
    #step3.在字典中找最大的分类  
    for key,value in classCount.items():  
        if value>maxCount:  
            maxCount = value  
            maxIndex = key  
    return maxIndex  

    

#training 训练集的每个数字都是一个32*32的二维矩阵
def img2vector(filename):
    returnVect = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    trainingFileList = listdir('HandTrainingData')
    mTrain = len(trainingFileList)
    #生成一个m*1024大小的二维数组
    trainingMat = np.zeros((mTrain,1024))

    #训练集文件名字1_1.txt,7_8.txt,第一个数字代表这个txt文件存的数字，第二个数字是个数
    for i in range(mTrain):
        fileNameStr = trainingFileList[i]        #1_1.txt
        fileStr     = fileNameStr.split('.')[0]  #1.1
        classNumStr = int(fileStr.split('_')[0]) #1
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('HandTrainingData/%s'%fileNameStr)
    
    testFileList = listdir('HandTestData')
    errorCount   = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr     = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('HandTestData/%s'%fileNameStr)
        #vectorUnderTest是一个1*1024的vector，即一条测试数据
        classifierResult = classifyKnn(vectorUnderTest,trainingMat,hwLabels,3)
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): errorCount += 1.0
    print ("\nthe total number of errors is: %d" % errorCount)
    print ("\nthe total error rate is: %f" % (errorCount/float(mTest)))

if __name__ == '__main__':
    handwritingClassTest()
