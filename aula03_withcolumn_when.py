# Databricks notebook source
#from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

if __name__ == "__main__":

    spark = (SparkSession.builder
        .master("local[3]")
        .appName("estudando-dataframes")
        .getOrCreate())

    df = (spark
          .read
          .format("csv")
          .option("header","true")
          .option("inferSchema","true")
          .option("delimiter",";")
          .load("csv/arquivo_geral.csv"))

    df.printSchema()

    df_status_casos_novos = (df.withColumn("Status",
                             F.when(F.col("casosNovos") > 0,
                             F.concat(df.casosNovos, F.lit(" casos novos"))).
                             otherwise("Sem casos novos")).
                             withColumn("Dia", F.substring(F.col("data"),9,2).cast("integer")).
                             withColumn("Mes", F.substring(F.col("data"), 6, 2).cast("integer")).
                             withColumn("Ano", F.substring(F.col("data"), 1, 4).cast("integer"))
                             )
    df_status_casos_novos.show(10)

    df_status_casos_novos.printSchema()