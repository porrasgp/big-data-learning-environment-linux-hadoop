from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.feature import StandardScaler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline

# ============================================================
# CREATE SPARK SESSION
# ============================================================

spark = SparkSession.builder \
    .appName("Hospital LOS Prediction") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ============================================================
# LOAD DATA FROM HDFS
# ============================================================

input_path = "hdfs:///user/hdoop/hospital/input/hospital_covid_data.csv"

print("Loading dataset from HDFS...")

# Infer schema automatically

df = spark.read.csv(
    input_path,
    header=True,
    inferSchema=True
)

print("Dataset Loaded Successfully")

# ============================================================
# MISSING VALUES PROCESSING (BLOQUE CORREGIDO / NUEVO)
# ============================================================

# Se añadieron estas líneas para definir las listas que faltaban:
categorical_columns = [
    field.name for field in df.schema.fields 
    if isinstance(field.dataType, StringType)
]

numeric_columns = [
    field.name for field in df.schema.fields 
    if isinstance(field.dataType, (IntegerType, DoubleType, FloatType, LongType))
]

# Tu bucle original para categóricos se mantuvo:
for col_name in categorical_columns:
    df = df.fillna({col_name: "Unknown"})

# Se añadió este bucle opcional para que los valores numéricos nulos no rompan el modelo:
for col_name in numeric_columns:
    df = df.fillna({col_name: 0})

print("Missing values processed")






# ============================================================
# FEATURE ENGINEERING
# ============================================================

# Example target column
# Replace with your real LOS column if different

TARGET_COLUMN = "Stay (in days)"

# Remove rows where target is null

df = df.filter(col(TARGET_COLUMN).isNotNull())

# CAMBIO: Se añadió esta línea para asegurar el tipo de dato correcto
df = df.withColumn(TARGET_COLUMN, col(TARGET_COLUMN).cast(DoubleType()))


# Encode categorical columns

indexers = []

for column in categorical_columns:
    if column != TARGET_COLUMN:
        indexer = StringIndexer(
            inputCol=column,
            outputCol=column + "_indexed",
            handleInvalid="keep"
        )
        indexers.append(indexer)

# Numerical feature columns

numeric_features = [
    c for c in numeric_columns
    if c != TARGET_COLUMN
]

# Indexed categorical feature columns

indexed_features = [
    c + "_indexed"
    for c in categorical_columns
    if c != TARGET_COLUMN
]

# Final feature list

feature_columns = numeric_features + indexed_features

# Assemble features

assembler = VectorAssembler(
    inputCols=feature_columns,
    outputCol="features_raw"
)

# Scale features

scaler = StandardScaler(
    inputCol="features_raw",
    outputCol="features",
    withStd=True,
    withMean=False
)



# ============================================================
# MODEL DEFINITION
# ============================================================

rf = RandomForestRegressor(
    featuresCol="features",
    labelCol=TARGET_COLUMN,
    numTrees=100,
    maxDepth=10
)

# ============================================================
# PIPELINE
# ============================================================


pipeline = Pipeline(stages=indexers + [assembler, scaler, rf])

# ============================================================
# TRAIN TEST SPLIT
# ============================================================

train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

print(f"Training rows: {train_df.count()}")
print(f"Testing rows: {test_df.count()}")

# ============================================================
# TRAIN MODEL
# ============================================================

print("Training model...")

model = pipeline.fit(train_df)

print("Model training completed")

# ============================================================
# PREDICTIONS
# ============================================================

predictions = model.transform(test_df)

predictions.select(
    TARGET_COLUMN,
    "prediction"
).show(20)

# ============================================================
# EVALUATION
# ============================================================

rmse_evaluator = RegressionEvaluator(
    labelCol=TARGET_COLUMN,
    predictionCol="prediction",
    metricName="rmse"
)

mae_evaluator = RegressionEvaluator(
    labelCol=TARGET_COLUMN,
    predictionCol="prediction",
    metricName="mae"
)

r2_evaluator = RegressionEvaluator(
    labelCol=TARGET_COLUMN,
    predictionCol="prediction",
    metricName="r2"
)

rmse = rmse_evaluator.evaluate(predictions)
mae = mae_evaluator.evaluate(predictions)
r2 = r2_evaluator.evaluate(predictions)

print("=" * 50)
print("MODEL EVALUATION")
print("=" * 50)
print(f"RMSE: {rmse}")
print(f"MAE : {mae}")
print(f"R2  : {r2}")


# ============================================================
# SAVE PROCESSED DATA
# ============================================================

output_path = "hdfs:///user/hdoop/hospital/output/predictions"

predictions.select(
    TARGET_COLUMN,
    "prediction"
).write.mode("overwrite").csv(output_path, header=True)

print("Predictions saved to HDFS")

# ============================================================
# SAVE MODEL
# ============================================================

model_path = "hdfs:///user/hdoop/hospital/output/model"

model.write().overwrite().save(model_path)

print("Model saved to HDFS")

# ============================================================
# STOP SESSION
# ============================================================

spark.stop()

print("Spark job completed successfully")
