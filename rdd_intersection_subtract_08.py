# Databricks notebook source
rdd01 = spark.sparkContext.parallelize(range(1,100))
rdd02 = spark.sparkContext.parallelize(range(50,100))

# COMMAND ----------

rdd01.intersection(rdd02).collect()

# COMMAND ----------

rdd01 = spark.sparkContext.parallelize(["Elton","Jon","Clarice","Antonni"])
rdd02 = spark.sparkContext.parallelize(["Clarice","Antonni","Brasil","Engenheiro","Jon"])

# COMMAND ----------

rdd01.intersection(rdd02).collect()

# COMMAND ----------

rdd01.subtract(rdd02).collect()

# COMMAND ----------

