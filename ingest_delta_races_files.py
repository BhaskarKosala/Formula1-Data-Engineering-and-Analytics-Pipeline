# Databricks notebook source
# MAGIC %md
# MAGIC ### Ingest races.csv file

# COMMAND ----------

dbutils.widgets.text("p_data_source", "")
v_data_source = dbutils.widgets.get("p_data_source")

# COMMAND ----------

dbutils.widgets.text("p_file_date", "2021-03-21")
v_file_date = dbutils.widgets.get("p_file_date")

# COMMAND ----------

# MAGIC %run "../Includes/configuration"

# COMMAND ----------

# MAGIC %run "../Includes/common_functions"

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType

# COMMAND ----------

races_schema = StructType(fields=[StructField("raceId", IntegerType(), False),
                                   StructField("year", IntegerType(), True),
                                   StructField("round", IntegerType(), True),
                                   StructField("circuitId", IntegerType(), True),
                                   StructField("name", StringType(), True),
                                   StructField("date", DateType(), True),
                                   StructField("time", StringType(), True),
                                   StructField("url", StringType(), True)])

# COMMAND ----------

races_df = spark.read \
    .option("header", True) \
    .schema(races_schema) \
    .csv(f"{incremental_raw_folder_path}/{v_file_date}/races.csv")

# COMMAND ----------

from pyspark.sql.functions import current_timestamp, concat, col, lit, try_to_timestamp

# COMMAND ----------


races_df = races_df.withColumn("datetime_str", concat(col("date"), lit(" "), col("time")))

races_with_timestamp_df = races_df.withColumn("ingestion_date", current_timestamp()) \
    .withColumn("race_timestamp", try_to_timestamp(col("datetime_str"))) \
    .withColumn("data_source", lit(v_data_source)) \
    .withColumn("file_date", lit(v_file_date))


# COMMAND ----------

races_selected_df = races_with_timestamp_df.select(col("raceId").alias("race_id"),
                                            col("year").alias("race_year"),
                                            col("round"),
                                            col("circuitId").alias("circuit_id"),
                                            col("name"),
                                            col("ingestion_date"),
                                            col("race_timestamp"),
                                            col("data_source"))

# COMMAND ----------

races_selected_df.write.mode("overwrite").partitionBy('race_year').format("delta").saveAsTable("f1_delta_processed.races")

# COMMAND ----------

dbutils.notebook.exit("Success")