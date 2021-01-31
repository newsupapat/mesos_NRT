import os
from pyspark.sql import DataFrame as sparkDF
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType, ArrayType
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql.types import *

conf = SparkConf()
sc = SparkContext(conf=conf)
spark = SparkSession.builder.getOrCreate()

data = [('James','','Smith','1991-04-01','M',3000),
  ('Michael','Rose','','2000-05-19','M',4000),
  ('Robert','','Williams','1978-09-05','M',4000),
  ('Maria','Anne','Jones','1967-12-01','F',4000),
  ('Jen','Mary','Brown','1980-02-17','F',-1)
]
columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
print("Data set")
print(df.show())
spark.stop()
