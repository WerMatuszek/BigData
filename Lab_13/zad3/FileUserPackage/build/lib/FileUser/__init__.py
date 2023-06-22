from SparkSession import makeSparkSession
spark = makeSparkSession()


def FileReadJson(path, multi="false"):
    df = spark.read.format('json') \
        .option("multiline", multi) \
        .load(path)
    return df


def FileReadCSV(path, schema="false", header="true", deli=","):
    df = spark.read.format("csv") \
        .option("inferSchema", schema) \
        .option("header", header) \
        .option("sep", deli) \
        .load(path)
    return df


def FileSaveCSV(df, path, header="true", deli=","):
    df.write.format("csv") \
        .option("header", header) \
        .option("sep", deli) \
        .save(path)


def FileSaveJson(df, path):
    df.write.format("json") \
        .save(path)


def HighestFive(df, sortCol):
    df2 = df \
        .sort(sortCol, ascending=False) \
        .limit(5)
    return df2
