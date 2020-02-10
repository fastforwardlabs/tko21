FROM docker.repository.cloudera.com/cdsw/engine:11-cml1.4-hwc-v1
  WORKDIR /tmp
  COPY ./requirements3.txt ./install.R ./rserver.conf ./rstudio-cdsw /tmp/
  RUN /usr/local/bin/pip3 install -r /tmp/requirements3.txt && \
    apt-get update && apt-get dist-upgrade -y && \
    apt-get install -y --no-install-recommends \
      libapparmor1 \
      libclang-dev \
      lsb-release \
      sudo \
      psmisc && \
    wget https://download2.rstudio.org/server/trusty/amd64/rstudio-server-1.2.1335-amd64.deb && \
    dpkg -i rstudio-server-1.2.1335-amd64.deb && \
    mv /tmp/rserver.conf /etc/rstudio/rserver.conf && \
    mv /tmp/rstudio-cdsw /usr/local/bin/rstudio-cdsw  && \
    chmod +x /usr/local/bin/rstudio-cdsw && \
    /usr/local/bin/Rscript install.R 
