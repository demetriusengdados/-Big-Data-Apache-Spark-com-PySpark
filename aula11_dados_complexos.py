# Databricks notebook source
# DBTITLE 1,Documentação de funções
# MAGIC %md
# MAGIC Consulta: http://spark.apache.org/docs/3.1.1/api/python/reference/pyspark.sql.html#functions

# COMMAND ----------

# DBTITLE 1,Complex Types
import pyspark.sql.functions as F
from pyspark.sql.types import ArrayType, DoubleType, IntegerType, LongType, StringType, StructType, StructField, BooleanType, MapType
from pyspark.sql import Row

# COMMAND ----------

# DBTITLE 1,Criação do DataFrame para o exemplo
data = [Row("Kenny","",10,[50,90,80],{"status":"Active"}), 
        Row("Elis","Robert",20,[10,56,43,20],{"status":"Inactive"}), 
        Row("Myck","Mendes",30,[18,50,32],{"status":"Active"}), 
        Row("Edson","Eliot",40,[60,87,3],{"status":"Active"}) 
      ]

rdd = spark.sparkContext.parallelize(data)


# COMMAND ----------

# DBTITLE 1,Criação do Esquema
scheme = StructType([
         StructField('firstname', StringType(), True),
         StructField('middlename', StringType(), True),
         StructField('age', IntegerType(), True),
         StructField("points", ArrayType(StringType()), True),
         StructField("user_state", MapType(StringType(),StringType()), True)        
         ])

# COMMAND ----------

# DBTITLE 1,Conversão de RDD para DataFrame
df = rdd.toDF(schema=scheme)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# DBTITLE 1,Display do DataFrame
display(df)

# COMMAND ----------

df.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Criação de uma nova coluna e explode em uma coluna com o valor array
df02 = (df.withColumn("point", F.explode("points"))
  .select("firstname","point","user_state.status")        
)

display(df02)

# COMMAND ----------

# DBTITLE 1,Filtro por valores de uma coluna array e criação de uma coluna com o segundo valor do array
df03 = (df.filter(F.array_contains(F.col("points"), "50")).withColumn("get_point", F.element_at(F.col("points"), 2)))      
display(df03)

# COMMAND ----------

# DBTITLE 1,Criação de uma coluna com o primeiro valor do array
df04 = df.withColumn("get_point", F.element_at(F.col("points"), 1))
display(df04)

# COMMAND ----------

# DBTITLE 1,Agrupamento por status e agregação por pontos
df05 = (df04.groupBy("user_state.status")
  .agg(F.collect_set("get_point").alias("Points"))
)
display(df05)

# COMMAND ----------

# DBTITLE 1,Renomear coluna
df05 = df05.withColumnRenamed("Points","New_Points")

# COMMAND ----------

df05.show(truncate=False)

# COMMAND ----------

