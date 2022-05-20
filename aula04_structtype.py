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

    schema = (StructType([
      StructField("regiao", StringType(), True),
      StructField("estado", StringType(), True),
      StructField("data", StringType(), True),
      StructField("casosNovos", IntegerType(), True),
      StructField("casosAcumulados", IntegerType(), True),
      StructField("obitosNovos", IntegerType(), True),
      StructField("obitosAcumulados", IntegerType(), True),
    ]))

    df = (spark
          .read
          .format("csv")
          .option("header","true")
          .option("inferSchema","false")
          .option("delimiter",";")
          .load("csv/arquivo_geral.csv", schema = schema))

    df.printSchema()