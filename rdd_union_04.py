# Databricks notebook source
rdd_01 = spark.sparkContext.parallelize(range(1,100))
rdd_02 = spark.sparkContext.parallelize(range(200,300))

# COMMAND ----------

rdd_01.collect()

# COMMAND ----------

rdd_02.collect()

# COMMAND ----------

rdd_01.union(rdd_02).collect()

# COMMAND ----------

