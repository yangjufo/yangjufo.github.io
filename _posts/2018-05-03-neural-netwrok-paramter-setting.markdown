---
title: "机器学习之全连接层参数设置"
layout: post
date: 2018-05-03 22:33
image: /assets/images/markdown.jpg
headerImage: false
tag:
- 机器学习
category: blog
author: Jian Yang
description: 全连接层参数设置总结
# jemoji: '<img class="emoji" title=":ramen:" alt=":ramen:" src="https://assets.github.com/images/icons/emoji/unicode/1f35c.png" height="20" width="20" align="absmiddle">'
---

## 摘要:

几个常用参数设置对于全连接层学习效率/效果的影响

## 背景概要

最近在用神经网络（只有全连接层）学习数据库索引，调参的问题困扰了很久，在此总结各个参数（batch_size、learning_rate、 core_size、 layer_size等）对于学习过程的影响，以做参考。

学习的目标是一维的数据对应一维的输出，相当于key-value模型，本质是在学习一维数据集合的分布模型。

全部实验基于TensorFlow。

## 隐藏层层数和各层核数量

全连接层隐藏层的设置需要考虑到数据分布的情况，比如线性的分布，那么不需要隐藏层，即简单的一次函数就能得到比较好的结果；如果是比较复杂的分布，比如长尾分布或者指数分布，高度非线性，那么就需要比较复杂的隐藏层设置，比如2层，每层各16个核。

要避免不自觉的认为核数越多，模型越复杂得到的结果越好，一般来说，复杂的模型能够得到比较好的结果，但是相比于简单的模型，学习路径更加曲折，所花费的代价更大，因此越是大规模看上去复杂的数据集，越要尝试用简单的模型去解决，而且往往就可以解决。

## 学习率

学习率决定了权重矩阵和偏置矩阵更新的幅度，比如将学习率设为0.01，那么可能矩阵的变化是0.1->0.07->0.03；将学习率设置为0.001，矩阵的变化可能是0.1->0.095->0.087。简而言之，学习率越小，更新的幅度就越小，学习的速度也会慢。

学习率的选取对于比较容易陷入硬饱和（神经元死亡，不再更新）的激活函数（如Relu）很关键，如果学习率过大，学习速度很快，但同时容易陷入硬饱和，因为幅度过大，错过了最优解；如果学习率过小，学习速度过慢，相应的代价也会变高。

## 批大小

批的大小和学习率的影响有些相似，当把批的数量设置得比较大时，学习得会比较快，但是容易陷入局部最优解；把批的数量设置得比较小时，学习得速度变慢，但学习路径变得丰富，更优可能跳出局部解。个人认为，设置一个居中的批大小比较合适。

## 学习步数

学习的步数不必过长，可以和学习率、批大小结合在一起考虑，当需要精细调整时，可以将步数调整得大一些，反之小一些即可，避免不必要的浪费。
