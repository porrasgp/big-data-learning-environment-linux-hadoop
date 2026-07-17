# 🚀 Configuración de Hadoop en Linux

> [!NOTE]
> Esta guía explica cómo utilizar los archivos del directorio `setup/`
> para configurar un entorno Hadoop completamente funcional.

---

# 📚 Tabla de Contenido

- 🎯 Objetivo
- 📁 Estructura del proyecto
- 📦 Archivos de configuración
- ⚙️ Paso 1 — Configurar `.bashrc`
- 🖥️ Paso 2 — Configurar Hadoop
- 🔍 Verificación
- ❗ Solución de problemas

---

# 🎯 Objetivo

Después de completar esta guía tendrás instalado:

| Software | Estado |
|----------|---------|
| ☕ Java 11 | ✅ |
| 🐘 Hadoop | ✅ |
| 🐝 Hive | ✅ |
| ⚡ Spark | ✅ |

---

# 📁 Directorio setup

```
setup/
│
├── bashrc.txt
├── core-site.txt
├── hdfs-site.txt
├── mapred-site.txt
├── yarn-site.txt
└── README.md
```

Cada archivo contiene la configuración necesaria para un componente de Hadoop.

---

# ⚙️ Paso 1 — Configurar .bashrc

## 📍 Archivo

```
~/.bashrc
```

Abre el archivo

```bash
nano ~/.bashrc
```

Ve hasta el final del documento.

> [!IMPORTANT]
> **NO elimines el contenido existente.**
>
> Únicamente agrega el contenido de:

```
setup/bashrc.txt
```

o directamente

```bash
cat setup/bashrc.txt >> ~/.bashrc
```

Guarda

```
CTRL + X
Y
ENTER
```

Ahora aplica los cambios

```bash
source ~/.bashrc
```

---

# ⚙️ Paso 2 — Configurar core-site.xml

## Archivo

```
$HADOOP_HOME/etc/hadoop/core-site.xml
```

Abrir

```bash
nano $HADOOP_HOME/etc/hadoop/core-site.xml
```

Copiar completamente el contenido de

```
setup/core-site.txt
```

Guardar

```
CTRL + X
Y
ENTER
```

---

# 🧩 Paso 3 — hdfs-site.xml

📄 Archivo destino

```
$HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

📄 Copiar desde

```
setup/hdfs-site.txt
```

---

# 🧩 Paso 4 — mapred-site.xml

Destino

```
$HADOOP_HOME/etc/hadoop/mapred-site.xml
```

Copiar

```
setup/mapred-site.txt
```

---

# 🧩 Paso 5 — yarn-site.xml

Destino

```
$HADOOP_HOME/etc/hadoop/yarn-site.xml
```

Copiar

```
setup/yarn-site.txt
```

---

# 🔍 Verificar la instalación

Ejecuta

```bash
echo $JAVA_HOME

echo $HADOOP_HOME

echo $PATH
```

Si todo está correcto continúa con

```bash
hdfs namenode -format
```

Después

```bash
start-dfs.sh

start-yarn.sh
```

Verifica

```bash
jps
```

Deberías obtener algo similar

```
NameNode
DataNode
SecondaryNameNode
NodeManager
ResourceManager
Jps
```

---

# 🌐 Interfaces Web

| Servicio | URL |
|----------|------|
| 🗄️ HDFS | http://localhost:9870 |
| ⚙️ YARN | http://localhost:8088 |

---

# 📌 Resumen

| Archivo | Destino |
|----------|----------|
| bashrc.txt | ~/.bashrc |
| core-site.txt | core-site.xml |
| hdfs-site.txt | hdfs-site.xml |
| mapred-site.txt | mapred-site.xml |
| yarn-site.txt | yarn-site.xml |

---

# 💡 Consejos

> [!TIP]
> Haz una copia de respaldo antes de modificar cualquier archivo.

```bash
cp ~/.bashrc ~/.bashrc.bak
```

---

# 🚨 Problemas comunes

> [!WARNING]
> Si Hadoop no inicia:

- Verifica JAVA_HOME
- Ejecuta `jps`
- Revisa `$HADOOP_HOME/logs`

---

# 🎉 ¡Listo!

Si llegaste hasta aquí ya tienes configurado el entorno básico de Hadoop y puedes continuar con Hive y Spark.

Happy Big Data! 🚀
