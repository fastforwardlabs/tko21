from pyspark.sql import SparkSession
import os

VW_URL='jdbc:hive2://hs2-default-vw.env-md95d2.dwx.cloudera.site/default;transportMode=http;httpPath=cliservice;ssl=true;retries=3'
JDBC_USERNAME='trial1910'
JDBC_PW='B5y+b4+D'
JDBC_URL=VW_URL+';user='+JDBC_USERNAME+';password='+JDBC_PW

spark = SparkSession\
    .builder\
    .appName("CDW Test")\
    .config("spark.security.credentials.hiveserver2.enabled","false ")\
    .config("spark.datasource.hive.warehouse.read.via.llap","false")\
    .config("spark.datasource.hive.warehouse.read.jdbc.mode", "client")\
    .config("spark.sql.hive.hiveserver2.jdbc.url", JDBC_URL)\
    .getOrCreate()
    
#.config("spark.jars", "/etc/spark/jars/hive-warehouse-connector-assembly-1.0.0.7.1.0.0-565.jar")\
#os.environ["PYTHONPATH"] += os.pathsep + '/etc/spark/python/lib/pyspark_hwc-1.0.0.7.1.0.0-565.zip'

sys.path.append('/etc/spark/python/lib/pyspark_hwc-1.0.0.7.1.0.0-565.zip')

from pyspark_llap.sql.session import HiveWarehouseSession
hive = HiveWarehouseSession.session(spark).build()
hive.showDatabases().show()
hive.showTables().show()
hive.setDatabase("default")
hive.sql("select code from airlines_new_orc").show()
hive.sql("select * from smaller_flight_table").show()  

#SELECT * FROM smaller_flight_table LIMIT 10;

spark.stop()