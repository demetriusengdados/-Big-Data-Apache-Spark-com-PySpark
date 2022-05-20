# Databricks notebook source
spark.sparkContext.parallelize(["Elton Oliveira Engenheiro de Dados","Jon Oliveira Engenheiro de Dados","Antonni Eduardo","Clarice Lima"]). \
flatMap(lambda x : x.split(" ")).map(lambda y : y.upper()).collect()

# COMMAND ----------

