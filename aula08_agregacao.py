# Databricks notebook source
# DBTITLE 1,Built-in standard Aggregate functions
# MAGIC %md O PySpark  built-in standard Aggregate functions definidas na API DataFrame, que são úteis quando precisamos fazer operações agregadas em colunas DataFrame. As funções agregadas operam em um grupo de linhas e calculam um único valor de retorno para cada grupo.
# MAGIC <br>
# MAGIC Documentação: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql.html#grouping

# COMMAND ----------

# DBTITLE 1,DataFrame que será utilizado
import pyspark.sql.functions as F
data = [("Anderson","Sales","NY",90000,34,10000),
    ("Kenedy","Sales","CA",86000,56,20000),
    ("Billy","Sales","NY",81000,30,23000),
    ("Andy","Finance","CA",90000,24,23000),
    ("Mary","Finance","NY",99000,40,24000),
    ("Eduardo","Finance","NY",83000,36,19000),
    ("Mendes","Finance","CA",79000,53,15000),
    ("Keyth","Marketing","CA",80000,25,18000),
    ("Truman","Marketing","NY",91000,50,21000)
  ]

schema = ["emp_name","dep_name","state","salary","age","bonus"]
df = spark.createDataFrame(data=data, schema = schema)
df.printSchema()
df.show(truncate=False)

# COMMAND ----------

from pyspark.sql.functions import monotonically_increasing_id

df = df.withColumn("id", monotonically_increasing_id())
display(df)


# COMMAND ----------

# DBTITLE 1,approx_count_distinct Aggregate Function
approx = df.select(F.approx_count_distinct("salary")).collect()[0][0]
print(f"approx_count_distinct: {approx}")

# COMMAND ----------

# DBTITLE 1,avg (average) Aggregate Function
avg = df.select(F.avg("salary")).collect()[0][0]
print(f"avg: {avg}")

# COMMAND ----------

# DBTITLE 1,collect_list Aggregate Function
df.select(F.collect_list("salary")).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,collect_set Aggregate Function
df.select(F.collect_set("salary")).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,countDistinct Aggregate Function
df2 = df.select(F.countDistinct(F.col("dep_name"), F.col("salary")))
df2.show(truncate=False)


# COMMAND ----------

print(f"Contagem distinta de departamentos e salários: {df2.collect()[0][0]}")

# COMMAND ----------

# DBTITLE 1,count function
salary = df.select(F.count("salary")).collect()[0]
print(f"Count:{salary}")

# COMMAND ----------

# DBTITLE 1,first function
df.select(F.first("salary")).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Max
df.select(F.max(F.col("salary"))).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Min
df.select(F.min(F.col("salary"))).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Sum
df.select(F.sum(F.col("salary"))).show(truncate=False)