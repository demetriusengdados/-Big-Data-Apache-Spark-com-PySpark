# Databricks notebook source
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS temp_tbl_covid;
# MAGIC 
# MAGIC CREATE TABLE temp_tbl_covid USING CSV
# MAGIC OPTIONS (path "/FileStore/tables/covid/arquivo_geral.csv", header="true", inferSchema="true", delimiter = ";")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM temp_tbl_covid

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT regiao, sum(casosNovos) FROM temp_tbl_covid GROUP BY 1 ORDER BY 1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT regiao, sum(casosNovos) AS SOMA, max(casosNovos) AS MAXIMO_CASOS_NOVOS,  min(casosNovos) AS MINIMO_CASOS_NOVOS  FROM temp_tbl_covid GROUP BY 1 ORDER BY 1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT regiao, sum(casosNovos) AS SOMA, max(casosNovos) AS MAXIMO_CASOS_NOVOS,  min(casosNovos) AS MINIMO_CASOS_NOVOS, avg(casosNovos) AS MEDIA_CASOS_NOVOS  FROM temp_tbl_covid GROUP BY 1 ORDER BY 1

# COMMAND ----------

