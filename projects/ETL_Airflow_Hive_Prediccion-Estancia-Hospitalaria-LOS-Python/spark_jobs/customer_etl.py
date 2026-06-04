from pyspark.sql import SparkSession
from pyspark.sql.functions import trim, upper

spark = (
    SparkSession.builder
    .appName("Customer ETL")
    .enableHiveSupport()
    .getOrCreate()
)

df = spark.read.csv(
    "hdfs:///user/hdoop/hospital/input/hospital_covid_data.csv",
    header=True,
    inferSchema=True
)

clean_df = (
    df.dropDuplicates()
      .na.drop()
      .withColumn("customer_name", trim(df.customer_name))
      .withColumn("country", upper(df.country))
)

clean_df.write.mode("overwrite").saveAsTable(
    "retail.customers"
)

spark.stop()
