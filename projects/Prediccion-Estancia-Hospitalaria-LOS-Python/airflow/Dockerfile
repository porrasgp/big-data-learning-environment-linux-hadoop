FROM apache/airflow:2.10.5-python3.11

ENV AIRFLOW_HOME=/opt/airflow
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

USER root

# ------------------------------------------------------------
# Java (requerido por Spark) y utilidades de descarga
# ------------------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openjdk-17-jdk-headless \
        wget \
        procps && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# ------------------------------------------------------------
# Apache Spark
# ------------------------------------------------------------
ENV SPARK_VERSION=3.5.3
ENV SPARK_HADOOP_VERSION=3
ENV SPARK_HOME=/opt/spark

RUN wget -q "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_VERSION}.tgz" -O /tmp/spark.tgz && \
    tar -xzf /tmp/spark.tgz -C /opt/ && \
    mv "/opt/spark-${SPARK_VERSION}-bin-hadoop${SPARK_HADOOP_VERSION}" "${SPARK_HOME}" && \
    rm /tmp/spark.tgz

ENV PATH="${SPARK_HOME}/bin:${PATH}"

# ------------------------------------------------------------
# Dependencias Python (pandas, openpyxl, pyspark, etc.)
# ------------------------------------------------------------
COPY requirements.txt /requirements.txt

USER airflow
RUN pip install --no-cache-dir -r /requirements.txt

WORKDIR /opt/airflow
