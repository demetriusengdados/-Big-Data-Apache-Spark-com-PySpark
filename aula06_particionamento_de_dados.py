# Databricks notebook source
# DBTITLE 1,Partições no Spark
# MAGIC %md Digamos que seus dados estejam em HDFS (Hadoop Distributed File System, que é distribuído entre muitos nós do cluster) ou no Amazon S3 (Simple Storage Service, que é um serviço de armazenamento (pode ser distribuído em muitos nós também). Seus dados físicos são distribuídos no armazenamento como partições que residem em HDFS, S3 ou armazenamento em nuvem. Como seus dados físicos são distribuídos como partições no cluster físico, o Spark trata cada um partição como uma abstração de dados lógicos de alto nível (como RDDs e DataFrames) na memória (e no disco se não houver memória suficiente). O cluster Spark otimizará o acesso à partição e lerá a partição mais próxima a ele na rede.

# COMMAND ----------

# DBTITLE 1, Qual é o objetivo principal do particionamento de dados? 
# MAGIC %md O principal objetivo do particionamento de dados é para o paralelismo eficiente (executar muitas tarefas ao mesmo tempo usando nós de cluster por meio de  Spark executors). Os executors do Spark são iniciados no início de um aplicativo Spark em coordenação com o Spark Cluster Manager. A divisão de dados (esquema distribuído) em partições permite que os executors do Spark processem apenas os dados próximos a eles.

# COMMAND ----------

# DBTITLE 1,Exemplo de particionamento
# MAGIC %md Por exemplo, se um RDD tem 10 bilhões de elementos, o Spark pode particioná-lo em 10.000 partes (também chamadas de partições - o número de partições é 10.000). Nesse caso, cada partição terá cerca de um milhão de elementos (10.000 x 1 milhão = 10 bilhões). Em seguida, essas partições podem ser enviadas para os nós do cluster para outras transofrmações, como mappers e reducers. O particionamento de dados permite que o Spark execute muitas transformações independentemente e ao mesmo tempo (maximizando o paralelismo).

# COMMAND ----------

import pyspark.sql.functions as F

# COMMAND ----------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# COMMAND ----------

rdd = sc.parallelize(numbers)

# COMMAND ----------

rdd.getNumPartitions()

# COMMAND ----------

# DBTITLE 1,Visualizar partições com seus valores
rdd.glom().collect()

# COMMAND ----------

# DBTITLE 1,Reduzindo o número de partições
rdd2 = rdd.coalesce(1)

# COMMAND ----------

rdd2.getNumPartitions()

# COMMAND ----------

rdd2.glom().collect()

# COMMAND ----------

# DBTITLE 1,Aumenta as partições mas faz um shuffle nos dados
rdd3 = rdd.repartition(4)

# COMMAND ----------

rdd3.getNumPartitions()

# COMMAND ----------

rdd3.glom().collect()

# COMMAND ----------

# DBTITLE 1,Criação de um Dataframe para exemplo de particionamento por coluna
df = spark.read.option("delimiter",";").option("header","true").csv("/FileStore/tables/covid/arquivo_geral.csv")

# COMMAND ----------

df.rdd.getNumPartitions()

# COMMAND ----------

df_partition = df.repartition(F.col("regiao"))

# COMMAND ----------

df_partition.rdd.glom().collect()

# COMMAND ----------

df_repartition2 = df_partition.repartition(200)

# COMMAND ----------

df_repartition2.rdd.glom().collect()

# COMMAND ----------

df_repartition2.rdd.getNumPartitions()

# COMMAND ----------

# DBTITLE 1,Função para imprimir detalhes do particionamento
def print_partitions(df):
    numPartitions = df.rdd.getNumPartitions()
    print("Total partitions: {}".format(numPartitions))   
    df.explain()
    parts = df.rdd.glom().collect()
    i = 0
    j = 0
    for p in parts:
        print("Partition {}:".format(i))
        for r in p:
            print("Row {}:{}".format(j, r))
            j = j+1
        i = i+1


# COMMAND ----------

print_partitions(df_repartition2)

# COMMAND ----------

df_repartition2.write.partitionBy("regiao","estado").mode("overwrite").csv("/FileStore/tables/covid/exemplo02/")

# COMMAND ----------

 df = (df.withColumn("Dia", F.substring(F.col("data"),9,2).cast("integer")).
          withColumn("Mes", F.substring(F.col("data"), 6, 2).cast("integer")).
          withColumn("Ano", F.substring(F.col("data"), 1, 4).cast("integer")))

# COMMAND ----------

df.write.partitionBy("mes","dia").mode("overwrite").csv("/FileStore/tables/covid/exemplo03/")