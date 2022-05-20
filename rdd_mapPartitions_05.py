# Databricks notebook source
spark.sparkContext.parallelize(range(1,100,5)).mapPartitions(lambda iterElement: [ x * 5 for x in iterElement] ).filter(lambda y: y < 100).collect()

# COMMAND ----------

