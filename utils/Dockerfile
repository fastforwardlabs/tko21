FROM docker.repository.cloudera.com/cdsw/engine:11-cml1.4
  WORKDIR /tmp
  COPY ./hive_warehouse_connector-20200209T135733Z-001.zip ./requirements3.txt ./install.R ./rserver.conf ./rstudio-cdsw /tmp/
  RUN /usr/local/bin/pip3 install -r /tmp/requirements3.txt && \
    apt-get update && apt-get dist-upgrade -y && \
    apt-get install -y --no-install-recommends \
      libapparmor1 \
      libclang-dev \
      lsb-release \
      psmisc && \
    wget https://download2.rstudio.org/server/trusty/amd64/rstudio-server-1.2.1335-amd64.deb && \
    dpkg -i rstudio-server-1.2.1335-amd64.deb && \
    mv /tmp/rserver.conf /etc/rstudio/rserver.conf && \
    mv /tmp/rstudio-cdsw /usr/local/bin/rstudio-cdsw  && \
    chmod +x /usr/local/bin/rstudio-cdsw && \
    /usr/local/bin/Rscript install.R && \
    /usr/bin/unzip /tmp/hive_warehouse_connector-20200209T135733Z-001.zip -d /tmp/ && \
    rm /tmp/hive_warehouse_connector-20200209T135733Z-001.zip && \
    mv /tmp/hive_warehouse_connector/pyspark_hwc-1.0.0.7.1.0.0-565.zip /etc/spark/python/lib/ && \
    mv /tmp/hive_warehouse_connector/hive-warehouse-connector-assembly-1.0.0.7.1.0.0-565.jar /etc/spark/jars/ && \
    mv /tmp/hive_warehouse_connector/cm-auto-global_truststore.jks /etc/ssl/certs/java/ 
