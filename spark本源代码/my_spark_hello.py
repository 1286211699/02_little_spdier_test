from pyspark import SparkContext
from pyspark import SparkConf

# 创建Spark对应此应用程序的配置，必须要设置应用名称，必须要设置运行模式
# ，local[*]是我们本地测试用的模式，local[*]代表用所有可用的线程并行执行
# ，local等价于local[1]
conf = SparkConf().setAppName("yasaka").setMaster("local")
# 创建Spark上下文环境，接收的参数通常是SparkConf
sc = SparkContext(conf=conf)
# 此时这个list列表数据是在Python解释器中
data = ["i love xuruyun", "i love wangfei", "i love liangyongqi"]
# 把上面的list列表并行化变成了RDD(弹性分布式数据集)
# RDD就分布式存在在spark集群的内存中分布式存在啦！
rdd = sc.parallelize(data)
# flatMap = flat(扁平化，把集合中的元素拿出来) + Map
# 先执行map操作，再执行flat操作
words = rdd.flatMap(lambda sen: sen.split())
# map操作是对集合也就是RDD里面的每个元素进行操作
pairs = words.map(lambda word: (word, 1))
# reduceByKey = reduce(按照匿名函数逻辑把集合进行聚合运算) + groupByKey(按照键来进行分组)
# 先执行groupByKey，再执行reduce
result = pairs.reduceByKey(lambda a, b: a+b).collect()
# collect是把结果从spark端拉取回来到Python解释器中
print(result)
