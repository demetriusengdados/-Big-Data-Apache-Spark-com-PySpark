# Databricks notebook source
spark.sparkContext.parallelize(range(1,11)).filter(lambda x: x <= 5).collect()

# COMMAND ----------

spark.sparkContext.parallelize(range(1,11)).filter(lambda x: x > 5).collect()

# COMMAND ----------

spark.sparkContext.parallelize(range(1,11)).filter(lambda x: x > 5).filter(lambda x: x < 8).collect()

# COMMAND ----------

spark.sparkContext.parallelize(["Elton Jon Oliveira DataScience DataEngineer"]).flatMap(lambda x: x.split(" ")). \
map(lambda y: y.upper()). \
filter(lambda z: z in ["DATAENGINEER","ELTON"]). \
filter(lambda z: z == "ELTON").collect()


# COMMAND ----------

