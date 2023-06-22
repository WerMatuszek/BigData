from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").appName("HelloWorld").getOrCreate()


def makeSparkSession():
    return spark
