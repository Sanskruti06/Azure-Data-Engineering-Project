# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Access using App

# COMMAND ----------
import os

app_id = os.getenv("AZURE_CLIENT_ID")
tenant_id = os.getenv("AZURE_TENANT_ID")
secret = os.getenv("AZURE_CLIENT_SECRET")

spark.conf.set("fs.azure.account.auth.type.projstorage.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.projstorage.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.projstorage.dfs.core.windows.net", app_id)
spark.conf.set("fs.azure.account.oauth2.client.secret.projstorage.dfs.core.windows.net", secret)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.projstorage.dfs.core.windows.net", f"https://login.microsoftonline.com/{tenant_id}/oauth2/token")


# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Loading

# COMMAND ----------

df_cal = spark.read.format('csv').option("header", True).option("inferSchema", True).load("abfss://bronze@projstorage.dfs.core.windows.net/AdventureWorks_Calendar")

# COMMAND ----------

df_cus = spark.read.format('csv').option("header", True).option("inferSchema", True).load("abfss://bronze@projstorage.dfs.core.windows.net/AdventureWorks_Customers")

# COMMAND ----------

df_procat = spark.read.format('csv').option("header", True).option("inferSchema", True).load("abfss://bronze@projstorage.dfs.core.windows.net/AdventureWorks_Product_Categories")

# COMMAND ----------

df_pro = spark.read.format('csv').option("header", True).option("inferSchema", True).load("abfss://bronze@projstorage.dfs.core.windows.net/AdventureWorks_Products")

# COMMAND ----------

df_ret = spark.read.format('csv').option("header", True).option("inferSchema", True).load("abfss://bronze@projstorage.dfs.core.windows.net/AdventureWorks_Returns")

# COMMAND ----------

df_sal = spark.read.format('csv').option("header", True).option("inferSchema", True).load("abfss://bronze@projstorage.dfs.core.windows.net/AdventureWorks_Sales*")

# COMMAND ----------

df_ter = spark.read.format('csv').option("header", True).option("inferSchema", True).load("abfss://bronze@projstorage.dfs.core.windows.net/AdventureWorks_Territories")

# COMMAND ----------

df_subcat = spark.read.format('csv').option("header", True).option("inferSchema", True).load("abfss://bronze@projstorage.dfs.core.windows.net/Product_Subcategories")

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformations**

# COMMAND ----------

df_cal.display()

# COMMAND ----------

df_cal = df_cal.withColumn('Month', month(col("Date"))).withColumn("Year", year(col("Date")))
df_cal.display()

# COMMAND ----------

df_cus.display()

# COMMAND ----------

df_cus.withColumn("Full Name", concat(col('Prefix'),lit(' '),col('FirstName'),lit(' '),col('LastName'))).display()

# COMMAND ----------

df_pro.display()

# COMMAND ----------

df_pro = df_pro.withColumn("ProductSKU", split(col("ProductSKU"), '-')[0])\
                .withColumn("ProductName", split(col("ProductName"), ' ')[0])

df_pro.display()

# COMMAND ----------

df_sal.display()

# COMMAND ----------

df_sal = df_sal.withColumn("StockDate", to_timestamp("StockDate"))

df_sal = df_sal.withColumn("OrderNumber", regexp_replace("OrderNumber", "S", "T"))

df_sal = df_sal.withColumn("Multiply", col("OrderLineItem")*col("OrderQuantity"))

df_sal.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Sales Analysis**

# COMMAND ----------

df_sal = df_sal.groupBy("OrderDate").agg(count("OrderNumber").alias("Total Orders"))
df_sal.display()

# COMMAND ----------

df_procat.display()

# COMMAND ----------

df_ter.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Push data from bronze to silver container**

# COMMAND ----------

df_cus.write.format('parquet')\
    .mode('append')\
    .option('path', 'abfss://silver@projstorage.dfs.core.windows.net/AdventureWorks_Customers')\
    .save()

# COMMAND ----------

df_cal.write.format('parquet')\
    .mode('append')\
    .option('path', 'abfss://silver@projstorage.dfs.core.windows.net/AdventureWorks_Calendar')\
    .save()

# COMMAND ----------

df_subcat.write.format('parquet')\
    .mode('append')\
    .option('path', 'abfss://silver@projstorage.dfs.core.windows.net/Product_Subcategories')\
    .save()

# COMMAND ----------

df_pro.write.format('parquet')\
    .mode('append')\
    .option('path', 'abfss://silver@projstorage.dfs.core.windows.net/AdventureWorks_Products')\
    .save()

# COMMAND ----------

df_ret.write.format('parquet')\
    .mode('append')\
    .option('path', 'abfss://silver@projstorage.dfs.core.windows.net/AdventureWorks_Returns')\
    .save()

# COMMAND ----------

df_ter.write.format('parquet')\
    .mode('append')\
    .option('path', 'abfss://silver@projstorage.dfs.core.windows.net/AdventureWorks_Territories')\
    .save()

# COMMAND ----------

df_sal.write.format('parquet')\
    .mode('append')\
    .option('path', 'abfss://silver@projstorage.dfs.core.windows.net/AdventureWorks_Sales')\
    .save()

# COMMAND ----------

