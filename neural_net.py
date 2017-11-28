# -*- coding: utf-8 -*-
"""
Created on Mon Oct 09 22:10:52 2017

@author: Jerry
"""

from numpy import exp,array,random,dot
train_set_inputs=array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
train_set_outputs=array([[0,1,1,0]]).T
random.seed(1)   #保证每次的随机数都是一样的
synaptic_weights=2*random.random((3,1))-1    # 为3*1矩阵随机赋值，原本是0~1，乘2后变成0~2，减1后变成-1~1
for i in xrange(10000):
    output=1/(1+exp(-(dot(train_set_inputs,synaptic_weights))))
    synaptic_weights+=dot(train_set_inputs.T,(train_set_outputs-output)*output*(1-output))
print 1/(1+exp(-(dot(array([1,0,0]),synaptic_weights))))