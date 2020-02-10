# # Spark-SQL from PySpark
# 
# In this code we are simply checking that we can talk to the hive metastore, query data and create secondary tables.

#NOTE: In CDP find the HMS warehouse directory and external table directory by browsing to:
# Environment -> <env name> ->  Data Lake Cluster -> Cloud Storage

#Data taken from ibm telco dataset
#aws configure
#aws s3 cp raw/ibm.xlsx s3://ml-field/demo/telco/

s3_bucket = os.environ.get('S3_BUCKET', "s3a://ml-field/demo/telco/")
s3_bucket_region = os.environ.get('S3_BUCKET_REGION', "us-west-2")

from __future__ import print_function
import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import Row, StructField, StructType, StringType, IntegerType

spark = SparkSession\
    .builder\
    .appName("PythonSQL")\
    .master("local[*]") \
    .getOrCreate()

#    .config("spark.hadoop.fs.s3a.s3guard.ddb.region", "us-west-2")\
#    .config("spark.yarn.access.hadoopFileSystems","s3a://ml-field/demo/flight-analysis/data/")\
#    .config("spark.executor.instances", 2)\
#    .config("spark.driver.maxResultSize","4g")\
#    .config("spark.executor.memory", "4g")\
#    .config("fs.s3a.metadatastore.impl","org.apache.hadoop.fs.s3a.s3guard.NullMetadataStore")\


spark.sql("SHOW databases").show()
spark.sql("USE default")
spark.sql("SHOW tables").show()

#spark.sql("DROP TABLE IF EXISTS `default`.`telco`").show()
statement = '''
CREATE EXTERNAL TABLE IF NOT EXISTS `default`.`telco` ( 
`gender` string ,
`SeniorCitizen` boolean ,
`Partner` boolean ,
`Dependents` boolean ,
`tenure` int ,
`PhoneService` boolean ,
`MultipleLines` boolean ,
`InternetService` string ,
`OnlineSecurity` boolean ,
`OnlineBackup` boolean ,
`DeviceProtection` boolean ,
`TechSupport` boolean ,
`StreamingTV` boolean ,
`StreamingMovies` boolean ,
`Contract` string ,
`PaperlessBilling` boolean ,
`PaymentMethod` string ,
`MonthlyCharges` double ,
`TotalCharges` double )
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
STORED AS TextFile 
LOCATION 's3a://ml-field/demo/telco/'
'''
spark.sql(statement) 
spark.sql("DESCRIBE EXTENDED `default`.`telco`").collect()

spark.sql("SELECT * FROM `default`.`telco` LIMIT 5").take(5)
    
spark.stop()
