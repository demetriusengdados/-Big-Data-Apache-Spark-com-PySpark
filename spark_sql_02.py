# Databricks notebook source
from pyspark.sql.functions import input_file_name

(spark.read.option("delimiter",";").option("header", True).
 csv("/FileStore/tables/covid/arquivo_geral.csv").
 withColumn("filename",input_file_name()).
 createOrReplaceTempView("tbl_covid"))

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECt * FROM tbl_covid

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_covid WHERE estado like 'R%'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_covid WHERE estado like '%A'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_covid WHERE regiao = 'Norte' and (estado = 'AM' or estado = 'RO')

# COMMAND ----------

spark.sql("SELECT estado FROM tbl_covid").dropDuplicates().show(truncate=False)

# COMMAND ----------

spark.sql("SELECT estado FROM tbl_covid").distinct().show(truncate=False)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT DISTINCT estado FROM tbl_covid

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT estado FROM tbl_covid WHERE estado in ('RR','AC','RN')

# COMMAND ----------

