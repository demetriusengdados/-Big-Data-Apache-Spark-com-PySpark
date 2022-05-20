# Databricks notebook source
# MAGIC %md As Windows Functions do PySpark operam em um grupo de linhas e retornam um único valor para cada uma delas. O PySpark SQL oferece suporte a três tipos de window function:
# MAGIC <br>
# MAGIC ranking functions<br>
# MAGIC analytic functions <br>
# MAGIC aggregate functions <br>
# MAGIC 
# MAGIC Documentação: https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.Window.html?highlight=window#pyspark.sql.Window

# COMMAND ----------

import pyspark.sql.functions as F
from pyspark.sql.window import Window

data = [("Anderson","Sales","NY",90000),
    ("Kenedy","Sales","CA",86000),
    ("Kenny","Sales","CA",86000),
    ("Billy","Sales","NY",81000),
    ("Andy","Finance","CA",90000),
    ("Mary","Finance","NY",99000),
    ("Eduardo","Finance","NY",83000),
    ("Mendes","Finance","CA",79000),
    ("Keyth","Marketing","CA",80000),
    ("Truman","Marketing","NY",91000)
  ]

schema = ["name","dep_name","state","salary"]
df = spark.createDataFrame(data=data, schema = schema)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,row_number Window Function
w0  = Window.partitionBy(F.col("dep_name")).orderBy(F.col("salary"))
df.withColumn("row_number",F.row_number().over(w0)).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,rank Window Function
df.withColumn("rank",F.rank().over(w0)).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,dense_rank Window Function
df.withColumn("dense_rank",F.dense_rank().over(w0)).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,percent_rank Window Function
df.withColumn("percent_rank",F.percent_rank().over(w0)).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,ntile Window Function
df.withColumn("ntile",F.ntile(2).over(w0)).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,cume_dist Window Function
df.withColumn("cume_dist",F.cume_dist().over(w0)).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,lag Window Function
df.withColumn("lag",F.lag("salary",1).over(w0)).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,lead Window Function
df.withColumn("lead",F.lead("salary",2).over(w0)).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Window Aggregate Functions
w01 = Window.partitionBy(F.col("dep_name")).orderBy(F.col("salary"))

df.withColumn("row",F.row_number().over(w01)) \
  .withColumn("avg", F.avg(F.col("salary")).over(w01)) \
  .withColumn("sum", F.sum(F.col("salary")).over(w01)) \
  .withColumn("min", F.min(F.col("salary")).over(w01)) \
  .withColumn("max", F.max(F.col("salary")).over(w01)) \
  .where(F.col("row")==1).select("dep_name","avg","sum","min","max") \
  .show(truncate=False)

# COMMAND ----------

