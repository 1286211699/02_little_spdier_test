#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: my_spark_textFile.py

from pyspark import SparkContext
from pyspark import SparkConf

__author__ = 'yasaka'

conf = SparkConf().setAppName("yasaka").setMaster("local[*]")
sc = SparkContext(conf=conf)

rdd = sc.textFile("../data/LICENSE-heapq.txt", minPartitions=4)
result = rdd.flatMap(lambda line: line.split()).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)
# sorted_result = result.sortBy(lambda el: el[1], ascending=False).collect()
sorted_result = result.map(lambda pairs: (pairs[1], pairs[0])).sortByKey(ascending=False)\
    .map(lambda pairs: (pairs[1], pairs[0]))
# print(sorted_result)
sorted_result.saveAsTextFile("./result")





