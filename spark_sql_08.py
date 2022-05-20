# Databricks notebook source
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
spark.createDataFrame(data=data, schema = schema).createOrReplaceTempView("tbl_window")


# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM tbl_window

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT name, dep_name, salary, RANK() OVER (PARTITION BY dep_name ORDER BY salary) AS rank FROM tbl_window

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT name, dep_name, salary, DENSE_RANK() OVER (PARTITION BY dep_name ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS rank FROM tbl_window

# COMMAND ----------

