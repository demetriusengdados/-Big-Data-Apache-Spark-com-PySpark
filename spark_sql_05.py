# Databricks notebook source
import pyspark.sql.functions as F

data = [
    (1, "Anderson", 10000),
    (2, "Kenedy", 20000),
    (3, "Billy", 23000),
    (4, "Andy", 23000),
    (5, "Mary", 24000),
    (6, "Eduardo", 19000),
    (7, "Mendes", 15000),
    (8, "Keyth", 18000),
    (9, "Truman", 21000),
]

schema = ["id", "name", "salary"]
spark.createDataFrame(data=data, schema=schema).createOrReplaceTempView("temp_tbl_1")

data = [
    (1, "Delhi", "India"),
    (2, "Tamil nadu", "India"),
    (3, "London", "UK"),
    (4, "Sydney", "Australia"),
    (8, "New York", "USA"),
    (9, "California", "USA"),
    (10, "New Jersey", "USA"),
    (11, "Texas", "USA"),
    (12, "Chicago", "USA"),
]

schema = ["id", "place", "country"]
spark.createDataFrame(data=data, schema=schema).createOrReplaceTempView("temp_tbl_2")



# COMMAND ----------

# DBTITLE 1,SQL Inner Join
# MAGIC %sql
# MAGIC SELECT T1.*, T2.* FROM temp_tbl_1 T1 INNER JOIN temp_tbl_2 T2 ON T1.id = T2.id

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT name FROM temp_tbl_1 INNER JOIN temp_tbl_2 ON temp_tbl_1.id = temp_tbl_2.id

# COMMAND ----------

# DBTITLE 1,SQL Left Outer Join 
# MAGIC %sql
# MAGIC SELECT T1.*, T2.* FROM temp_tbl_1 T1 LEFT OUTER JOIN temp_tbl_2 T2 ON T1.id = T2.id

# COMMAND ----------

# DBTITLE 1,SQL Right Outer Join
# MAGIC %sql
# MAGIC SELECT T1.*, T2.* FROM temp_tbl_1 T1 RIGHT OUTER JOIN temp_tbl_2 T2 ON T1.id = T2.id