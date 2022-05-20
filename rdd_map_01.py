# Databricks notebook source
spark.sparkContext.parallelize(range(1,100)).map(lambda x : x * 2).take(3)

# COMMAND ----------

