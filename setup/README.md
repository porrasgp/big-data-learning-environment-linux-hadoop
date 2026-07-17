---
title: "Guía de Configuración de Hadoop en Linux"
author: "Giovanni Solano Porras"
date: "`r Sys.Date()`"
output: html_document
---

# Introducción

Esta guía explica cómo agregar los archivos de configuración de Hadoop en Linux utilizando los archivos disponibles en el repositorio de GitHub.

Repositorio utilizado:

```
https://github.com/porrasgp/big-data-learning-environment-linux-hadoop
```

# Requisitos previos

- Ubuntu instalado
- Java 11 instalado
- Hadoop 3.4.1 descargado
- Usuario `hdoop` configurado
- SSH funcionando sin contraseña

# Configuración de variables de entorno (.bashrc)

Abrir el archivo:

```bash
nano ~/.bashrc
```

Agregar el contenido del archivo del repositorio:

```
https://github.com/porrasgp/big-data-learning-environment-linux-hadoop/blob/main/setup/bashrc.txt
```

Aplicar los cambios:

```bash
source ~/.bashrc
```

# Configuración de core-site.xml

Editar el archivo:

```bash
nano $HADOOP_HOME/etc/hadoop/core-site.xml
```

Copiar el contenido desde:

```
https://github.com/porrasgp/big-data-learning-environment-linux-hadoop/blob/main/setup/core-site.txt
```

Guardar con:

```
Ctrl + X → Y → Enter
```

# Configuración de hdfs-site.xml

Editar:

```bash
nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

Copiar desde:

```
https://github.com/porrasgp/big-data-learning-environment-linux-hadoop/blob/main/setup/hdfs-site.txt
```

# Configuración de mapred-site.xml

Editar:

```bash
nano $HADOOP_HOME/etc/hadoop/mapred-site.xml
```

Copiar desde:

```
https://github.com/porrasgp/big-data-learning-environment-linux-hadoop/blob/main/setup/mapred-site.txt
```

# Configuración de yarn-site.xml

Editar:

```bash
nano $HADOOP_HOME/etc/hadoop/yarn-site.xml
```

Copiar desde:

```
https://github.com/porrasgp/big-data-learning-environment-linux-hadoop/blob/main/setup/yarn-site.txt
```

# Configuración de JAVA_HOME en Hadoop

Editar:

```bash
nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```

Verificar que exista:

```bash
export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
```

# Formatear el NameNode

```bash
hdfs namenode -format
```

# Iniciar Hadoop

```bash
start-dfs.sh
start-yarn.sh
```

# Verificar procesos

```bash
jps
```

Deberían aparecer procesos como:

- NameNode
- DataNode
- ResourceManager
- NodeManager

# Verificación Web

- HDFS: http://localhost:9870
- YARN: http://localhost:8088

# Conclusión

Con esta guía se pueden agregar rápidamente todos los archivos de configuración necesarios utilizando los archivos del directorio `setup/` del repositorio GitHub.
