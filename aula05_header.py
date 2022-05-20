# Databricks notebook source
#from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

if __name__ == "__main__":

    spark = (SparkSession.builder
        .master("local[*]")
        .appName("estudando-dataframes")
        .getOrCreate())

    df = (spark
          .read
          .format("csv")
          .option("header", "true")
          .option("inferSchema", "true")
          .option("delimiter", ";")
          .load("csv/arquivo_geral.csv"))

    df.printSchema()