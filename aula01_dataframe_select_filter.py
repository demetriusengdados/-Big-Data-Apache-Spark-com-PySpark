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

    #df.show(10)

    #visualizar o schema das minhas colunas

    #df.printSchema()

    #df.select(F.col("regiao"),F.col("estado"),F.col("casosNovos")).filter(F.col("regiao") == "Norte").show(10)
    #df.select(F.col("regiao"), F.col("estado"), F.col("casosNovos")).filter(df.regiao == "Norte").show(10)
    #df.select(F.col("regiao"), F.col("estado"), F.col("casosNovos")).filter("regiao = 'Norte'").show(10)

    #filtro = F.col("regiao") == "Sul"
    #df.select(F.col("regiao"), F.col("estado"), F.col("casosNovos")).filter(filtro).show(10)
    #colunas_selecionadas = ["regiao", "casosNovos"]
    #df.select(*colunas_selecionadas).show(100)
    df.printSchema()
    #df.filter("regiao = 'Norte'").filter("estado = 'AM'").show(10)
    #df.filter("regiao = 'Norte' and estado = 'AM'").show(10)
    #df.filter((F.col("regiao") == 'Norte') | (F.col("estado") == 'AM')).show(10)
    #df.filter((F.col("regiao") == 'Norte') | (F.col("estado") == 'AM')).show(10)
    #df.where((F.col("regiao") == 'Norte') | (F.col("estado") == 'AM')).show(10)
    #df.filter((F.col("regiao") == 'Norte')).filter("estado like 'A%'").show(10)
    #df.filter("regiao in ('Norte','Sul')").show(1000)
    #lista_regiao = ["Norte","Sul"]
    #df.filter(F.col("regiao").isin(lista_regiao)).show(1000)
    #df.filter(F.col("regiao").startswith("C")).show(1000)
    #df.filter(F.col("regiao").like("C%")).show(1000)

    #print(dir("regiao"))
    #print(dir(F.col("regiao")))


