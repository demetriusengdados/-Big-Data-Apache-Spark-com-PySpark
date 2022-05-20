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
# MAGIC SELECT regiao, estado, casosNovos,
# MAGIC CASE
# MAGIC    WHEN casosNovos > 200 THEN 'Estado Médio'
# MAGIC    WHEN casosNovos >= 400 THEN 'Estado Crítico'
# MAGIC    WHEN casosNovos = 0 THEN 'Estado Seguro'
# MAGIC    ELSE 'Nenhuma das Alterativas'
# MAGIC END AS verificacao_casos
# MAGIC FROM temp_tbl_covid
# MAGIC ORDER BY casosNovos

# COMMAND ----------

