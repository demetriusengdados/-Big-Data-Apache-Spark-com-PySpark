# Databricks notebook source
from pyspark.sql.functions import input_file_name

(spark.read.option("delimiter",";").option("header", True).
 csv("/FileStore/tables/covid/arquivo_geral.csv").
 withColumn("filename",input_file_name()).
 createOrReplaceTempView("tbl_covid"))

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_covid

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT REGIAO, COUNT(ESTADO) AS COUNT_ESTADOS FROM tbl_covid GROUP BY REGIAO

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT REGIAO, COUNT(ESTADO) AS COUNT_ESTADOS FROM tbl_covid GROUP BY REGIAO HAVING COUNT_ESTADOS > 500

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT REGIAO, COUNT(ESTADO) AS COUNT_ESTADOS FROM tbl_covid GROUP BY REGIAO HAVING COUNT_ESTADOS < 500

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT REGIAO, COUNT(ESTADO) AS COUNT_ESTADOS FROM tbl_covid GROUP BY REGIAO HAVING COUNT_ESTADOS < 500 ORDER BY REGIAO DESC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT REGIAO, COUNT(ESTADO) AS COUNT_ESTADOS FROM tbl_covid GROUP BY REGIAO HAVING COUNT_ESTADOS < 500 ORDER BY REGIAO DESC LIMIT 2

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TEMPORARY VIEW tbl_covid_group AS
# MAGIC   SELECT REGIAO, COUNT(ESTADO) AS COUNT_ESTADOS FROM tbl_covid GROUP BY REGIAO

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_covid_group

# COMMAND ----------

spark.sql("SELECT * FROM tbl_covid_group").show(truncate=False)

# COMMAND ----------

