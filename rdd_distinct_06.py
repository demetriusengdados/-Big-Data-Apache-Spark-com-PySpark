# Databricks notebook source
spark.sparkContext.parallelize([10,10,3,4,5,5,9,9,4,4]).distinct().collect()

# COMMAND ----------

spark.sparkContext.parallelize(["Elton","Elton","Jon","Data","Engenheiro"]).distinct().collect()

# COMMAND ----------

