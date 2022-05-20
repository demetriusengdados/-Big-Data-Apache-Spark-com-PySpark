# Databricks notebook source
# DBTITLE 1,Documentação
# MAGIC %md
# MAGIC Link : https://spark.apache.org/docs/3.0.2/api/sql/

# COMMAND ----------

# MAGIC %fs ls "FileStore/tables/covid/"

# COMMAND ----------

from pyspark.sql.functions import input_file_name

(spark.read.option("delimiter",";").option("header", True).
 csv("/FileStore/tables/covid/arquivo_geral.csv").
 withColumn("filename",input_file_name()).
 createOrReplaceTempView("tbl_covid"))

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_covid

# COMMAND ----------

spark.sql("show tables").show(truncate=False)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_covid WHERE REGIAO = 'Norte' OR ESTADO = 'AM'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) as count_norte FROM tbl_covid WHERE REGIAO = 'Norte'

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE tbl_covid

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_covid WHERE month(data) > 2 and month(data) < 4

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_covid WHERE year(data) > 2020

# COMMAND ----------

