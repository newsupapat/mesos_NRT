
import os
from pyspark.sql import DataFrame as sparkDF
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, ArrayType
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql.types import *

NUM_SAMPLES=10000
conf = SparkConf()
sc = SparkContext(conf=conf)
def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1

count = sc.parallelize(range(0, NUM_SAMPLES)) \
             .filter(inside).count()
print("Pi is roughly %f" % (4.0 * count / NUM_SAMPLES))