# Databricks notebook source
spark.sparkContext.parallelize([("Elton",1),("Jon",2),("Antonni",3),("Clarice",4),("Monica",5)]).collect()

# COMMAND ----------

spark.sparkContext.parallelize([("Elton",1),("Jon",2),("Antonni",3),("Clarice",4),("Monica",5)]).sortBy(lambda x : -x[1]).collect()

# COMMAND ----------

spark.sparkContext.parallelize([("Elton",1),("Jon",2),("Antonni",3),("Clarice",4),("Monica",5)]).sortBy(lambda x : x[1]).collect()

# COMMAND ----------

spark.sparkContext.parallelize([("Elton",1),("Jon",2),("Antonni",3),("Clarice",4),("Monica",5)]).sortByKey().collect()

# COMMAND ----------

