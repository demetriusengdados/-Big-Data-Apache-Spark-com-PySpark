# Databricks notebook source
#from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

if __name__ == "__main__":
    """
    conf = SparkConf() \
    .setMaster("local") \
    .setAppName("estudando-dataframes")
    spark = SparkSession.builder.config(conf = conf).getOrCreate()

    """
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

    new_df = (df.withColumn("soma_novos_e_acumulados",F.col("casosNovos")+F.col("casosAcumulados")).
              withColumn("coluna_personalizada",F.lit("O Valor da Coluna"))
              )
    new_df_cast = new_df.selectExpr("cast(casosNovos as string)")
    new_df_cast.printSchema()
    #new_df_cast.show(10)