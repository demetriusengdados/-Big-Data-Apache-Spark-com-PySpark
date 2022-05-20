# Databricks notebook source
# MAGIC %sql
# MAGIC SHOW TABLES

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS temp_tbl_covid;
# MAGIC 
# MAGIC CREATE TABLE temp_tbl_covid USING CSV
# MAGIC OPTIONS (path "/FileStore/tables/covid/arquivo_geral.csv", header="true", inferSchema="true", delimiter = ";")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM temp_tbl_covid

# COMMAND ----------

