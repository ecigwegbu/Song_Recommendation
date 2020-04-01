from pyspark.sql import SparkSession
from pyspark.sql.functions import desc


if __name__ == "__main__":

    spark = SparkSession \
        .builder \
        .appName("TagStream") \
        .master("local[2]") \
        .getOrCreate()

    tags = spark.read.json("data/tags.data")

    tags\
        .select("match.track.id") \
        .groupBy("id") \
        .count() \
        .orderBy(desc("count")) \
        .show(10)
