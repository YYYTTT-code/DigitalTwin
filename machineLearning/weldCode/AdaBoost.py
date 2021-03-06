#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/8 15:25
# @Author  : GXl
# @File    : 7.4.2.py
# @Software: win10 Tensorflow1.13.1 python3.5.6


import numpy as np
import matplotlib.pyplot as plt

"""
Parameters:
    无
Returns:
    dataMat - 数据矩阵
    classLabels - 数据标签
"""


# # 创建单层决策树的数据集
# def loadSimpData():
#     datMat = np.matrix([[1., 2.1],
#                         [1.5, 1.6],
#                         [1.3, 1.],
#                         [1., 1.],
#                         [2., 1.]])
#     classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
#     return datMat, classLabels

# 加载焊接数据
def loadDataSet(fileName,xNum=2):
    """
    Parameters:
        fileName - 文件名
        xNum 用于训练的参数
    Returns:
        xArr - x数据集
        yArr - y数据集
    """
    xArr = []
    yArr = []
    featureName=open(fileName,encoding='utf-8').readline().split('\t')
    numFeat = len(featureName)
    fr = open(fileName)
    fr.readline()
    for line in fr.readlines():
        xLine = []
        yLine=[]
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            if i<xNum:
                xLine.append(float(curLine[i]))
            else:
                yLine.append(float(curLine[i]))
        xArr.append(xLine)
        yArr.append(yLine)
    print(featureName)
    return xArr, yArr
"""
Parameters:
    dataMat - 数据矩阵
    labelMat - 数据标签
Returns:
    无
"""


# 数据可视化
def showDataSet(dataMat, labelMat):
    data_plus = []  # 正样本
    data_minus = []  # 负样本
    for i in range(len(dataMat)):
        if labelMat[i] > 0:
            data_plus.append(dataMat[i])
        else:
            data_minus.append(dataMat[i])
    data_plus_np = np.array(data_plus)  # 转换为numpy矩阵
    data_minus_np = np.array(data_minus)  # 转换为numpy矩阵
    plt.scatter(np.transpose(data_plus_np)[0], np.transpose(data_plus_np)[1])  # 正样本散点图
    plt.scatter(np.transpose(data_minus_np)[0], np.transpose(data_minus_np)[1])  # 负样本散点图
    plt.show()


"""
Parameters:
    dataMatrix - 数据矩阵
    dimen - 第dimen列，也就是第几个特征
    threshVal - 阈值
    threshIneq - 标志
Returns:
    retArray - 分类结果
"""

# 这里原代码写错了，把阈值改为自己实际分类的值，并且跟大于、小于阈值相对应
# 单层决策树分类函数
def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = np.ones((np.shape(dataMatrix)[0], 1))  # 初始化retArray为1
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = 0.0  # 如果小于阈值,则赋值为0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = 1  # 如果大于阈值,则赋值为1
    return retArray


"""
Parameters:
    dataArr - 数据矩阵
    classLabels - 数据标签
    D - 样本权重
Returns:
    bestStump - 最佳单层决策树信息
    minError - 最小误差
    bestClasEst - 最佳的分类结果
"""


# 找到数据集上最佳的单层决策树
def buildStump(dataArr, classLabels, D):
    dataMatrix = np.mat(dataArr)
    labelMat = np.mat(classLabels).T
    m, n = np.shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClasEst = np.mat(np.zeros((m, 1)))
    minError = float('inf')  # 最小误差初始化为正无穷大
    for i in range(n):  # 遍历所有特征
        rangeMin = dataMatrix[:, i].min()
        rangeMax = dataMatrix[:, i].max()  # 找到特征中最小的值和最大值
        stepSize = (rangeMax - rangeMin) / numSteps  # 计算步长
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:  # 大于和小于的情况，均遍历。lt:less than，gt:greater than
                threshVal = (rangeMin + float(j) * stepSize)  # 计算阈值
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)  # 计算分类结果
                errArr = np.mat(np.ones((m, 1)))  # 初始化误差矩阵
                errArr[predictedVals == labelMat] = 0  # 分类正确的,赋值为0
                weightedError = D.T * errArr  # 计算误差
                # print("split: dim %d, thresh %.2f, thresh ineqal: %s, the weighted error is %.3f" % (i, threshVal, inequal, weightedError))
                if weightedError < minError:  # 找到误差最小的分类方式
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClasEst


"""
Parameters:
    dataArr - 数据矩阵
    classLabels - 数据标签
    numIt - 最大迭代次数
Returns:
    weakClassArr - 训练好的分类器
    aggClassEst - 类别估计累计值
"""


# 使用AdaBoost算法提升弱分类器性能
def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    weakClassArr = []
    m = np.shape(dataArr)[0]
    D = np.mat(np.ones((m, 1)) / m)  # 初始化权重
    aggClassEst = np.mat(np.zeros((m, 1)))
    for i in range(numIt):
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)  # 构建单层决策树
        # print("D:",D.T)
        alpha = float(0.5 * np.log((1.0 - error) / max(error, 1e-16)))  # 计算弱学习算法权重alpha,使error不等于0,因为分母不能为0
        bestStump['alpha'] = alpha  # 存储弱学习算法权重
        weakClassArr.append(bestStump)  # 存储单层决策树
        # print("classEst: ", classEst.T)
        expon = np.multiply(-1 * alpha * np.mat(classLabels).T, classEst)  # 计算e的指数项
        D = np.multiply(D, np.exp(expon))
        D = D / D.sum()  # 根据样本权重公式，更新样本权重
        # 计算AdaBoost误差，当误差为0的时候，退出循环
        aggClassEst += alpha * classEst  # 计算类别估计累计值
        # print("aggClassEst: ", aggClassEst.T)
        aggErrors = np.multiply(np.sign(aggClassEst) != np.mat(classLabels).T, np.ones((m, 1)))  # 计算误差
        errorRate = aggErrors.sum() / m
        # print("total error: ", errorRate)
        if errorRate == 0.0: break  # 误差为0，退出循环
    return weakClassArr, aggClassEst


"""
Parameters:
    datToClass - 待分类样例
    classifierArr - 训练好的分类器
Returns:
    分类结果
"""


# AdaBoost分类函数
def adaClassify(datToClass, classifierArr):
    dataMatrix = np.mat(datToClass)
    m = np.shape(dataMatrix)[0]
    aggClassEst = np.mat(np.zeros((m, 1)))
    for i in range(len(classifierArr)):  # 遍历所有分类器，进行分类
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'], classifierArr[i]['thresh'],
                                 classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha'] * classEst
        print(aggClassEst)
    return np.sign(aggClassEst)


if __name__ == '__main__':
    dataArr, yArr = loadDataSet('../welding.txt',2)
    dataArr=np.mat(dataArr)
    '''选择yArr的第一项作为目标特征，这里是焊接方法，0为埋弧焊，1为二保焊'''
    classLabels=np.array(yArr)[:,0].reshape(1,-1)
    weakClassArr, aggClassEst = adaBoostTrainDS(dataArr, classLabels)
    print(type(dataArr))
    print(classLabels)
    print(weakClassArr)
    '''测试数据，共两个，第一个为15mm厚、1mm宽，输出为0，正确'''
    print(adaClassify([[15, 1], [8, 5]], weakClassArr))