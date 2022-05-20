# Databricks notebook source
spark.sparkContext.parallelize(range(1,100)).collect()

# COMMAND ----------

spark.sparkContext.parallelize(range(1,100)).count()

# COMMAND ----------

spark.sparkContext.parallelize(range(1,100)).take(10)

# COMMAND ----------

spark.sparkContext.parallelize(range(1,100)).top(2)

# COMMAND ----------

spark.sparkContext.parallelize(range(1,100)).takeOrdered(5, key = lambda x: x)

# COMMAND ----------

spark.sparkContext.parallelize(range(1,100)).first()

# COMMAND ----------

spark.sparkContext.parallelize(range(1,100)).reduce( lambda a, b: a + b )