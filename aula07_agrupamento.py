# Databricks notebook source
# DBTITLE 1,GROUP BY
# MAGIC %md Semelhante à cláusula SQL GROUP BY, a função PySpark groupBy () é usada para coletar os dados idênticos em grupos no DataFrame e executar funções de agregação nos dados agrupados.<br> Documentação Oficial:
# MAGIC https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql.html#grouping <br>
# MAGIC https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.groupBy.html#pyspark.sql.DataFrame.groupBy

# COMMAND ----------

# DBTITLE 1,GroupedData
# MAGIC %md Quando executamos groupBy () no Dataframe, ele retorna o objeto GroupedData que contém as funções agregadas abaixo:<br>
# MAGIC mean() - Retorna a média dos valores de cada grupo. <br>
# MAGIC max() - Retorna o máximo de valores para cada grupo. <br>
# MAGIC min() - Retorna o mínimo de valores para cada grupo. <br>
# MAGIC sum() - Retorna o total de valores para cada grupo. <br>
# MAGIC avg() - Retorna a média dos valores de cada grupo. <br>
# MAGIC agg() - Calcular mais de um valor agregado por vez

# COMMAND ----------

# DBTITLE 1,Preparando dados e criando o DataFrame
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

df.createTempView("tbl_teste")

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT SUM(salary) as SALARIO, to_json(collect_list(map("DEPRTAMENTOS",dep_name,"PESSOAS",emp_name))) AS DEPARTAMENTOS  FROM tbl_teste GROUP BY state

# COMMAND ----------

# DBTITLE 1,Sum
df.groupBy(F.col("dep_name")).sum("salary").show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Count
df.groupBy(F.col("dep_name")).count().show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Min
df.groupBy(F.col("dep_name")).min("salary").show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Max
df.groupBy(F.col("dep_name")).max("salary").show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Mean
df.groupBy(F.col("dep_name")).mean("salary").show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Avg
df.groupBy(F.col("dep_name")).avg("salary").show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Groupyby com multiplas colunas
df.groupBy(F.col("dep_name"),F.col("state")).sum("salary","bonus").show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Agg
df.groupBy(F.col("dep_name")) \
.agg(F.sum("salary").alias("Sum_salary"), \
    F.avg("salary").alias("Avg_salary"), \
    F.sum("bonus").alias("Sum_bonus"), \
    F.max("bonus").alias("Max_bonus"), \
    F.min("bonus").alias("Min_bonus")    
    ).show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Filtrando DataFrame Agrupado
df.groupBy(F.col("dep_name")) \
.agg(F.sum("salary").alias("Sum_salary"), \
    F.avg("salary").alias("Avg_salary"), \
    F.sum("bonus").alias("Sum_bonus"), \
    F.max("bonus").alias("Max_bonus"), \
    F.min("bonus").alias("Min_bonus")    
    ).where(F.col("Sum_salary") >= 79000 ).show(truncate=False)

# COMMAND ----------

