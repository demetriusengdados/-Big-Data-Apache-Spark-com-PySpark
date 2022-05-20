# Databricks notebook source
# DBTITLE 1,JOIN
# MAGIC %md
# MAGIC O PySpark Join é usado para combinar dois DataFrames e, encadeando-os, você pode juntar vários DataFrames; <br>ele suporta todas as operações básicas de tipo de junção disponíveis no SQL tradicional, como INNER, LEFT OUTER, RIGHT OUTER, LEFT ANTI, LEFT SEMI, CROSS, SELF JOIN. 
# MAGIC 
# MAGIC Exemplos:<br>
# MAGIC 
# MAGIC inner ==> INNER JOIN SQL <br>
# MAGIC outer, full, fullouter, full_outer ==> FULL OUTER JOIN <br>
# MAGIC left, leftouter, left_outer  ==> LEFT JOIN <br>
# MAGIC right, rightouter, right_outer ==> RIGHT JOIN <br>
# MAGIC cross <br>
# MAGIC anti, leftanti, left_anti <br>
# MAGIC semi, leftsemi, left_semi <br>

# COMMAND ----------

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
df1 = spark.createDataFrame(data=data, schema=schema)
df1.printSchema()
df1.show(truncate=False)


# COMMAND ----------

import pyspark.sql.functions as F

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
df2 = spark.createDataFrame(data=data, schema=schema)
df2.printSchema()
df2.show(truncate=False)


# COMMAND ----------

# DBTITLE 1,Inner join
df_inner = df1.join(df2, on=['id'], how='inner')
df_inner.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Outer join
df_outer = df1.join(df2, on=['id'], how='outer')
df_outer.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Left join
df_left = df1.join(df2, on=['id'], how='left')
df_left.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Right join
df_right = df1.join(df2, on=['id'], how='right')
df_right.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Left Anti join
df_left_anti = df1.join(df2, on=['id'], how='left_anti')
df_left_anti.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Left Semi join 
df_left_semi = df1.join(df2, on=['id'], how='left_semi')
df_left_semi.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Full join
df_left_semi = df1.join(df2, on=['id'], how='full')
df_left_semi.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Anti join
df_anti = df1.join(df2, on=['id'], how='anti')
df_anti.show(truncate=False)