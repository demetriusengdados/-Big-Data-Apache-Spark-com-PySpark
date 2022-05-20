# Databricks notebook source
# DBTITLE 1,Funções utilitárias
# MAGIC %md
# MAGIC 
# MAGIC %fs ls "FileStore/tables/json"
# MAGIC <br>
# MAGIC dbutils.fs.ls("FileStore/tables/json")

# COMMAND ----------

# DBTITLE 1,Documentação
# MAGIC %md
# MAGIC LINK: https://hyukjin-spark.readthedocs.io/en/latest/reference/api/pyspark.sql.functions.pandas_udf.html

# COMMAND ----------

import pyspark.sql.functions as F  

# COMMAND ----------


df = spark.read.option("inferSchema", True).json("/FileStore/tables/json/data.json")
new_df = df.limit(500)

# COMMAND ----------

new_df.write.mode("overwrite").parquet("/FileStore/tables/parquet/data.parquet")

# COMMAND ----------

parquet_df = spark.read.parquet("/FileStore/tables/parquet/data.parquet")

# COMMAND ----------

display(parquet_df)

# COMMAND ----------

def upperCase(string):
  return string.upper()

def change_value_date(date):
  if date in ("20160817"):
    return "Achou"
  else:
    return "Não achou"
  
  

# COMMAND ----------

upperCaseUDF = F.udf(lambda x: upperCase(x), StringType())
change_value_date_UDF = F.udf(lambda x: change_value_date(x), StringType())

# COMMAND ----------

# DBTITLE 1,Registrando UDF
spark.udf.register("upperCaseUDF", upperCase, StringType())

# COMMAND ----------

# DBTITLE 1,Criando uma tabela temporária
parquet_df.createTempView("tbl_parquet")

# COMMAND ----------

display(parquet_df.withColumn("channelGrouping", upperCaseUDF(F.col("channelGrouping"))).withColumn("date",change_value_date_UDF(F.col("date"))))

# COMMAND ----------

spark.sql("SELECT * FROM tbl_parquet")

# COMMAND ----------

df01 = spark.table("tbl_parquet")

# COMMAND ----------

display(df01)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT  upperCaseUDF("channelGrouping") FROM tbl_parquet

# COMMAND ----------

import pandas as pd
from pyspark.sql.functions import pandas_udf

@pandas_udf("string")
def to_upper(s: pd.Series) -> pd.Series:
  return s.str.upper()

# COMMAND ----------

display(parquet_df.select(to_upper("channelGrouping")))

# COMMAND ----------

